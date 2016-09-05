from model.project import Project
import time

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    projects_cache = None

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("управление").click()
            wd.find_element_by_link_text("Управление проектами").click()

    def fill_form(self, project):
        wd = self.app.wd
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(project.name)
        self.select_status(project.status)
        if not project.inherit_global:
            wd.find_element_by_id("project-inherit-global").click()
        self.select_view_state(project.view_state)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(project.description)

    def add(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input.button-small").click()
        self.fill_form(project)
        wd.find_element_by_xpath("//span[@class='submit-button']/input").click()
        self.open_projects_page()
        self.projects_cache = None

    def count(self):
        wd = self.app.wd
        self.open_projects_page()
        entries = wd.find_elements_by_xpath("//div/div[4]/div[2]/table/tbody/tr")
        return int(len(entries))

    def get_projects(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.projects_cache = []
            entries = wd.find_elements_by_xpath("//div/div[4]/div[2]/table/tbody/tr")
            for element in entries:
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                description = cells[4].text
                self.projects_cache.append(Project(name=name, description=description))
        return list(self.projects_cache)

    def open_by_name(self, project):
        wd = self.app.wd
        wd.find_element_by_link_text(project.name).click()

    def delete_by_name(self, project):
        wd = self.app.wd
        self.open_projects_page()
        self.open_by_name(project)
        wd.find_element_by_xpath("//form[@id='project-delete-form']/fieldset/input[3]").click()
        wd.find_element_by_xpath("//div[@id='content']/div/form/input[4]").click()
        self.open_projects_page()
        self.projects_cache = None

    def select_status(self, status):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@id='project-status']").click()
        wd.find_element_by_xpath("//select[@id='project-status']//option["+str(status)+"]").click()

    def select_view_state(self, state):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@id='project-view-state']").click()
        wd.find_element_by_xpath("//select[@id='project-view-state']//option["+str(state)+"]").click()
