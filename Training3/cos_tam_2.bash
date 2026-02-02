#!/bin/bash
# Shebang – mówi systemowi, że skrypt ma być uruchomiony interpreterem bash

while getopts "h" opt; do
# Pętla while: getopts sprawdza argumenty wywołania skryptu
# "h" oznacza, że dozwolona jest flaga -h
# opt to zmienna, w której zapisywana jest aktualnie przetwarzana flaga

  case $opt in
  # case sprawdza, jaka flaga została znaleziona przez getopts

    h)
      # Jeśli flaga to -h
      echo "Help: użyj -h aby zobaczyć pomoc"
      # Wyświetlamy komunikat pomocy
      ;;
      # Kończy obsługę tego przypadku

    *)
      # Obsługa każdej nieznanej / niepoprawnej flagi
      echo "Nieznana flaga"
      # Informacja o błędzie
      exit 1
      # Zakończenie skryptu kodem błędu
      ;;
      # Koniec obsługi niepoprawnej flagi

  esac
  # Koniec instrukcji case

done
# Koniec pętli while – wszystkie flagi zostały przetworzone

echo "Koniec skryptu"
# Kod, który wykona się po przetworzeniu flag
