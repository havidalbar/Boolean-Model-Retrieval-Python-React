import os
import requests
from bs4 import BeautifulSoup
from itertools import repeat
from multiprocessing import Pool, cpu_count
from typing import Any, Dict, List, IO


def start_spider(write_path: str = None, debug: bool = False):
    start_url: str = 'https://www.sehatq.com/penyakit'
    hdr: Dict[str, str] = {'User-Agent': 'Mozilla/5.0'}
    landing_page_soup: BeautifulSoup = BeautifulSoup(
        requests.get(start_url, headers=hdr).text, 'lxml')

    penyakit_urls = {penyakit_element.get('href'): None
                     for penyakit_element in landing_page_soup.select('.content-item>a')
                     if penyakit_element.get('href').startswith(start_url)}

    p: Pool = Pool(cpu_count())
    result: List[Dict[str, str]] = p.starmap(
        scrape_penyakit, zip(penyakit_urls.keys(), repeat(debug)))
    p.close()
    p.join()

    if write_path is not None:
        if os.path.isfile(write_path):
            os.remove(write_path)
        result_file_pointer: IO = open(write_path, 'w+')
        for res in result:
            result_file_pointer.write(
                f"<DOC>\n<URL>{res['url']}</URL>\n<IMG>{res['img']}</IMG>\n<TITLE>{res['title']}</TITLE>\n<CONTENT>\n{res['content']}\n</CONTENT>\n</DOC>\n")
        result_file_pointer.close()

    return result


def scrape_penyakit(penyakit_url: str, debug: bool):
    hdr: Dict[str, str] = {'User-Agent': 'Mozilla/5.0'}
    success: bool = False
    result: Dict[str, str] = {}
    while not success:
        try:
            penyakit_soup: BeautifulSoup = BeautifulSoup(
                requests.get(penyakit_url, headers=hdr).text, 'lxml')

            processing_params: Dict[str, Any] = {
                'separator': ' ',
                'strip': True
            }
            result = {
                'url': penyakit_url,
                'img': penyakit_soup.select_one('figure.content-item.mb-3>div>div>img').get('src'),
                'title': penyakit_soup.select_one('div.content-item.has-top.mb-4>h1').get_text(**processing_params),
                'content': '\n'.join(f'{content_title.get_text(**processing_params)}\n{content_element.get_text(**processing_params)}'
                                     for content_title, content_element in zip(penyakit_soup.select('h2.d-inline'),
                                                                               penyakit_soup.select('div.dynamic-content.large')))
            }
            success = True
        except KeyboardInterrupt:
            exit()
        except:
            print(f'Retrying to: {penyakit_url}')

    if debug:
        print(result)
    return result
