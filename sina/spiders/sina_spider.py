# -*- coding: utf-8 -*-
import scrapy
import urlparse

class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["sports.sina.cn"]
    start_urls = [
        "http://sina.cn/?pos=10&vt=4"
    ]
    spideredurl=[]

    def parse(self, response):
	#print response.selector.xpath("//title/text()")[0].extract()	
	if response.selector.xpath("//title/text()")[0].re(u'- 手机新浪网') or response.selector.re('commentConfig'):
		#print response.url+"--------OK"
		with open(self.allowed_domains[0]+'ok','a') as f:
			f.write(response.url+"\n")
	else:
		#print response.url+"-------- not OK"
		with open(self.allowed_domains[0]+'not_ok','a') as f:
			f.write(response.url+"\n")
	urls=response.selector.xpath("//a")
	for url in urls:
		link= url.xpath('@href')[0].extract()
		if urlparse.urlparse(link)[0]=='http' and link not in self.spideredurl:
                	#print link
			self.spideredurl.append(link)
			yield scrapy.Request(link, callback=self.parse)
