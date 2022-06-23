from root.n_gram import generate_n_gram
from root.trail import get_gram_from_csv, get_top_n_grams
from collections import defaultdict


def test_uni_gram():
    data = "this is trail will it work"
    result = generate_n_gram(data, 1)
    test = ["trail", "work"]
    for n_gram in result:
        assert len(n_gram.split()) == 1
    assert result == test


def test_bi_gram(data):
    result = generate_n_gram(data, 2)
    test = [
        "Technopolis plans",
        "plans develop",
        "develop stages",
        "stages area",
        "area less",
        "less 100,000",
        "100,000 square",
        "square meters",
        "meters order",
        "order host",
        "host companies",
        "companies working",
        "working computer",
        "computer technologies",
        "technologies telecommunications",
    ]
    for n_gram in result:
        assert len(n_gram.split()) == 2
    assert result == test


def test_tri_gram(data):
    result = generate_n_gram(data, 3)
    test = [
        "Technopolis plans develop",
        "plans develop stages",
        "develop stages area",
        "stages area less",
        "area less 100,000",
        "less 100,000 square",
        "100,000 square meters",
        "square meters order",
        "meters order host",
        "order host companies",
        "host companies working",
        "companies working computer",
        "working computer technologies",
        "computer technologies telecommunications",
    ]
    for n_gram in result:
        assert len(n_gram.split()) == 3
    assert result == test


def test_get_csv(csv, n_gram=1):
    get_gram_from_csv(csv, n_gram)
    return result


def test_get_top_n_gram(csv, top=10):
    result = get_top_n_grams(csv, top)

    return result


if __name__ == "__main__":
    # data = "Technopolis plans to develop in stages an area of no less than 100,000 square meters in order to host companies working in computer technologies and telecommunications the statement said"
    # test_uni_gram()
    # test_bi_gram(data)
    # test_tri_gram(data)

    # (a,b,c) = test_get_top_n_gram("3_govt_urls_state_only.csv")
    # print(type(a))
    # print(a)

    print(test_get_top_n_gram("3_govt_urls_state_only.csv"))
