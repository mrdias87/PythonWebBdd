import pytest

from pytest_bdd import given
from selenium import webdriver

# Constants

PETZ_HOME = 'https://www.petz.com.br/'


# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Fixture

@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Shared Given Steps

@given('A pagina Petz é mostrada')
def ddg_home(browser):
    browser.get(PETZ_HOME)
