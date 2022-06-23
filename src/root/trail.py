
from n_gram_trail.n_gram import generate_n_gram
from collections import defaultdict
import csv

def get_data(csv_name):
    raw_data = list()
    with open(csv_name,'r') as read_file:
        for line in read_file.readlines():
            raw_data.append(line.split(','))
    return raw_data    

def get_gram_from_csv(csv_name, result=0):
   
    n_gram_list_u = list()
    n_gram_list_b = list()
    n_gram_list_t = list()
    raw_data = get_data(csv_name)
    if result == 0:
        result = len(raw_data)-1
    else:
        result+=1
    for data in raw_data[0:result]:
        if raw_data.index(data) == 0:
            continue
        print(len(generate_n_gram(data[5])))
        # n_gram_list_u.append(generate_n_gram(data[5])[0])
        # n_gram_list_b.append(generate_n_gram(data[5])[1])
        # n_gram_list_t.append(generate_n_gram(data[5])[2])
    
    #   (a,b,c) = generate_n_gram(data[5])

    #     n_gram_list_u.append(a)
    #     n_gram_list_b.append(b)
    #     n_gram_list_t.append(c)
        
    print("this \n::::::::::::::::::",n_gram_list_u)
    print("this \n::::::::::::::::::",n_gram_list_b)
    print("this \n::::::::::::::::::",n_gram_list_t)
    # return n_gram_list_u,n_gram_list_b,n_gram_list_t

def get_top_n_grams(csv_name,top=20):
    get_gram_from_csv(csv_name)
    pass 
    # print(get_gram_from_csv(csv_name))
    # binary = get_gram_from_csv(csv_name,2)
    # ternary = get_gram_from_csv(csv_name,3)

    
    # dic_unary = defaultdict(int)
    # dic_binary = defaultdict(int)
    # dic_ternary = defaultdict(int)

    # for gram in uniary:
    #     for value in gram:
    #         dic_unary[value] += 1
    
    # for gram in binary:
    #     for value in gram:
    #         dic_binary[value] += 1

    # for gram in ternary:
    #     for value in gram:
    #         dic_ternary[value] += 1 

    # csv_columns = ["ngrams","frequency"]
    # dic_unary = sorted(dic_unary.items(),key=lambda x:x[1],reverse=True)[0:top]
    # dic_binary = sorted(dic_binary.items(),key=lambda x:x[1],reverse=True)[0:top]
    # dic_ternary = sorted(dic_ternary.items(),key=lambda x:x[1],reverse=True)[0:top]

    # with open("unary.csv","w") as writefile:
    #     write_csv = csv.DictWriter(writefile,fieldnames=csv_columns)
    #     write_csv.writerow(dic_unary)



    # return (
    #     dic_unary,
    #     dic_binary,
    #     dic_ternary
    # )

