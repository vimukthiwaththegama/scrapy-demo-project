import scrapy
from pathlib import Path

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    

     
    start_urls = [  "https://books.toscrape.com",
                        "https://quotes.toscrape.com/page/1/",
                        "https://quotes.toscrape.com/page/2/"]
            
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f"quotes-{page}.html"
    #     Path(filename).write_bytes(response.body)
    #     self.log(f"Saved file {filename}")
    def parse(self,response):
        for  quote in response.css("div.css"):
            yield{
                "text":quote.css("span.text::text").get(),
                "author":quote.css("small.author::text").get(),
                "tags":quote.css("div.tags a.tag::tag.text").getall(),
            }