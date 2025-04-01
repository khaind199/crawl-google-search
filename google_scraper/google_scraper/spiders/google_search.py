
import scrapy
import requests
from google_scraper.items import GoogleSearchItem

class GoogleSearchSpider(scrapy.Spider):
    name = "google_search"

    # API key của SerpAPI
    api_key = "b01b05a3e80ee7d840be90f95f7ac06c8bc830cc616909e927d10abb8c3e15c8"
    
    # URL của SerpAPI cho Google Local Search
    base_url = "https://serpapi.com/search"
    
    def start_requests(self):
        query = "106 Hoàng Quốc Việt restaurant"
        
        # Tạo tham số cho yêu cầu
        params = {
            "engine": "google_local",
            "q": query,
            "api_key": self.api_key
        }

        # Gửi yêu cầu đến SerpAPI
        response = requests.get(self.base_url, params=params)
        
        # Chuyển kết quả trả về thành dạng scrapy Response để tiếp tục xử lý
        if response.status_code == 200:
            json_response = response.json()
            yield from self.parse(json_response)
        else:
            self.logger.error("Request to SerpAPI failed with status code %d", response.status_code)

    def parse(self, response):
        # Dữ liệu trả về từ SerpAPI sẽ có một số trường chứa kết quả tìm kiếm
        local_results = response.get('local_results', [])
        for place in local_results:
            item = GoogleSearchItem()
            item['name'] = place.get("title", "N/A")
            item['address'] = place.get("address", "N/A")
            item['rating'] = place.get("rating", "N/A")
            item['reviews'] = place.get("reviews", "N/A")
            item['service_options'] = place.get("service_options", {})
            item['place_id'] = place.get("place_id", "N/A")
            item['place_id_search'] = place.get("place_id_search", "N/A")
            item['gps_coordinates'] = place.get("gps_coordinates", {})
            item['thumbnail'] = place.get("thumbnail", "No thumbnail available")
            item['type'] = place.get("type", "N/A")
            item['lsig'] = place.get("lsig", "N/A")
            item['description'] = place.get("description", "N/A")
            yield item
