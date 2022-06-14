import tkinter as tk
import random as rd
import csv

#この引数は何？
#syntax error 人間語のプログラムをコンピュータさんが分かる形に翻訳できなかったエラー
#メンバ＝クラス内で使う変数。メンバは全てパブリック。
#インスタンスのメンバは(オブジェクト).(変数名)で参照できる
class Application(tk.Frame):
      #__init__メソッド。コンストラクタ。インスタンスの初期設定を行う。
      #コンストラクタ = インスタンス化されたときに最初に呼ばれる特別なメソッド
      #selfはそれぞれのインスタンスを表す。
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
        self.SetVar()
        self.widget()

        self.master.bind("<Return>", self.EnterJudge)

    def SetVar(self):
        self.judgeNum = -1
        self.num = rd.randint(0, len(self.wordlist) - 1)

    #__name__とは Pythonのプログラムがどこから呼ばれて実行されている
    # かを格納している変数
    #Python のプログラムがコマンドラインから直接呼ばれた
    #　⇒__name__には__main__という文字列が格納されている。
    #一方、importで他のプログラムから呼ばれた
    #　⇒__name__にはファイル名が格納されている
    # Pythonファイルが[XXX.py]という形で実行されているかどうかを
    #判定するif文。

    def WordInput(self):
        #encoding パラメータとは、
        # テキストファイルのエンコーディング方式を明示→デフォルトエンコーディング以外の形式で符号化されているファイルを読み書きする
        #
        f = open("C:\\ドキュメント\\Documents\\application development\\word.csv","r",encoding = "cp932")

        self.wordlist = list(csv.reader(f))

        f.close()

    def widget(self):

        self.txt1 = tk.Entry(self.master, width = 33)
        self.txt1.place(x = 50, y = 30)

        self.txt1.insert(0, self.wordlist[self.num][0])

        #Tkinter Entryウィジェット＝テキストボックスみたいな。文字の入力を受け取る。
        self.txt2 = tk.Entry(self.master, width = 33)
        self.txt2.place(x = 50, y = 90)

        #判定ボタン
        #command を 答えを表示するメソッドにする。
        self.BtnJudge = tk.Button(self.master, text = "答えを見る", command = self.ClickJudge, width = 10)
        self.BtnJudge.place(x = 110, y = 148)

        self.BtnNext = tk.Button(self.master, text = "次の単語", command = self.Next, width = 10)
        self.BtnNext.place(x = 215, y = 148)

        self.select4()
        

#4択の表示
    def select4(self):

        rdNum = rd.randint(0, 3) #rdはなんの変数？
        lbl_x = 280
        lbl_y = 15

        self.Rdlist()



        for i in range(4):

            if i == 0:
                if i == rdNum:
                    self.lbl1 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.num][1])
                    #place()メソッド：ウィジェットを配置できる。空間的位置は、x, y座標で指定する。 書き方は、tk.ウィジェット.place(オプション)
                    self.lbl1.place(x = lbl_x, y = lbl_y + i * 30)
                else:
                    self.lbl1 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl1.place(x = lbl_x, y = lbl_y + i * 30)


            if i == 1:
                if i == rdNum:
                    self.lbl2 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl2.place(x = lbl_x, y = lbl_y + i * 30)
                else:
                    self.lbl2 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl2.place(x = lbl_x, y = lbl_y + i * 30)

        
            if i == 2:
                if i == rdNum:
                    self.lbl3 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.num][1])
                    self.lbl3.place(x = lbl_x, y = lbl_y + i * 30)
                else:
                    self.lbl3 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl3.place(x = lbl_x, y = lbl_y + i * 30)

            if i == 3:
                if i == rdNum:
                    self.lbl4 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.num][1])
                    self.lbl4.place(x = lbl_x, y = lbl_y + i * 30)
                else:
                    self.lbl4 = tk.Label(self.master, text = str(i+1) + " . " + self.wordlist[self.rdlist[i]][1])
                    self.lbl4.place(x = lbl_x, y = lbl_y + i * 30)


    def Rdlist(self):
        self.rdlist = list(range(len(self.wordlist)))           #?<- self.wordlistは変数? self.　という書き方の規則が分からない
        #shuffle関数　元のリストをランダムに並べ替える
        rd.shuffle(self.rdlist)  
        #remove method = explore and delete the result which is found first. 
        #index method = return the index of a value
        self.rdlist.remove(self.wordlist.index(self.wordlist[self.num]))     #冗長では？self.numで十分では？

    def select4_destroy(self):
        #when you erase UI of an application, destroy()
        self.lbl1.destory()
        self.lbl2.destory()
        self.lbl3.destory()
        self.lbl4.destory()  
      

#判定
#    def Judge(self):
    #getメソッド：辞書型.get(キー)。メリットは、存在しないキーを指定してもエラーしない点。
    #get(引数)ではないのか？
#       if self.txt2.get() == self.wordlist[self.num][1]:
#            self.marupro ()
#        else:
#            self.batsupro()
    def Answer(self):
        

    #次の2つのメソッドはなぜ必要なのかというと、
    # クリックされてもエンターされても処理が進むようにするため
    def ClickJudge(self):
        self.Judge()

    def EnterJudge(self, event):
        self.Judge()


    def marupro(self):
        #deleteメソッド＝リストの要素を指定して削除。
        self.canvas.delete("batsu1")
        self.canvas.delete("batsu2")
        self.judgeNum = 1

        #print("正解")
        self.canvas.create_oval(10, 10, 43, 43, outline = "red", width = 5, tag = "maru")
    
    def batsupro(self):
        #print("不正解")
        self.canvas.create_line(10, 10, 43, 43, fill = "black", width = 5, tag = "batsu1")
        self.canvas.create_line(10, 43, 43, 10, fill = "black", width = 5, tag = "batsu2")
        self.txt2.delete(0, tk.END)   

    def Next(self):

        if self.judgeNum == 1:
            self.canvas.delete("maru")

            self.num = rd.randint(1, len(self.wordlist) - 1)

            self.txt1.delete(0, tk.END)
            self.txt2.delete(0, tk.END)
            self.txt1.insert(0, self.wordlist[self.num][0])

            self.seletet4_destroy()
            self.select4()

            self.judgeNum = -1



def main():
    #Tk()関数　メインとなるウィンドウを作成
    win = tk.Tk()
    app = Application(master = win)
    app.mainloop()    #なぜか()を忘れていた。


#これは何
if __name__ == "__main__":

    main()


#TkinterはPythonでTcl/Tkを扱うためのライブラリ。
#Tcl とは　シンプルな構造をしているスクリプト言語
#Tkとは　　TckでGUIを開発するためのツールキット

#classの定義の際
#メソッドは第一引数にselfを書くルールがある。
#self.a = a　におけるselfとは、自分自身の変数に、という意味。
#引数でもらったaを自分自身のaに、という意味。self.aとaは異なる。