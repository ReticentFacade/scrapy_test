# from pathlib import Path
# import scrapy

# class QuotesSpider(scrapy.Spider):
#     name = "quotes_spider"

#     # def start_requests(self):
#     #     urls = [
#     #         "https://quotes.toscrape.com/tag/humor/page/1/",
#     #         "https://quotes.toscrape.com/page/2"
#     #     ]
#     #     for url in urls:
#     #         yield scrapy.Request(url = url, callback = self.parse)
#     start_urls = [
#         "https://quotes.toscrape.com/tag/humor/page/1/",
#         "https://quotes.toscrape.com/page/2"
#     ]
    
#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f"quotes-{page}.html"
#         Path(filename).write_bytes(response.body)
#         self.log(f"Saved file: {filename}")

import scrapy

class LinkedinPplSpider(scrapy.Spider):
    name = "linkedin_ppl_spider"

    # start_urls = [
    #     "",
    # ]
    def start_requests(self):
        profile_list = ["reidhoffman", "williamhgates"]
        for profile in profile_list:
            linkedin_ppl_url = f"https://www.linkedin.com/in/{profile}"
            yield scrapy.Request(url = linkedin_ppl_url, callback=self.parse_profile, meta={'profile': profile, 'linkedin_url': linkedin_ppl_url})

    def parse_profile(self, response):
        item = {}
        item['profile'] = response.meta['profile']
        item['url'] = response.meta['linkedin_url']

        """
            SUMMARY SECTION:
        """
        summary_box = response.css("section.top-card-layout")
        item['name'] = summary_box.css("h1::text").get().strip()
        item['description'] = summary_box.css("h2::text").get().strip()