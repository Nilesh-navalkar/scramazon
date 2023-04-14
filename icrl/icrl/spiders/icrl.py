import scrapy

class spidy(scrapy.Spider):
    name="spidy" 
    allowed_domains = ['amazon.in']
    start_urls=["https://www.amazon.in/s?rh=n%3A1389432031&fs=true&ref=lp_1389432031_sar"]
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

    def parse(self,response):
        for products in response.css('div.s-card-container'):
            dict={
                'name':products.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get(),
                'price':products.css('span.a-price-whole::text').get(),
                'link':'https://www.amazon.in'+products.css('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal').attrib['href']
            }
            #print(dict)
            yield dict
        next_page='https://www.amazon.in'+response.css('a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
    
#scrapy crawl spidy -o output.csv