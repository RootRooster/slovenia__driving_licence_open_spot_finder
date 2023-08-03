import scrapy
from datetime import date


JESENICE = 171
KRANJ = 223


class ACategoryScraperSpider(scrapy.Spider):
    name = "a_category"
    allowed_domains = ["e-uprava.gov.si"]

    def start_requests(self):
        curr_date = date.today()
        curr_date = curr_date.strftime("%Y-%m-%d")
        urls = [
            f"https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?=&type=1&cat=4&izpitniCenter=18&lokacija={KRANJ}&calendar_date={curr_date}&offset=0&sentinel_type=ok&sentinel_status=ok&is_ajax=1",
            f"https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?=&type=1&cat=4&izpitniCenter=18&lokacija={JESENICE}&calendar_date={curr_date}&offset=0&sentinel_type=ok&sentinel_status=ok&is_ajax=1"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={"playwright": True})

    def parse(self, response):
        open_appointments = response.css('div.js_dogodekBox.dogodek')
        self.log(open_appointments)
        for appointment in open_appointments:
            free_date = appointment.css(".calendarBox > .sr-only::text").get()
            location = appointment.css(
                ".upperOpomnikDiv > span:nth-child(2)::text").get()
            time = appointment.css(
                ".contentOpomnik.celotnaSirina > div:nth-child(6) > span.bold::text").get()
            self.log(f"Free date: {free_date}")
            self.log(f"At location: {location}")
            self.log(f"At time: {time}\n")
