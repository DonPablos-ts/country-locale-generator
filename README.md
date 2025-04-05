# Country & Locale Generator

A Python script that reads an Excel file with country and locale data, and outputs:
- A JSON file for use in CMS platforms like Contentstack
- Extensible to output TypeScript config

## Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Place `countries_example.xlsx` in the same folder.

3. Run the script:
   ```
   python generate_from_excel.py
   ```

4. Output: `country_locale_entries.json`
