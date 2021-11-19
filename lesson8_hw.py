import requests
import csv


def get_raw_quote(key):
    url = "http://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "key": key,
              "lang": "en"}

    quotes = []
    try:
        while len(quotes) < key:
            r = requests.get(url, params=params)
            quote = r.json()

            if not quote["quoteAuthor"]:
                continue

            if quote["quoteText"] not in [q["quoteText"] for q in quotes]:
                quotes.append(quote)
    except Exception:
        quote = {}
    return sorted(quotes, key=lambda x: x["quoteAuthor"])


my_quotes = get_raw_quote(10)

selected_quotes = [{key: value for key, value in d.items() if key in {"quoteAuthor", "quoteText", "quoteLink"}}
                   for d in my_quotes]
for d in selected_quotes:
    d["Author"] = d.pop("quoteAuthor")
    d["Quote"] = d.pop("quoteText")
    d["URL"] = d.pop("quoteLink")

fieldnames = selected_quotes[0].keys()


def save_to_csv(filename="quotes.csv"):
    with open(filename, "w", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(selected_quotes)


# filename = "quotes.csv"
csv_w_quotes = save_to_csv()
