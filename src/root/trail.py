
from root.n_gram import generate_n_gram,\
                        remove_punctuation, get_ngrams
from collections import defaultdict
from root.parser_table import parser,ratio_and_distance
import csv


def get_data(csv_name):
    raw_data = list()
    with open(csv_name, "r") as read_file:
        for line in read_file.readlines():
            raw_data.append(line.split(","))

    return raw_data


def get_gram_from_csv(csv_name, result=0):
    n_gram_list_u = list()
    n_gram_list_b = list()
    n_gram_list_t = list()
    raw_data = get_data(csv_name)

    if result == 0:
        result = len(raw_data) - 1
    else:
        result += 1

    for data in raw_data[0:result]:
        if raw_data.index(data) == 0:
            continue
        [data_u, data_b, data_t] = generate_n_gram(
            data[5].split("--")[0], data[3]
        )
        n_gram_list_u.append(data_u)
        n_gram_list_b.append(data_b)
        n_gram_list_t.append(data_t)

    return [n_gram_list_u, n_gram_list_b, n_gram_list_t]


def get_sorted_dic(ngram_dic):
    default_dict = defaultdict(int)

    for gram in ngram_dic:
        for value in gram:
            default_dict[value] += 1

    default_dict = sorted(
        default_dict.items(), key=lambda x: x[1], reverse=True
    )

    return default_dict


def create_csv(top_gram):
    with open("./tests/temp/data_set.csv", "w") as write_file:
        file_writer = csv.writer(
            write_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        for n_gram in top_gram:
            for data in n_gram:
                file_writer.writerow(data)


def is_in_top(gram_search, top_gram_bin):
    value_in = defaultdict(list)

    for index, value in enumerate(gram_search):
        for grams in value:
            if grams in dict(top_gram_bin):

                value_in[str(index)].append(grams)

    return value_in


def get_location_from_notes(sentence, city):
    sentence = remove_punctuation(sentence)
    words = sentence.split("--")
    
    bigram = get_ngrams(words[0].split(" "),2)
    trigram = get_ngrams(words[0].split(" "),3)

    words = set(sentence.split(" "))
    city_return = city & set(trigram)
   
    if not city_return:
        city_return = city & set(bigram)

        if not city_return:
            city_return = words & city 
            
    return list(city_return)


def get_top_n_grams(csv_name, top=20):
    [uniary, binary, ternary] = get_gram_from_csv(csv_name)
    
    dic_unary = get_sorted_dic(uniary)[0:top]
    dic_binary = get_sorted_dic(binary)[0:top]
    dic_ternary = get_sorted_dic(ternary)[0:top]

    sorted = []

    with open("data.txt", "r") as myfile:
        data_location = "".join([line for line in myfile.readlines()])
    
    city = list(parser(data_location)["State"])
    city = set(city)

    for i in range(0, len(get_sorted_dic(ternary))):
        sorted.append((get_sorted_dic(binary)[i] + get_sorted_dic(ternary)[i]))

    with open("./tests/temp/top.csv", "w") as write_file:
        file_writer = csv.writer(write_file, delimiter=",")
        for data in sorted:
            file_writer.writerow(data)

    top_bin = is_in_top(binary, dic_binary)
    top_ter = is_in_top(ternary, dic_ternary)

    raw_data = get_data(csv_name)
    raw_data.pop(0)
    data_csv = list()
    notes_csv = list()
    tmp = list()

    for i,data_location in enumerate(raw_data[0:]):
        data_csv.append(data_location[5])
        notes_csv.append(get_location_from_notes(data_location[5], city))
        a = top_bin[str(i)] + top_ter[str(i)]
        tmp.append((",".join(a), " ".join(notes_csv[i]), data_csv[i]))
    

    with open("./tests/temp/patter.csv", "w") as write_file:
        file_writer = csv.writer(write_file, delimiter=",")
        for data_location in tmp:
            file_writer.writerow(data_location)

    create_csv([dic_unary, dic_binary, dic_ternary])

    return [dic_unary, dic_binary, dic_ternary]
