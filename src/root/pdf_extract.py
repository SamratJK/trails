import camelot
import pandas as pd


def get_pdf_save_csv(path):
    pdf = camelot.read_pdf(path, pages="all", line_scale=40)
    get_table = []
    get_table_late = []
    for i in range(0, len(pdf) - 1):

        if len(pdf[i].df.columns) == 10:
            get_table.append(pdf[i].df)

        if len(pdf[i].df.columns) == 9:
            get_table_late.append(pdf[i].df)

    result = pd.concat(get_table)
    remove_head = result.values.tolist()
    remove_head.pop(0)
    result = pd.DataFrame(remove_head)
    result.columns = [
        "Id",
        "State",
        "District",
        "Diseases",
        "Cases",
        "Deaths",
        "Date Of Outbreak",
        "Date Of Reporting",
        "Status",
        "Action Taken",
    ]

    if get_table_late:
        result_late = pd.concat(get_table_late)
        remove_head_late = result_late.values.tolist()
        remove_head_late.pop(0)
        remove_head_late.pop(0)
        result_late = pd.DataFrame(remove_head_late)
        result_late.columns = [
            "Id",
            "State",
            "District",
            "Diseases",
            "Cases",
            "Deaths",
            "Date Of Outbreak",
            "Status",
            "Action Taken",
        ]
        combine_table = pd.concat(
            [
                pd.merge(result, result_late, how="left"),
                pd.merge(result, result_late, how="right"),
            ],
            axis=0,
        ).drop_duplicates()
    else:
        combine_table = result

    combine_table.to_csv(path + ".csv")
