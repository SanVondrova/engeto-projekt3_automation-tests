# Projekt 3 - Automatizované testy pomocí Playwright

# Autor

Sandra Vondrová

## Popis projektu

Projekt obsahuje automatizované testy vytvořené pomocí frameworku Playwright a knihovny Pytest.

Testovaná stránka:
https://engeto.cz

## Pužité technologie

- Python 3
- Pytest
- Playwright
- pytest-playwright

## Testovací scénáře
### TC-001 Ověření dostupnosti stránky Testing Akademie

Test ověřuje správné přesměrování stránky Testing Akademie na stránku Testování softwaru.

### TC-002 Ověření dostupnosti stránky termíny

Test kontroluje dostupnost stránky s termíny kurzů.

### TC-003 Ověření dostupnosti vybraných stránek
Parametrizovaný test kontrolující dostupnost více strnek webu Engeto:

### TC-004 Ověření zobrazení odkazu Python Akademie

Test ověřuje viditelnost odkazu Python Akkademie na stránce Termíny.

## Instalace

Instalace potřebných knihoven:

pip install pytest,
pip install playwright,
pip isntall pytest-playwright,
python -m playwright install

## Spouštění testů

pytest -v

## Výsledek
Při poslendím spuštění byly všechny testy úspěšně dokončeny: 6 passed
