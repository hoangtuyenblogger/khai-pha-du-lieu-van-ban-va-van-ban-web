# c1 thêm file stopword vào thư viện stopword của nltk
#from nltk.corpus import stopwords
#cachedStopWords = stopwords.words("stopword_vietnam_ne")


# c2 tạo stopword






stopwords_vietnam = []
with open('stopword_vietnam.txt', 'r',encoding="utf8") as f:
    for line in f:
        stopwords_vietnam.append(line.strip())

def loai_bo_stopword(text):
    text = ' '.join([word for word in text.split() if word not in stopwords_vietnam])
    return text

def loai_bo_stopword_trong_danhsach(danh_sach):
    danh_sach_ko_co_stopword = [loai_bo_stopword(str(i)) for i in danh_sach]
    return danh_sach_ko_co_stopword
if __name__ == "__main__":
    text = "thì ý là tôi thích học python á hjhj :))"
    print(loai_bo_stopword(text))
    ### >>> tôi thích học python