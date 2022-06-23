from n_gram_trail.n_gram import generate_n_gram
from collections import defaultdict


def get_gram_from_csv(csv, n_gram=1, result=0):
    raw_data = list()
    n_gram_list = list()
    with open(csv,'r') as read_file:
        for line in read_file.readlines():
            raw_data.append(line.split(','))
    if result ==0:
        result = len(raw_data)-1
    else:
        result+=1
    for data in raw_data[0:result]:
        if raw_data.index(data) == 0:
            continue
        n_gram_list.append(generate_n_gram(data[5],n_gram))
    
    return n_gram_list

def get_top_n_grams(csv,top=20):
    uniary = get_gram_from_csv("3_govt_urls_state_only.csv",1)
    binary = get_gram_from_csv("3_govt_urls_state_only.csv",2)
    ternary = get_gram_from_csv("3_govt_urls_state_only.csv",3)

    dic_unary = defaultdict(int)
    dic_binary = defaultdict(int)
    dic_ternary = defaultdict(int)

    for gram in uniary:
        for value in gram:
            dic_unary[value] += 1
    
    for gram in binary:
        for value in gram:
            dic_binary[value] += 1

    for gram in ternary:
        for value in gram:
            dic_ternary[value] += 1 


    dic_unary = sorted(dic_unary.items(),key=lambda x:x[1],reverse=True)
    dic_binary = sorted(dic_binary.items(),key=lambda x:x[1],reverse=True)
    dic_ternary = sorted(dic_ternary.items(),key=lambda x:x[1],reverse=True)

    return (
        dic_unary[0:top],
        dic_binary[0:top],
        dic_ternary[0:top]
    )

    