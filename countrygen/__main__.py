import pandas as pd
import json
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Generate country-locale config files.")
    parser.add_argument("--json", action="store_true", help="Generate JSON output")
    parser.add_argument("--ts", "--typescript", dest="ts", action="store_true", help="Generate TypeScript output")
    parser.add_argument("--input", default="countries_example.xlsx", help="Path to the Excel input file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"❌ Input file '{args.input}' not found.")
        return

    language_map = {
        'pl': 'Polish',
        'sw': 'Swedish',
        'eng': 'English',
        'de': 'German'
    }

    date_format_map = {
        'PL': 'DD/MM/YYYY',
        'SE': 'DD/MM/YYYY',
        'GB': 'DD/MM/YYYY',
        'DE': 'DD/MM/YYYY'
    }

    df = pd.read_excel(args.input)

    entries = []
    country_ts_entries = []
    locale_ts_entries = []

    for _, row in df.iterrows():
        country = row['Country']
        locale = row['Locale']
        lang_code, region_code = locale.split('_')

        language = language_map.get(lang_code, lang_code.capitalize())
        date_format = date_format_map.get(region_code, "DD/MM/YYYY")
        ts_locale = f"{lang_code}-{region_code}"

        entries.append({
            "entry": {
                "title": f"{country} - {locale}",
                "country": country,
                "locale": locale,
                "language": language,
                "region": region_code,
                "date_format": date_format
            }
        })

        country_ts_entries.append(f"  {{ code: '{country[:2].upper()}', name: '{country}', locale: '{ts_locale}' }}")
        locale_ts_entries.append(f"  {{ language: '{language}', region: '{region_code}', dateFormat: '{date_format}' }}")

    if args.json or (not args.json and not args.ts):
        with open("country_locale_entries.json", "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2)
        print("✅ Generated: country_locale_entries.json")

    if args.ts or (not args.json and not args.ts):
        ts_content = f"""/**
 * Auto-generated country & locale TypeScript configuration
 * (c) 2025 YourCompanyName. All rights reserved.
 */

export interface ICountryConfig {{
  code: string;
  name: string;
  locale: string;
}}

export interface ILocaleConfig {{
  language: string;
  region: string;
  dateFormat: string;
}}

export const cfgCountrySettings: ICountryConfig[] = [
{',\n'.join(country_ts_entries)}
];

export const cfgLocaleSettings: ILocaleConfig[] = [
{',\n'.join(locale_ts_entries)}
];
"""
        with open("country_locale_config.ts", "w", encoding="utf-8") as f:
            f.write(ts_content)
        print("✅ Generated: country_locale_config.ts")

if __name__ == "__main__":
    main()
