import scrapy
from datetime import date
from time import sleep
JESENICE = 171
KRANJ = 223

class ACategoryScraperSpider(scrapy.Spider):
    name = "a_category"
    allowed_domains = ["e-uprava.gov.si"]
    base_url = ""

    def __init__(self, name=None, **kwargs):
        self.location = kwargs.get('location')
        assert self.location == "kranj" or self.location == "jesenice", "location parameter should be either kranj or jesenice"
        if self.location == "kranj":
            self.location = str(KRANJ)
        if self.location == "jesenice":
            self.location = str(JESENICE)

    def start_requests(self):
        curr_date = date.today()
        # format date to "2023-08-03" string
        curr_date = curr_date.strftime("%Y-%m-%d")        
        self.base_url = f"https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?&type=-&cat=4&izpitniCenter=18&lokacija={self.location}&calendar_date={curr_date}&offset=731&sentinel_type=ok&sentinel_status=ok&is_ajax=1&complete=false"
        self.crawler.stats.set_value('pages_checked', 0)
        yield scrapy.Request(url=self.base_url, callback=self.parse, meta={"playwright": True})


    def parse(self, response):
        open_appointments = response.css('didv.js_dogodekBox.dogodek')
        if len(open_appointments) == 0:
            # no appointments found on this page, go to next page
            self.crawler.stats.inc_value('pages_checked')
            new_url = self.base_url + "&page=" + str(self.crawler.stats.get_value('pages_checked'))
            yield scrapy.Request(url=new_url, callback=self.parse, meta={"playwright": True})
        else:
            # appointments found on this page
            for appointment in open_appointments:
                free_date = appointment.css(".sr-only::text").get().strip()
                self.log(f"Free date: {free_date}")
        
        
# new url
#https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?&type=1&cat=4&izpitniCenter=18&lokacija=223&calendar_date=2023-08-03&offset=163.5&sentinel_type=ok&sentinel_status=ok&is_ajax=1