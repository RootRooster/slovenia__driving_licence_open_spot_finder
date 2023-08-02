import scrapy
from datetime import date


class ACategoryScraperSpider(scrapy.Spider):
    name = "a_category"
    allowed_domains = ["e-uprava.gov.si"]

    def start_requests(self):
        curr_date = date.today()
        # format date to "2023-08-03" string
        curr_date = curr_date.strftime("%Y-%m-%d")
        url = f"https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?&type=-&cat=4&izpitniCenter=18&lokacija=171&calendar_date={date}&offset=731&sentinel_type=ok&sentinel_status=ok&is_ajax=1&complete=false"
        url_test = url + "&page=7"
        yield scrapy.Request(url=url_test, callback=self.parse)


    def parse(self, response):
        response_data = response.text
        self.logger.info(response_data)
