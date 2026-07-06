import pdfplumber as pp
import pandas as pd
import json


def small_guns():
    with pp.open("./files/small_guns.pdf") as pdf:
        table = pdf.pages[0].extract_table()
        df = pd.DataFrame(table[1:], columns=table[0])
        print(df)
        
def main():
    with pp.open("./files/equipment.pdf") as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table[1:], columns=table[0])
                df = df.replace(r'\n', ' ', regex=True)
                df.columns = df.columns.str.replace(r'\n', ' ', regex=True)
                df.to_csv(f'./files/equipment_{i}.csv', encoding='ascii', errors='replace', index=False)
                # df = df.fillna('')

                print(df)

if __name__ == "__main__":
    main()