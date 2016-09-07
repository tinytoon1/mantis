from model.project import Project
import random


def test_delete_project(app):
    if len(app.project.get_projects()) == 0:
        new_project = Project(name='NEW', description='DESCRIPTION')
        app.project.add(new_project)

    projects = app.soap.get_projects('administrator', 'secret')
    random_project = random.choice(projects)
    app.project.delete_by_name(random_project)

    new_projects = app.soap.get_projects('administrator', 'secret')
    projects.remove(random_project)
    assert sorted(projects, key=Project.get_name) == sorted(new_projects, key=Project.get_name)
