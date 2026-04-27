Projekt zawiera test procesu akceptacji ciasteczek analitycznych na stronie ing.pl.

1. Instrukcja uruchomienia lokalnego
   
Aby uruchomić testy na swoim komputerze, wykonaj kolejno poniższe komendy w terminalu:

Krok 1: Instalacja niezbędnych bibliotek i przeglądarek

pip install -r requirements.txt

playwright install

Krok 2: Uruchomienie testu w wielu przeglądarkach jednocześnie

Zgodnie z wymaganiami niefunkcjonalnymi, testy należy uruchomić komendą:

pytest test_ing.py --browser chromium --browser firefox

Domyślnie testy uruchamiają się w tle. Aby zaobserwować proces klikania na żywo, należy dodać parametr --headed

2. Opis rozwiązania
   
Technologia: Python + Playwright.

A. Weryfikacja (pkt 5 w zadaniu): 
  Test weryfikuje stan pamięci przeglądarki za pomocą context.cookies(), aby potwierdzić, że po interakcji z banerem przeglądarka zapisała dane sesyjne.
  
B. Powtarzalność: 
  Każdy test uruchamia się w nowym, czystym kontekście przeglądarki (izolacja sesji).

3. Zadanie Bonusowe (CI/CD)
   
Lokalnie, test przechodzi w 100% poprawnie (1 passed). Na fizycznym urządzeniu baner cookies jest widoczny, a automat poprawnie wykonuje wszystkie kroki interakcji.

GitHub Actions: Występuje AssertionError: Locator expected to be visible.

Wnioski: Error wynika z blokady Anti-Bot strony ING. Systemy identyfikują adresy IP serwerów chmurowych GitHub jako ruch maszynowy i w ogóle nie wyskakuje baner cookies. Kod został zoptymalizowany pod kątem imitowania zachowań ludzkich, jednak blokada wydaje się być na poziomie infrastruktury sieciowej.
