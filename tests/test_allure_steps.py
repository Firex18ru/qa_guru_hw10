import allure

from selene import browser, by, be

from selene.support.shared.jquery_style import s


def test_steps_github():
    with allure.step("открываем страницу Github"):
        browser.open("https://github.com")

    with allure.step("ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issues с номером 76"):
        s(by.partial_text("#76")).should(be.visible)
