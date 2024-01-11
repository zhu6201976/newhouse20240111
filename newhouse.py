import base64

import execjs
import requests
from loguru import logger
from scrapy import Selector


class Newhouse(object):
    def __init__(self):
        self.session = requests.session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' +
                                                   ' (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        self.host_name = base64.b64decode('aHR0cHM6Ly9uZXdob3VzZS4wNTU3ZmRjLmNvbQ==').decode('utf-8')
        self.ctx = execjs.compile(self.read_js_code())

    def read_js_code(self):
        with open('./lanrenzhijia.js', 'r', encoding='utf-8') as f:
            return f.read()

    def parse_project(self):
        home_url = f'{self.host_name}'
        resp = self.session.get(home_url)
        s = Selector(response=resp)
        iptstamp = s.xpath('//input[@id="iptstamp"]/@value').get('')
        a_s = s.xpath('//a[@id and @onclick="reurl(this)"]')
        for a in a_s:
            project_name = a.xpath('./text()').get('')
            # project_url = a.xpath('./@href').get('')  # project_url JS动态生成
            project_id = a.xpath('./@id').get()
            if not project_id:
                continue

            project_href = self.ctx.call('reurl', {'id': project_id}, iptstamp)
            if not project_href:
                continue
            project_url = f'{self.host_name}{project_href}'

            resp = self.session.get(project_url)
            logger.info(f'{project_name} --> {project_id} --> {project_url} --> {resp.status_code}')

    def run(self):
        self.parse_project()


if __name__ == '__main__':
    obj = Newhouse()
    obj.run()
