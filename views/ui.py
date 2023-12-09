import requests


def component(name, elements: list[dict]):
    res = f"<h2>{name} #{len(elements)}</h2>"
    res += "<div>"
    for element in elements:
        res += "<span>"
        for key, value in element.items():
            res += f"{key}: {value}<br>"
        res += "</span>"
        res += "<hr>"
    res += "</div>"
    return res


def homepage():
    items = ["laptops", "producers", "market_offers"]
    res = ""
    for item in items:
        res += component(item, requests.get(f"http://127.0.0.1:8000/{item}").json())

    return res
