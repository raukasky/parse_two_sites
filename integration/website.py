import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from urllib.parse import urlparse, urljoin


class WebsiteIntegration:
    def __init__(self, url):
        self.url = url

    def get_domain(self):
        parsed_url = urlparse(self.url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return base_url

    def get_robots_file(self):
        parsed_url = urlparse(self.url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        robots_url = urljoin(base_url, '/robots.txt')
        try:
            response = requests.get(robots_url)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except RequestException as e:
            return e

    def get_sitemap(self):
        robots_txt = self.get_robots_file()
        if robots_txt is not None:
            lines = robots_txt.split('\n')
            for line in lines:
                if line.lower().startswith('sitemap'):
                    sitemap_url = line.split(': ')[1].strip()
                    return sitemap_url

    def get_disallow_path(self, user_agent='*'):
        robots_txt = self.get_robots_file()
        res = []
        if robots_txt is not None:
            lines = robots_txt.split('\n')
            user_agent_section = False
            for line in lines:
                if line.startswith('#'):
                    continue
                if line.lower().startswith('user-agent:'):
                    current_user_agent = line.split(': ')[1].strip()
                    user_agent_section = current_user_agent == '*' or current_user_agent == user_agent
                if user_agent_section and line.lower().startswith('disallow:'):
                    disallowed_path = line.split(': ')[1].strip()
                    res.append(str(disallowed_path))
        return res

    def get_title(self):
        parsed_url = urlparse(self.url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for title in soup.find_all('title'):
            return title.get_text()
