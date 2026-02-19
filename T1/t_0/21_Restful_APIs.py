"""
Definicja REST
REST = Representational State Transfer
Architektura komunikacji między systemami
Oparta na protokole HTTP
Definiuje zasady projektowania sieciowych usług internetowych
Główne zasady REST
Klient-serwer
Bezstanowość
Możliwość cachowania
Zunifikowany interfejs
Warstwowa architektura
Metody HTTP
GET    - Pobieranie danych
POST   - Tworzenie nowych zasobów
PUT    - Całkowita aktualizacja
PATCH  - Częściowa aktualizacja
DELETE - Usuwanie zasobów
Kody statusu HTTP
1xx - Informacyjne
2xx - Sukces (200 OK)
3xx - Przekierowania
4xx - Błędy klienta (404 Not Found)
5xx - Błędy serwera

Charakterystyczne cechy
Bezstanowość (każde żądanie niezależne)
Zasoby identyfikowane przez URI
Reprezentacja danych (JSON, XML)
Operacje oparte na standardowych metodach HTTP

GET    /users     - lista użytkowników
GET    /users/1   - szczegóły użytkownika
POST   /users     - utworzenie użytkownika
PUT    /users/1   - aktualizacja użytkownika
DELETE /users/1   - usunięcie użytkownika
"""

# Przykłady z requests
import requests

# GET - pobieranie danych
response = requests.get('https://api.example.com/users')

# POST - wysyłanie danych
data = {'name': 'John', 'email': 'john@example.com'}
response = requests.post('https://api.example.com/users', json=data)

# PUT - aktualizacja
response = requests.put('https://api.example.com/users/1', json=data)

# DELETE - usuwanie
response = requests.delete('https://api.example.com/users/1')

# Sprawdzanie statusu i treści
response = requests.get('https://api.example.com/users')

# Status odpowiedzi
print(response.status_code)  # 200 - OK, 404 - nie znaleziono

# Dane JSON
users = response.json()
print(users)

# Obsługa błędów
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Błąd HTTP: {err}")