import tkinter as tk
import random as rd
import csv
RepeatList = []
DoneList = []

class Application(tk.Frame):

    def __init__(self, master):      #masterという引数？

        #基底クラスのコンストラクタをオーバーライド
        #コンストラクタ=オブジェクトを作るときの特別なメソッド
        super().__init__(master)

        #packメソッド＝ウィジェットを配置する
        self.pack()

        self.master.geometry("380x200")
        self.master.title("英単語ソフト")

        self.canvas = tk.Canvas(self.master, bg = "white", width = 50, height = 50)
        self.canvas.place(x = 30, y = 135)

        self.WordInput()
        #self.SetVar()
        self.widget()

        self.master.bind("<Return>", self.EnterJudge)



    #単語を格納するため
    def WordInput(self):
        #encoding パラメータとは、
        # テキストファイルのエンコーディング方式を明示→デフォルトエンコーディング以外の形式で符号化されているファイルを読み書きする
        #
        f = open("C:\\ドキュメント\\Documents\\application development\\word.csv","r",encoding = "cp932")

        self.wordlist = list(csv.reader(f))

        f.close()

    def widget(self):

        #問題文の表示
        self.txt1 = tk.Entry(self.master, width = 33)
        self.txt1.place(x = 50, y = 30)

        self.txt1.insert(0, self.wordlist[self.num][0])
        #command 引数　ボタン押しの時のイベント処理
        self.tobeMemorized = tk.Button(self.master, text = "to be Reviewed", command = self.addRepeatList, width = 10)
        self.tobeMemorized.place(x = 110, y = 148)

        self.haveMemorized = tk.Button(self.master, text = "Done", command = self.addDoneList, width = 10)
        self.haveMemorized.place(x = 215, y = 148)

#リストをランダムに並べ替える


    #問題文の表示
    def display_answer(self):
        question_text = tk.Frame(text = self.wordlist[self.num][0])
    
    # def classfy(self):
        #覚えたボタンに入力⇒再学習リスト
        #覚えたボタンに入力されたとどう認識？


        #覚えていないボタンに入力⇒学習済みリスト

####ここから作業する！！！
    def addRepeatList(self):
        RepeatList.append(self.wordlist[self.num])

    def addDoneList(self):
        DoneList.append(self.wordlist[self.num])

    
    #if (len(addDoneList) >= 7){
        
    #}

def main():
    win = tk.Tk()
    app = Application(master = win)
    app.mainloop()

if __name__ == "__main__":
    main()


# 宿題
# なぜselfを書くのか？



