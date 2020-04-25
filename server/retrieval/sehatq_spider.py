import os
import re
import scrapy
from typing import Dict, List, IO


class SehatQSpider(scrapy.Spider):
    name = 'SehatQ: Penyakit - Spider'
    start_urls = ['https://www.sehatq.com/penyakit']

    def __init__(self, write_path: str = None):
        super(SehatQSpider, self).__init__()
        self.write_path: str = write_path
        if self.write_path is not None:
            self.results: List[Dict[str, str]] = []

    def parse(self, response: scrapy.http.Response):
        for url_penyakit in response.css('.content-item>a ::attr(href)').getall():
            yield response.follow(url_penyakit, self.parse_penyakit)

    def parse_penyakit(self, response: scrapy.http.Response):
        contents = []
        for content_element in response.css('div.dynamic-content.large'):
            paragraph = ''
            for content in content_element.css('::text').getall():
                stripped_content = re.sub(r"\\x[a-z0-9]{2}", " ", content)
                if len(stripped_content) > 0:
                    paragraph += ' ' + stripped_content
            contents.append(paragraph)

        result = {
            "url": response.url,
            "title": response.css('div.content-item.has-top.mb-4>h1 ::text').get().strip(),
            "content": '\n'.join(par.strip() for par in contents).strip()
        }
        if self.write_path is not None:
            self.results.append(result)
        yield result

    def close(self, reason: str):
        if self.write_path is not None and reason == 'finished':
            if os.path.isfile(self.write_path):
                os.remove(self.write_path)
            result_file_pointer: IO = open(self.write_path, 'w+')
            for result in self.results:
                result_file_pointer.write(
                    f"<DOC>\n<URL>{result['url']}</URL>\n<TITLE>{result['title']}</TITLE>\n<CONTENT>\n{result['content']}\n</CONTENT>\n</DOC>\n")
            result_file_pointer.close()
