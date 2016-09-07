from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, baseurl):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)
        self.baseurl = baseurl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get(self.baseurl)

    def destroy(self):
        self.wd.quit()
