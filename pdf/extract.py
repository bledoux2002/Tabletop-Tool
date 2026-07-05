import pdfplumber as pp
import pandas as pd


def main():
    
    with pp.open("./files/small_guns.pdf") as pdf:
        table = pdf.pages[0].extract_table()
        df = pd.DataFrame(table[1:], columns=table[0])
        print(df)
    return
    with pp.open("./files/small_guns.pdf") as pdf:
        # 1. Extract raw characters
        chars = pdf.pages[0].chars
        
        # 2. Filter to keep only ASCII or standard Unicode characters 
        # (Using .isprintable() or a regex)
        filtered_chars = [c['text'] for c in chars if c['text'].isprintable()]
        
        # 3. Reconstruct the text
        clean_text = "".join(filtered_chars)
        print(clean_text)

if __name__ == "__main__":
    main()