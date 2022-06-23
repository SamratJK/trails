from n_gram_trail.n_gram import generate_n_gram
def get_gram_from_csv(csv, n_gram=1, result=20):
    raw_data = list()
    n_gram_list = list()
    with open(csv,'r') as read_file:
        for line in read_file.readlines():
            raw_data.append(line.split(','))
        
    for data in raw_data[0:result+1]:
        if raw_data.index(data) == 0:
            continue
        n_gram_list.append(generate_n_gram(data[5],n_gram))
    
    return n_gram_list
