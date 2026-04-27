Projekt zawiera zautomatyzowany test procesu akceptacji ciasteczek analitycznych na stronie ing.pl.

1. Instrukcja uruchomienia lokalnego

Aby uruchomić testy na swoim komputerze, wykonaj kolejno poniższe komendy w terminalu:

Krok 1: Instalacja niezbędnych bibliotek i przeglądarek
pip install -r requirements.txt
playwright install

Krok 2: Uruchomienie testu w wielu przeglądarkach jednocześnie
Zgodnie z wymaganiami niefunkcjonalnymi, testy należy uruchomić komendą:
pytest --browser chromium --browser firefox

2. Opis rozwiązania
Technologia: Python + Playwright.

Weryfikacja (Punkt 5 zadania): Test nie tylko klika w przyciski, ale sprawdza stan pamięci przeglądarki za pomocą context.cookies(), 
aby potwierdzić fizyczne zapisanie zgody.

Powtarzalność: Każdy test uruchamia się w nowym, czystym kontekście przeglądarki (izolacja sesji).

3. Zadanie Bonusowe (Pipeline CI/CD)
Projekt został wyposażony w automatyzację GitHub Actions. Kod pipeline'a znajduje się w folderze .github/workflows/tests.yml. 
Testy uruchamiają się automatycznie w chmurze (Ubuntu) na przeglądarkach Chromium i Firefox po każdym wypchnięciu zmian do repozytorium.