import scrapy
from pathlib import Path

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    
    def start_requests(self):
     
        start_urls = [  "https://books.toscrape.com",
                        "https://quotes.toscrape.com/page/1/",
                        "https://quotes.toscrape.com/page/2/"]
        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
            
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")