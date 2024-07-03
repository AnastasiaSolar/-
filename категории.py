import requests
import json
s=requests.get('https://fakestoreapi.com/products/categories')
if s.status_code == 200:
    data = s.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Ошибка: {response.status_code}")
print('Какой категории товары вы желаете посмотреть?')
a=input()
if a=="jewelery":
    d = requests.get('https://fakestoreapi.com/products/category/jewelery')
    if d.status_code == 200:
        data = d.json()
        print(json.dumps(data, indent=4))
    else:
        print(f"Ошибка: {response.status_code}")
elif a=="electronics":
    f = requests.get('https://fakestoreapi.com/products/category/electronics')
    if f.status_code == 200:
        data = f.json()
        print(json.dumps(data, indent=4))
    else:
        print(f"Ошибка: {response.status_code}")
elif a=="men's clothing":
    g = requests.get("https://fakestoreapi.com/products/category/men's clothing")
    if g.status_code == 200:
        data = g.json()
        print(json.dumps(data, indent=4))
    else:
        print(f"Ошибка: {response.status_code}")
elif a=="women's clothing":
    t = requests.get("https://fakestoreapi.com/products/category/women's clothing")
    if t.status_code == 200:
        data = t.json()
        print(json.dumps(data, indent=4))
    else:
        print(f"Ошибка: {response.status_code}")
else:
    print(f"Категория не найдена, введити категорию из представленного выше списка")