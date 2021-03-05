from Stopword import loai_bo_stopword, loai_bo_stopword_trong_danhsach
from pyvi import ViTokenizer, ViPosTagger, ViUtils
import sqlite3
import pandas
from  pyvi import ViTokenizer as tach_tu
from sklearn.feature_extraction.text import TfidfVectorizer


def chuan_hoa_data_csv(data):
    # Chuẩn hoá chuỗi: xoá dấu cách dư thừa, chuyển chữ hoa thành chữ thường
    data_chuan_hoa = []
    for row in data:
        comment_chuan_hoa = str(row).lower()  # chuyển chữ hoa thành chữ thường
        comment_chuan_hoa = comment_chuan_hoa.strip()  # xoá dấu cách dư thừa
        comment_chuan_hoa = loai_bo_stopword(comment_chuan_hoa) # loại bỏ stopword
        #comment_chuan_hoa = ViUtils.add_accents(comment_chuan_hoa) # thêm dấu(add_accents) câu không có dấu
        data_chuan_hoa.append(comment_chuan_hoa)
    return data_chuan_hoa

def remove_stopword(data):
    data_removed_stopword = [comment for comment in loai_bo_stopword_trong_danhsach(data)]
    return data_removed_stopword

def tokenize_tfidf(data):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data)
    Y = [tach_tu.tokenize(str(row)) for row in data]

    for comment in Y:
        print(comment)
    print(vectorizer.get_feature_names())
    print(X)


# load data csv
data_load = pandas.read_csv('data.csv')
data_csv =  list(data_load['data_comment'])

if __name__ == '__main__':
    data_chuan_hoa = chuan_hoa_data_csv(data_csv)
    print(data_chuan_hoa)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data_chuan_hoa)
    Y = [tach_tu.tokenize(str(row)) for row in data_chuan_hoa]

    print(vectorizer.get_stop_words())




