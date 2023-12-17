from random import choice, randint, uniform
from datetime import datetime, timedelta
import string
import json
import requests


def generate_random_date(start_date, end_date):
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    random_days = randint(0, (end_datetime - start_datetime).days)
    random_date = start_datetime + timedelta(days=random_days)

    return random_date.strftime("%Y-%m-%d")


def generate_random_string(size: int):
    characters = string.ascii_lowercase + string.digits
    return "".join(choice(characters) for _ in range(size))


cpus = [
    "Core i9-9900K",
    "Ryzen 7 3700X",
    "Core i5-10400",
    "Ryzen 5 3600",
    "Core i7-10700K",
    "Ryzen 9 5950X",
    "Core i9-11900K",
    "Ryzen 7 5800X",
    "Core i5-11600K",
    "Ryzen 5 5600X",
    "Core i7-12700K",
    "Ryzen 9 6900K",
    "Core i9-10900K",
    "Ryzen 7 4700G",
    "Core i5-12600K",
    "Ryzen 5 4600G",
    "Core i7-11700K",
    "Ryzen 9 5900X",
    "Core i9-12900K",
    "Ryzen 7 4800H",
    "Core i5-12400",
    "Ryzen 5 5500U",
    "Core i7-10850H",
    "Ryzen 9 6950X",
    "Core i9-11980HK",
    "Ryzen 7 5700G",
    "Core i5-11400F",
    "Ryzen 5 3400G",
]

gpus = [
    "NVIDIA GeForce RTX 3080",
    "AMD Radeon RX 6800 XT",
    "NVIDIA GeForce GTX 1660 Ti",
    "AMD Radeon RX 5700 XT",
    "NVIDIA GeForce RTX 3060",
    "AMD Radeon RX 6900 XT",
    "NVIDIA GeForce RTX 3090",
    "AMD Radeon RX 6700 XT",
    "NVIDIA GeForce GTX 1650 Super",
    "AMD Radeon RX 5600 XT",
    "NVIDIA GeForce RTX 3070",
    "AMD Radeon RX 6600 XT",
    "NVIDIA GeForce GTX 1660 Super",
    "AMD Radeon RX 5500 XT",
    "NVIDIA GeForce RTX 2080 Ti",
    "AMD Radeon RX 6700",
    "NVIDIA GeForce GTX 1050 Ti",
    "AMD Radeon RX 580",
    "NVIDIA GeForce GTX 1070",
    "AMD Radeon RX 560",
    "NVIDIA GeForce RTX 2080 Super",
    "AMD Radeon RX 480",
    "NVIDIA GeForce GTX 1060",
    "AMD Radeon RX 460",
    "NVIDIA GeForce RTX 2060",
    "AMD Radeon RX 550",
    "NVIDIA GeForce GTX 1660",
    "AMD Radeon RX 570",
    "NVIDIA GeForce GTX 970",
    "AMD Radeon RX 5300",
]
companies = [
    "Dell",
    "HP",
    "Lenovo",
    "Asus",
    "Acer",
    "MSI",
    "Samsung",
    "Toshiba",
    "Sony",
    "LG",
    "Microsoft",
    "Fujitsu",
    "Gateway",
    "Razer",
    "Panasonic",
    "Huawei",
    "Xiaomi",
]

names = [
    "Gor",
    "Sargis",
    "Narek",
    "Aram",
    "Hayk",
    "Vahe",
    "Arman",
    "Suren",
    "Garo",
    "Ruben",
    "Arsen",
    "Gevork",
    "Gevorg",
    "Ara",
    "Araik",
    "Hakob",
    "Norayr",
    "Sevak",
    "Areg",
    "Taron",
    "Zareh",
    "Vigen",
    "Hovhannes",
    "Artur",
    "Gagik",
    "Ashot",
    "Levon",
    "Mher",
    "Karen",
    "Alik",
    "Vardan",
    "Garnik",
]

countries_with_cities = {
    "United States": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"],
    "United Kingdom": ["London", "Manchester", "Birmingham", "Glasgow", "Liverpool"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"],
    "India": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"],
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
    "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary", "Edmonton"],
    "Brazil": ["Sao Paulo", "Rio de Janeiro", "Brasilia", "Salvador", "Fortaleza"],
    "China": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu"],
    "Japan": ["Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya"],
    "South Africa": ["Johannesburg", "Cape Town", "Durban", "Pretoria", "Bloemfontein"],
    "Mexico": ["Mexico City", "Guadalajara", "Monterrey", "Puebla", "Tijuana"],
    "Italy": ["Rome", "Milan", "Naples", "Turin", "Florence"],
    "Spain": ["Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza"],
    "Russia": [
        "Moscow",
        "Saint Petersburg",
        "Novosibirsk",
        "Yekaterinburg",
        "Nizhny Novgorod",
    ],
}

for _ in range(1000):
    data = {}
    data["model"] = choice(companies) + "-" + generate_random_string(10)
    data["cpu"] = choice(cpus)
    data["gpu"] = choice(gpus)
    data["screen_size"] = uniform(1000, 2000)
    data["memory"] = randint(2048, 8000)

    requests.post(f"http://127.0.0.1:8000/laptops", data=json.dumps(data))

for _ in range(1000):
    data = {}
    data["name"] = choice(names) + " " + choice(names) + "yan"
    data["guarantee"] = randint(1, 5)
    data["country"], cities = choice(list(countries_with_cities.items()))
    data["place"] = choice(cities)

    requests.post(f"http://127.0.0.1:8000/producers", data=json.dumps(data))


for _ in range(10000):
    data = {}
    data["volume"] = randint(1, 1000)
    data["date"] = generate_random_date("1995-01-01", "2023-05-05")
    data["cost"] = randint(1000, 2000)
    data["laptop_id"] = randint(1, 1000)
    data["producer_id"] = randint(1, 1000)

    requests.post(f"http://127.0.0.1:8000/market_offers", data=json.dumps(data))
