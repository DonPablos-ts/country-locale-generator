import pandas as pd
import json

language_map = {
    'pl': 'Polish',
    'sw': 'Swedish',
    'eng': 'English'
}

date_format_map = {
    'PL': 'DD/MM/YYYY',
    'SE': 'DD/MM/YYYY',
    'GB': 'DD/MM/YYYY'
}

df = pd.read_excel("countries_example.xlsx")

entries = []

for _, row in df.iterrows():
    country = row['Country']
    locale = row['Locale']
    lang_code, region_code = locale.split('_')

    entries.append({
        "entry": {
            "title": f"{country} - {locale}",
            "country": country,
            "locale": locale,
            "language": language_map.get(lang_code, lang_code.capitalize()),
            "region": region_code,
            "date_format": date_format_map.get(region_code, "DD/MM/YYYY")
        }
    })

with open("country_locale_entries.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2)

print("Generated country_locale_entries.json")
