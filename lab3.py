# replace_simple.py
table = str.maketrans({
    'ф': '_',
    'ц': '.',
    'у': 'І',
    'ю': 'Н',
    'ч': 'О', 
    'в': 'А',
    'а': 'Й', 
    '-': 'П',
    ' ': 'Д',
    'г': 'В',
    'е': 'Р',
    'о': 'Б',
    'и': 'И',
    'п': 'С',
    'н': 'Г',
    'х': ',',
    'ш': 'У',
    'л': 'Т',
    'т': 'Е',
    'б': 'Х',
    ',': 'Л',
    'с': 'Я',
    'м': 'К',
    'щ': 'З',
    'з': 'М',
    'щ': 'З',
    'к': 'Ї',
    'д': 'Ч',
    'і': 'Ж',
    'й': 'Ю',
    'є': 'Ш',
    'ї': 'Ь',
    'ґ': 'Ц',
    'я': '–',
    'ж': 'Щ',
    'р': 'Є',
    #'': '',

})
chastota = dict()
ALPHABET = 'абвгдеєжзийіклмнопрстуфхцчшщьюяґ. ,-'


import sys, pathlib
src = pathlib.Path("V5.txt").read_text(encoding="utf-8")
for char in ALPHABET: 
    chastota[char] = src.count(char)/len(src) 

out = src.translate(table)
pathlib.Path("output.txt").write_text(out, encoding="utf-8")
print("done -> output.txt")
for a in chastota:
    print(a, ":", chastota[a])
