from lxml import html
import requests

def spider(url):
	html_doc=requests.get(url).text
	selector=html.fromstring(html_doc)
	ul_list=selector.xpath("//div[@class='indexs']")
	print(len(ul_list))
	for li in ul_list:
		title=li.xpath("h2/text()")
		print(title)

if __name__=='__main__':
	spider('http://jandan.net')
