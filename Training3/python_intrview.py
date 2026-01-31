# =========================
# PYTHON – CORE
# =========================

# List comprehension – szybkie tworzenie list
squares = [x**2 for x in range(5)]
print("list comprehension:", squares)

# Dict comprehension – mapowanie danych
mapping = {x: x**2 for x in range(3)}
print("dict comprehension:", mapping)

# Unpacking args / kwargs – elastyczne funkcje
def demo_args(*args, **kwargs): print("args:", args, "kwargs:", kwargs)
demo_args(1, 2, a=3)

# Multiple return values – często w helperach testowych
def get_user(): return "john", 30
name, age = get_user()
print("multiple return:", name, age)

# Context manager – bezpieczna praca z plikami
with open("file.txt", "w") as f: f.write("test")
print("context manager: file written")

# Exceptions – obsługa błędów w testach
try: 1 / 0
except ZeroDivisionError: print("exception handling: ZeroDivisionError")

# OOP – prosta klasa testowa
class User:
    def __init__(self, name): self.name = name
print("OOP class:", User("Alice").name)

# Import modułów – struktura projektu
import os
print("import module:", os.name)

# =========================
# PYTEST – CORE (SYNTAX)
# =========================

# Test function – podstawowa struktura testu
def test_basic_assert():
    assert 2 + 2 == 4  # assert – walidacja wyniku

# Fixture – setup danych testowych
import pytest
@pytest.fixture
def sample_data():
    return [1, 2, 3]

# Fixture usage – wstrzykiwanie danych
def test_fixture(sample_data):
    assert len(sample_data) == 3

# Parametrize – jeden test, wiele danych
@pytest.mark.parametrize("a,b,expected", [(1,2,3), (2,3,5)])
def test_parametrize(a, b, expected):
    assert a + b == expected

# Test wyjątku – walidacja błędów
def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# Mock – izolacja zależności
from unittest.mock import patch
def get_data(): return "real"
def test_mock():
    with patch("__main__.get_data", return_value="mock"):
        assert get_data() == "mock"

# =========================
# LINUX / OS
# =========================

# Zmienne środowiskowe – konfiguracja testów
os.environ["ENV"] = "test"
print("env var:", os.getenv("ENV"))

# Ścieżki – przenośność testów
from pathlib import Path
print("current dir:", Path.cwd())

# =========================
# REQUESTS – API TESTING
# =========================

import requests
response = requests.Response()
response.status_code = 200
print("API response status:", response.status_code)

# =========================
# BASH / SHELL (KONCEPCJE)
# =========================

# $? – status ostatniej komendy (bash)
print("bash concept: $? -> exit code of last command")

# $1, $@ – argumenty skryptu (bash)
print("bash concept: $1, $@ -> script arguments")

# | > >> – pipe i przekierowania (bash)
print("bash concept: pipe | redirect > >>")

# =========================
# TEST MINDSET
# =========================

# Arrange / Act / Assert – czytelny test
def test_aaa():
    data = [1, 2]        # Arrange
    result = sum(data)  # Act
    assert result == 3  # Assert

print("AAA pattern demonstrated")

# ==========================================================
"""
#!/bin/bash
export ENV=test
export API_URL=https://api.test.local
export TOKEN=abc123

python:
import os
ENV = os.getenv("ENV", "dev")
API_URL = os.getenv("API_URL")

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
"""