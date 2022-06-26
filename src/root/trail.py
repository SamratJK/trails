from ntpath import join
from os import get_terminal_size
from numpy import binary_repr
from urllib3 import Retry
from root.n_gram import generate_n_gram, remove_punctuation
from collections import defaultdict
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


def is_in_top(gram_search, top_gram_bin, which_file):
    value_in = defaultdict(list)

    for index, value in enumerate(gram_search):
        for grams in value:
            if grams in dict(top_gram_bin):

                value_in[str(index)].append(grams)

    with open("./tests/temp/" + which_file + ".csv", "w") as write_file:
        file_writer = csv.writer(write_file, delimiter=",")
        for key, data in value_in.items():
            file_writer.writerow((key, data))
    return value_in


def get_note_without_city_name(sentence, city):
    sentence = remove_punctuation(sentence)
    words = sentence.split(" ")
    get_city = list()

    if city:
        get_name = city.split(" ")
        name_city = ""
        for name in get_name:

            if name in words:
                name_city += name + " "

        get_city.append(name_city)

    return get_city


def get_top_n_grams(csv_name, top=20):
    [uniary, binary, ternary] = get_gram_from_csv(csv_name)

    dic_unary = get_sorted_dic(uniary)[0:top]
    dic_binary = get_sorted_dic(binary)[0:top]
    dic_ternary = get_sorted_dic(ternary)[0:top]
    sorted = []
    for i in range(0, len(get_sorted_dic(ternary))):
        sorted.append((get_sorted_dic(binary)[i] + get_sorted_dic(ternary)[i]))

    with open("./tests/temp/top.csv", "w") as write_file:
        file_writer = csv.writer(write_file, delimiter=",")
        for data in sorted:
            file_writer.writerow(data)

    top_bin = is_in_top(binary, dic_binary, "grams_in_binary")
    top_ter = is_in_top(ternary, dic_ternary, "grams_in_ternary")

    raw_data = get_data(csv_name)
    data_csv = list()
    notes_csv = list()
    for data in raw_data[0:]:
        if raw_data.index(data) == 0:
            continue
        data_csv.append(data[5])
        notes_csv.append(get_note_without_city_name(data[5], data[3]))
    tmp = []
    for i in range(0, len(data_csv)):
        a = top_bin[str(i)] + top_ter[str(i)]
        tmp.append((",".join(a), " ".join(notes_csv[i]), data_csv[i]))

    with open("./tests/temp/patter.csv", "w") as write_file:
        file_writer = csv.writer(write_file, delimiter=",")
        for data in tmp:
            file_writer.writerow(data)

    create_csv([dic_unary, dic_binary, dic_ternary])

    return [dic_unary, dic_binary, dic_ternary]
