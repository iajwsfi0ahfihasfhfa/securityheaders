# SecurityHeaders Scanner

**SecurityHeaders Scanner** to proste narzędzie webowe do sprawdzania obecności kluczowych nagłówków bezpieczeństwa na wybranej stronie WWW.

## Funkcje

- Sprawdza nagłówki:
    - Content-Security-Policy
    - Strict-Transport-Security
    - X-Frame-Options
    - X-Content-Type-Options
    - Referrer-Policy
    - Permissions-Policy
    - X-XSS-Protection
- Intuicyjny interfejs webowy
- Szybka analiza domen publicznych

## Szybki start

1. Klonuj repozytorium:
    ```sh
    git clone https://github.com/iajwsfi0ahfihasfhfa/securityheaders.git
    cd securityheaders-scanner
    ```

2. Zainstaluj zależności:
    ```sh
    pip install -r requirements.txt
    ```

3. Uruchom aplikację:
    ```sh
    python app.py
    ```

4. Otwórz w przeglądarce: [http://localhost:5000](http://localhost:5000)

## Przykład użycia

Wpisz adres np. `https://wikipedia.org` i sprawdź obecność nagłówków bezpieczeństwa.

## Licencja

MIT License
