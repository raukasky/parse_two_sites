from services.deps import get_db
from crud import website
from tests.parse import WebsiteParse


def insert_website(url):
    db = next(get_db())
    websites = website.get_by_domain(db, url)
    if websites is None:
        return
    integration = WebsiteParse(url=url)
    data = {
        'title': integration.get_title(),
        'robots_txt': integration.get_robots_file(),
        'sitemap': integration.get_sitemap(),
        'disallow': integration.get_disallow_path(),
    }


