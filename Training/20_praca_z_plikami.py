with open('txt_file.txt', 'r') as f:
    zawartosc = f.read()
    print(zawartosc)

with open('./pliczki/txt_file2.txt', 'r') as filet:
    zaw = filet.read()
    print(zaw)

lines = ["Pierwsza linia", "Druga linia", "Trzecia linia"]
print("===================================")
with open('./pliczki/txt_file2.txt', 'w', encoding='utf-8') as plik:
    for item in lines:
        plik.write(item)
        plik.write("\n")


print("===================================")
with open('./pliczki/txt_file2.txt', 'r', encoding='utf-8') as plik2:
    zaw2 = plik2.read()
    print(f"zaw2 = {zaw2}")