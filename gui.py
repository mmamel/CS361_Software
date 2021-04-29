from tkinter import * # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import tkinter.font as font
from webscrapper import *

originalText=''
root = Tk()
root.title("Aparel Researcher")




def myClick(name, href ):
    user_input = searchBar.get()
    url = get_href(user_input, name, href)
    originalText = get_text(url)

    if len(originalText) < 150:
        textBox.insert(INSERT, originalText)
        textBox.pack()
    else:
        abbrvText=originalText[:150] + "..."
        textBox.insert(INSERT, abbrvText)
        textBox.pack(side=LEFT)
        textBtn = Button(textFrame, text="+", command=lambda: expandTxt(textBox, textBtn, originalText, abbrvText))
        myFont = font.Font(size=15)
        textBtn['font'] = myFont
        textBtn.pack(side=LEFT)

    # myLabel = Label(topFrame, text= searchBar.get())
    # myLabel.grid(row=2)
def expandTxt(widget, btn, originalText, abbrvText):
    widget.destroy()
    btn.destroy()
    textBox = Text(textFrame, height=30)
    textBox.insert(INSERT, originalText)
    textBox.pack(side=LEFT)
    textBtn = Button(textFrame, text="-", command=lambda: shrinkTxt(textBox, textBtn,originalText,abbrvText))
    myFont = font.Font(size=15)
    textBtn['font'] = myFont
    textBtn.pack(side=LEFT)
def shrinkTxt(widget, btn,originalText, abbrvText):
    widget.destroy()
    btn.destroy()
    textBox = Text(textFrame, height=5)
    textBox.insert(INSERT, abbrvText)
    textBox.pack(side=LEFT)
    textBtn = Button(textFrame, text="+", command=lambda: expandTxt(textBox, textBtn,originalText,abbrvText))
    myFont = font.Font(size=15)
    textBtn['font'] = myFont
    textBtn.pack(side=LEFT)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

revenueFrame = LabelFrame(bottomFrame, text="Revenue Breakdown")
revenueFrame.pack(side=LEFT)
revenue = Label(revenueFrame, text="Revenue graph here")
revenue.pack()

assetFrame = LabelFrame(bottomFrame, text="Asset Breakdown")
assetFrame.pack(side=LEFT)
asset = Label(assetFrame, text="Asset graph here")
asset.pack()

myLabel = Label(topFrame, text = "Apparel Researcher")
myLabel.pack()

searchFrame = Frame(topFrame)
searchFrame.pack()

searchBar = Entry(searchFrame, width = 50)
searchBar.pack(side=LEFT)
searchBar.insert(0, "Enter Apparel Company Name")

name, href = get_fitness_brand("https://en.wikipedia.org/wiki/List_of_fitness_wear_brands")
searchBtn = Button(searchFrame, text="Search", command=lambda: myClick(name, href))
searchBtn.pack(side=LEFT)

textFrame = Frame(topFrame)
textFrame.pack()


expand = False
originalText=''
abbrvText=''


textBox = Text(textFrame, height=5)
# if len(originalText) < 150:
#     textBox.insert(INSERT, originalText)
#     textBox.pack()
# else:
#     abbrvText=originalText[:150] + "..."
#     textBox.insert(INSERT, abbrvText)
#     textBox.pack(side=LEFT)
#     textBtn = Button(textFrame, text="+", command=lambda: expandTxt(textBox, textBtn))
#     myFont = font.Font(size=15)
#     textBtn['font'] = myFont
#     textBtn.pack(side=LEFT)


# button_quit = Button(root, text="Exit Program", command=root.quit)
#add web scraper component here







#############################


root.mainloop()
