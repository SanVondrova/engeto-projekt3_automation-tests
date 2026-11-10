import re

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://engeto.cz"


def test_open_testing_academy(page: Page):
    """
    TC-001
    Původní adresa /testing-akademie/ přesměruje na stránku kurzu Testing Akademie.
    """
    response = page.goto(f"{BASE_URL}/testing-akademie/")

    assert response.status == 200
    expect(page).to_have_url(f"{BASE_URL}/testovani-softwaru/")
    expect(page.locator("h1")).to_have_text("Testing Akademie")


def test_terms_page_is_available(page: Page):
    """
    TC-002
    Stránka Termíny se načte a zobrazí správný titulek a nadpis.
    """
    response = page.goto(f"{BASE_URL}/terminy/")

    assert response.status == 200
    expect(page).to_have_title(re.compile("Termíny kurzů"))
    expect(page.locator("h1")).to_have_text("Termíny kurzů")


@pytest.mark.parametrize(
    "path, title_part",
    [
        ("/", "ENGETO"),
        ("/testovani-softwaru/", "Testing Akademie"),
        ("/python-akademie/", "Python Akademie"),
    ],
)
def test_pages_are_accessible(page: Page, path: str, title_part: str):
    """
    TC-003
    Vybrané stránky odpoví stavovým kódem 200 a mají očekávaný titulek.
    """
    response = page.goto(f"{BASE_URL}{path}")

    assert response.status == 200
    expect(page).to_have_title(re.compile(title_part))


def test_first_term_opens_detail(page: Page):
    """
    TC-004
    Kliknutí na první vypsaný termín na stránce Termíny otevře detail stejného kurzu.
    """
    page.goto(f"{BASE_URL}/terminy/")

    # Cookie lišta překrývá celou stránku, proto ji před klikáním odmítneme.
    page.locator("#cookiescript_reject").click()

    # Karta termínu = odkaz v hlavním obsahu, který obsahuje nadpis s názvem kurzu.
    first_term = (
        page.locator("main")
        .get_by_role("link")
        .filter(has=page.get_by_role("heading"))
        .first
    )
    expect(first_term).to_be_visible()

    course_name = first_term.get_by_role("heading").text_content().strip()
    detail_url = first_term.get_attribute("href")

    first_term.click()

    # Otevřela se adresa, na kterou karta odkazuje, a titulek obsahuje název kurzu.
    # re.escape zajistí, že se znaky jako "+" v názvu kurzu berou doslova.
    expect(page).to_have_url(detail_url)
    expect(page).to_have_title(re.compile(re.escape(course_name)))
