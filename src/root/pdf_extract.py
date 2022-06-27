import camelot
import pandas as pd


def get_pdf_save_csv(path):
    pdf = camelot.read_pdf(path,pages='all', line_scale=40)
    get_table = []
    for i in range(0,len(pdf)-1):
        
        if len(pdf[i].df.columns) == 10:
            get_table.append(pdf[i].df)
            print(pdf[i].df)
           
    result = pd.concat(get_table)
    result.to_csv(path+".csv")


if __name__ == "__main__":
    get_pdf_save_csv('one.pdf')