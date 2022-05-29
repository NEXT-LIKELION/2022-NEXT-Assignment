import scrapy
import csv

file = open('kopas.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","date","source"])

class KoreapasSpider(scrapy.Spider):
    name = 'KoreapasSpider'
    allowed_domains = ['www.koreapas.com']
    start_urls = ['https://www.koreapas.com/bbs/main.php']

    def parse(self, response):
        
            titles = response.xpath('/html/body/div/div[5]/div[2]/div/table[2]/tr/td[1]/table/tr[1]/td[3]/div/ul/li/a/span/text()').extract()
            date = response.xpath('/html/body/div/div[5]/div[2]/div/table[2]/tr/td[1]/table/tr[1]/td[3]/div/ul/li[11]/span/text()').extract()
            

            for item in zip(titles):
                info = {
                    'title' : item[0].strip()
                }
                info['date'] = date
                info['source'] = "고파스"
                yield info

                row = []
                row.append(info['title'])
                row.append(info['date'])
                row.append(info['source'])
                writer.writerow(row)


                print("**************************")

    
