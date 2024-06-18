import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("поиск issues в репозитории")
    allure.dynamic.story("issues отсутствует в репозитории")
    allure.dynamic.link("https://github.com", name="Github")


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Yakimenko")
@allure.feature("поиск issues в репозитории")
@allure.story("issues присутствует в репозитории")
@allure.link("https://github.com", name="Github")
def test_decorator_labels():
    pass
