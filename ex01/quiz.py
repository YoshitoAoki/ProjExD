from random import *
import datetime

def shutudai(qa_lst):
    qa = choice(qa_lst)
    print("問題：" + qa["q"])
    kaitou(qa["a"])
    return qa["a"]

def kaitou (ans_lst):
    st = datetime.datetime.now()
    ans = input("答えるんだ：")
    end = datetime.datetime.now()
    if ans in ans_lst:
        print("正解！")
    else:
        print("出直してこい")

    print("回答時間：",(end-st).seconds,"秒")

if __name__ == "__main__":
    qa_lst = [
        {"q":"サザエの旦那の名前は？","a":["マスオ","ますお"]},
        {"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]},
        {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]}
    ]


    shutudai(qa_lst)