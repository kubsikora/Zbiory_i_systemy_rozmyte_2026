# Zbiory i Systemy Rozmyte - Kurs 2026

Repozytorium zawiera materiały, zadania laboratoryjne oraz projekty realizowane w ramach przedmiotu "Zbiory i systemy rozmyte" w semestrze letnim 2026.

## Opis przedmiotu
Przedmiot wprowadza w podstawy teorii i zastosowań zbiorów rozmytych, ze szczególnym naciskiem na implementacje praktyczne. Zakres tematyczny obejmuje:
* Teorię zbiorów rozmytych i operacje na funkcjach przynależności.
* Budowanie i optymalizację systemów regułowych.
* Praktyczne zastosowania logiki rozmytej w sterowaniu i systemach wspomagania decyzji.

## Struktura projektu
Materiały w repozytorium zostały podzielone według etapów realizacji programu:

| Katalog | Opis zawartości | Status |
|:--- |:--- |:--- |
| /zadania | Rozwiązania list zadań dotyczących teorii i operacji. | W trakcie |
| /systemy-regulowe | Implementacje prostych baz reguł i silników wnioskowania. | Planowane |
| /projekty | Większe aplikacje praktyczne wykorzystujące logikę rozmytą. | Planowane |
| /dokumentacja | Opisy algorytmów i raporty z przeprowadzonych testów. | W trakcie |

## Wykorzystane technologie
Projekty i zadania są realizowane z wykorzystaniem następujących narzędzi:
* Język programowania: Python 3.x
* Biblioteki obliczeniowe: NumPy, SciPy
* Biblioteki dedykowane: scikit-fuzzy
* Środowisko: Jupyter Notebook / VS Code

## Teoria i obliczenia
W ramach zadań analizowane są m.in. operacje na zbiorach rozmytych $A$ i $B$, gdzie funkcja przynależności sumy zbiorów definiowana jest często jako:

$$\mu_{A \cup B}(x) = \max(\mu_A(x), \mu_B(x))$$

Oraz proces defuzyfikacji (np. metoda środka ciężkości):

$$y^* = \frac{\int \mu_C(y) \cdot y \, dy}{\int \mu_C(y) \, dy}$$

## Autor
* Imię i Nazwisko: [Twoje Dane]
* Kierunek: [Twój Kierunek]
* Rok akademicki: 2025/2026 (Semestr letni)
