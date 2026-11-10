# Projekt 3 – Automatizované testy pomocí Playwright

## Autor

Sandra Vondrová

## Popis projektu

Projekt obsahuje automatizované testy webu [engeto.cz](https://engeto.cz) napsané v Pythonu
pomocí frameworku Playwright a pluginu pytest-playwright.

## Použité technologie

- Python 3
- Pytest
- Playwright
- pytest-playwright

## Testovací scénáře

Všechny testy jsou v souboru `test_engeto.py`.

### TC-001 Přesměrování na stránku Testing Akademie

Původní adresa `/testing-akademie/` přesměruje na `/testovani-softwaru/`.
Test ověřuje stavový kód 200, výslednou adresu a nadpis stránky „Testing Akademie“.

### TC-002 Dostupnost stránky Termíny

Test ověřuje, že se stránka `/terminy/` načte se stavovým kódem 200
a má titulek i nadpis „Termíny kurzů“.

### TC-003 Dostupnost vybraných stránek

Parametrizovaný test, který u každé stránky ověří stavový kód 200 a očekávaný titulek:

- `/` – úvodní stránka
- `/testovani-softwaru/` – Testing Akademie
- `/python-akademie/` – Python Akademie

### TC-004 Otevření detailu termínu

Test na stránce `/terminy/` odmítne cookies, klikne na první vypsaný termín a ověří,
že se otevřela adresa, na kterou karta odkazuje, a že titulek stránky obsahuje název kurzu.
Test nezávisí na konkrétním kurzu, stačí, aby byl na webu vypsaný alespoň jeden termín.

## Instalace

```bash
pip install -r requirements.txt
playwright install chromium
```

## Spuštění testů

```bash
pytest -v
```

Spuštění s viditelným oknem prohlížeče:

```bash
pytest -v --headed
```

## Výsledek

Soubor obsahuje 4 testovací funkce, díky parametrizaci se spustí 6 testů.
Očekávaný výstup: `6 passed`.
