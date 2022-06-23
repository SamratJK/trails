
import pandas as pd
def parser(data):
    
    list_data=data.replace('    ','|').split("\n")
    list_data_clean = list()
    for row in list_data:
    
        if "State" in row or "Abbr." in row or "Code" in row or row == "":
            continue
        else:
            list_data_clean.append(row.split('|')[0:3])
            if len(row) > 19:
                list_data_clean.append(row.split('|')[3:])


    df = pd.DataFrame(list_data_clean, columns=["State","Postal-abbr.","Postal Code"])
    df = df.sort_values("Postal Code")
    df.to_csv("output.csv")

if __name__ == "__main__":
    with open ("data.txt", "r") as myfile:
        data = ' '.join([line for line in myfile.readlines()])

    parser(data)