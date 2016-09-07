from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def get_projects(self, username, password):
        soap_projects = []
        client = Client("http://localhost/mantisbt-1.3.0/api/soap/mantisconnect.php?wsdl")
        try:
            accessible_projects = client.service.mc_projects_get_user_accessible(username, password)
            for project in accessible_projects:
                soap_projects.append(Project(name=project["name"]))
        except WebFault:
            print('fault')
        return soap_projects
