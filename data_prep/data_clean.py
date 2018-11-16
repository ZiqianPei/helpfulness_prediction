"""
clean original data, main steps includes:
remove non-unicode chars; remove stop words; tokenization;
input file should be in JSON format.
output file will be pure text format
"""
import json
import nltk
import string


def remove_noneng(line):
    # identify = string.maketrans('', '')
    # delEStr = string.punctuation + string.digits
    # clean_line = line.translate(identify,delEStr)
    # clean_line = line.translate(identify, delEStr)
    clean_line = ''
    return clean_line

def remove_stopword():
    pass

def remove_repetition():
    pass

def load_stopword():
    pass

def label_check():
    pass

def clean(filein, fileout, textkey="body"):
    fin = open(filein, encoding='utf-8', mode='r')
    fout = open(fileout, encoding='utf-8', mode='w')
    for data_unit in json.load(fin):
        text = data_unit[textkey]
        # data cleaning
        new_line = text+'\n'
        fout.write(new_line)


if __name__ == "__main__":
    filein_list = ["../data/json/fortnite_review_neg_1105.json",
                   "../data/json/fortnite_review_pos_1105.json"]
    fileout_list = ["../data/raw/fortnite.500.neg.txt",
                    "../data/raw/fortnite.500.pos.txt"]
    for i in range(len(filein_list)):
        clean(filein_list[i], fileout_list[i])
