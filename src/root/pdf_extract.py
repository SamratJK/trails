import camelot
import pandas as pd


def get_pdf_save_csv(path):
    pdf = camelot.read_pdf(path,pages='all', line_scale=40)
    get_table = []
    for i in range(0,len(pdf)-1):
        
        if len(pdf[i].df.columns) == 10:
            get_table.append(pdf[i].df)
            print(pdf[i].df)
        if len(pdf[i].df.columns) == 9:
            pdf[i].to_csv("outbreak_late"+path+".csv")
    result = pd.concat(get_table)
    result.to_csv("outbreak"+path+".csv")


