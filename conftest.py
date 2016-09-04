import pytest
import json
import os.path
from fixture.application import Application

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as config:
            target = json.load(config)
    return target


@pytest.fixture
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid:
        fixture = Application(baseurl=web_config["baseURL"])
    fixture.session.login("administrator", "secret")
    #fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
