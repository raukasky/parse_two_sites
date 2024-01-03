import crud
from integration import WebsiteIntegration
from models import Website
from schemas import WebsiteDetail
from services.base import BaseDBService


class WebsiteService(BaseDBService):
    def create_website(self, url: str) -> WebsiteDetail:
        websites = crud.website.get_by_domain(url)
        if websites:
            return None
        else:
            integration = WebsiteIntegration(url)
            website = Website(**{
                'domain': integration.get_domain(),
                'robots_txt': integration.get_robots_file(),
                'sitemap': integration.get_sitemap(),
                'disallow': integration.get_disallow_path()
            })
        return WebsiteDetail.model_validate(website)
