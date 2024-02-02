import scrapy
import csv


class NewstitlespiderSpider(scrapy.Spider):

    name = "NewsTitleSpider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):

        titoli = []
        for title in response.css('h1::text').getall():
            titoli.append({'title': title})

        with open('NewsTitleSpider.csv', 'w', nwline = '') as csvfile:
            fieldames = ['title']    
            writer = csv.DictWriter(csvfile, fieldnames= fieldames)
            writer.writeheader()

            for title in titoli:
                writer.writerow(title)


        yield {'titoli' : titoli}        
