import pytest
from playwright.sync_api import Page


def test_open_testing_academy(page: Page):
    """
    TC-001
    Ověření dostupnosti stránky Testing Akademie.
    """

    page.goto("https://engeto.cz/testing-akademie/")

    assert page.url == "https://engeto.cz/testovani-softwaru/"

def test_terms_page_is_available(page: Page):
    """
    TC-002
    Ověření dostupnosti stránky Termíny.
    """

    page.goto("https://engeto.cz/terminy/")

    assert "terminy" in page.url

@pytest.mark.parametrize(
    "url",
    [
        "https://engeto.cz/",
        "https://engeto.cz/terminy/",
        "https://engeto.cz/testovani-softwaru"
    ]
)
def test_page_are_accessible(page: Page, url):
    """
    TC-003
    Ověření dostupnosti vybraných stránek.
    """

    page.goto(url)

    assert page.url.startswith("https://engeto.cz")


def test_python_academy_visible(page: Page):
    """
    TC-004
    Ověření zobrazení Python Akademie na stránce termínů.
    """
    page.goto("https://engeto.cz/terminy/")

    assert page.get_by_role("link", name="Python Akademie", exact=True).is_visible()


