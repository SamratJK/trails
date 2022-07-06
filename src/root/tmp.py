import camelot
import pandas
import matplotlib.pyplot as plt
import tkinter
def get_csv(path):
    tables = camelot.read_pdf(
        "abc.pdf", 
        pages="48",
        split_text=True,
        strip_text="\n"
    )
    tmp = tables[0].df
    tmp.columns = [
        "S.N",
        "Name",
        "Contact Person",
        "Email Address",
        "Name Of Project",
        "Project Site",
        "Donor Agency",
        "Approved Amount Internal",
        "Approved Amount External",
        "Total",
        "Project Duration",
        "Project Sector"

    ]
    
    
    tmp.to_csv("tmp.csv")
    plt.show(block=True)