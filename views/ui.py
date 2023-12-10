from yattag import Doc
import requests


def component(name, elements: list[dict]):
    doc, tag, text = Doc().tagtext()
    with tag('h2'):
        text(name, ' #', len(elements))
    with tag('div'):
        for element in elements:
            with tag('span'):
                for key, value in element.items():
                    try:
                        text(key, ': ', value)
                        doc.stag('br')
                    except Exception:
                        pass
            doc.stag('hr')
        doc.stag('hr')
    return doc.getvalue()


def homepage():
    items = ["laptops", "producers", "market_offers"]
    doc, tag, _ = Doc().tagtext()
    with tag('html'):
        for item in items:
            doc.asis(component(item, requests.get(f"http://127.0.0.1:8000/{item}").json()))

    return doc.getvalue()
