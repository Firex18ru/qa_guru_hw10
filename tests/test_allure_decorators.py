import allure

from selene import browser, by, be

from selene.support.shared.jquery_style import s


def test_decorator_step():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_number("#76")


@allure.step("открываем страницу Github")
def open_main_page():
    browser.open("https://github.com")


@allure.step("ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issues с номером {number}")
def should_see_number(number):
    s(by.partial_text(number)).should(be.visible)
