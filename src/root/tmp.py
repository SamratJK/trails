import camelot

def get_csv(path):
    tables = camelot.read_pdf("abc.pdf",pages="48")
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