from model.project import Project


def test_add_project(app):

    projects = app.project.get_projects()

    new_project = Project(name='NEW555', description='DESCRIPTION')
    app.project.add(new_project)
    new_projects = app.project.get_projects()

    projects.append(new_project)
    assert sorted(projects, key=Project.get_name) == sorted(new_projects, key=Project.get_name)
