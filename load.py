cities = []
with open('cities.txt', 'r', encoding='utf-8') as f:
    for city in f.readlines():
        cities.append(city.replace('\n', '').lower())