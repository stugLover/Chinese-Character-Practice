import tkinter as tk
import json
import random as rd

words = json.load(open("words.json", "r", encoding = "utf-8"))

def random_word():
    randomWord = rd.choice(list(words.keys()))
    return randomWord

def toneButton(letter, inpt, frame):
    inptStr = inpt.get()
    button = tk.Button(frame, text = letter, command = lambda: {
        inpt.set(inptStr + letter)
    })
    button.pack()

class something:
    def __init__(self, topFrame, aFrame, eFrame, iFrame, oFrame, uFrame):
        self.inputStr = tk.StringVar()
        self.topFrame = topFrame
        self.aFrame = aFrame
        self.eFrame = eFrame
        self.iFrame = iFrame
        self.oFrame = oFrame
        self.uFrame = uFrame
        self.pinyinEng = []
        self.hanzi = ""

        toneButton("ā", self.inputStr, self.aFrame)
        toneButton("á", self.inputStr, self.aFrame)
        toneButton("ǎ", self.inputStr, self.aFrame)
        toneButton("à", self.inputStr, self.aFrame)

        toneButton("ē", self.inputStr, self.eFrame)
        toneButton("é", self.inputStr, self.eFrame)
        toneButton("ě", self.inputStr, self.eFrame)
        toneButton("è", self.inputStr, self.eFrame)

        toneButton("ī", self.inputStr, self.iFrame)
        toneButton("í", self.inputStr, self.iFrame)
        toneButton("ǐ", self.inputStr, self.iFrame)
        toneButton("ì", self.inputStr, self.iFrame)

        toneButton("ō", self.inputStr, self.oFrame)
        toneButton("ó", self.inputStr, self.oFrame)
        toneButton("ǒ", self.inputStr, self.oFrame)
        toneButton("ò", self.inputStr, self.oFrame)

        toneButton("ū", self.inputStr, self.uFrame)
        toneButton("ú", self.inputStr, self.uFrame)
        toneButton("ǔ", self.inputStr, self.uFrame)
        toneButton("ù", self.inputStr, self.uFrame)

    def __clearUp(self):
        for shit in self.topFrame.winfo_children():
            shit.destroy()
        self.funcSomething()

    def funcSomething(self):
        self.inputStr.set("")
        self.hanzi = random_word()
        self.pinyinEng = words[self.hanzi]
        print(self.pinyinEng[0])
        showThisOne = tk.Label(self.topFrame, text = self.hanzi, font = ("Arial", 32))
        showThisOne.pack()
        enterPinyin = tk.Entry(self.topFrame, textvariable = self.inputStr, font = ("Arial", 32))
        enterPinyin.pack()

    def checkAns(self):
        inpt = self.inputStr.get()
        if self.pinyinEng[0].lower() == inpt.lower():
            pinyin = tk.Label(self.topFrame, text = self.pinyinEng[0], font = ("Arial", 32))
            pinyin.pack()
            english = tk.Label(self.topFrame, text = self.pinyinEng[1], font = ("Arial", 32))
            english.pack()
            nextW = tk.Button(self.topFrame, text = "Next", command = lambda: self.__clearUp())
            nextW.pack()
        else:
            self.inputStr.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hanzi Practice Tool")
    root.geometry("600x400")
    root.resizable(False, False)
    root.attributes("-topmost", False)

    root.grid_rowconfigure(0, weight = 0)
    root.grid_rowconfigure(1, weight = 1)
    root.grid_columnconfigure(0, weight = 1)

    someFrame = tk.Frame(root)
    someFrame.grid(row = 0)

    bottomFrame = tk.Frame(root)
    bottomFrame.grid(row = 1)

    aFrame = tk.Frame(bottomFrame)
    aFrame.pack(side = "left")

    eFrame = tk.Frame(bottomFrame)
    eFrame.pack(side = "left")

    iFrame = tk.Frame(bottomFrame)
    iFrame.pack(side = "left")

    oFrame = tk.Frame(bottomFrame)
    oFrame.pack(side = "left")

    uFrame = tk.Frame(bottomFrame)
    uFrame.pack(side = "left")

    something = something(someFrame, aFrame, eFrame, iFrame, oFrame, uFrame)
    something.funcSomething()
    root.bind("<Return>", lambda event: something.checkAns())
    
    root.mainloop()