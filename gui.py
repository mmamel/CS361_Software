from tkinter import * # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import tkinter.font as font
from webscrapper import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import socket

def clearFrame():
    for widget in revenueFrame.winfo_children():
        widget.destroy()

def graph(pie_data, pie_labels):
    clearFrame()
    fig1, ax1 = plt.subplots()
    ax1.pie(pie_data, labels=pie_labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    bar1 = FigureCanvasTkAgg(fig1, revenueFrame)
    bar1.get_tk_widget().pack()

def getPie(name):
    responseCount = 0
    HOST ='173.255.242.108'
    PORT =2113
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as link:
        link.connect((HOST, PORT))
        link.send(name.encode())
        flag = True
        while flag == True:

            response = link.recv(1024)

            if not response:
                break

            if responseCount == 0:
                # Decode to turn bytes back to str
                pie_data = eval(response.decode())

            if responseCount == 1:
                pie_labels = eval(response.decode())

            responseCount += 1
            if responseCount > 1:
                flag = False
    print(name)
    print(type(pie_data))
    print(pie_labels)
    graph(pie_data, pie_labels)

originalText=''
root = Tk()
root.title("Aparel Researcher")

count = 0
abbrvText = ''
originalText = ''
options = ['adidas', 'asics', 'athleta', 'callaway', 'canterbury', 'lululemon athletica', 'nike', 'puma', 'raymond ltd', 'sondico', 'under armour']





def myClick(name, href):
    global count
    global abbrvText
    global originalText
    count += 1
    userInput = searchBar.get()
    getPie(userInput)
    url = getHref(userInput, name, href)
    originalText = getText(url)

    if len(originalText) < 150:
        textBox.delete(0,'end')
        textBox.insert(INSERT, originalText)
    else:
        abbrvText=originalText[:150] + "..."
        print(abbrvText)

        if(count > 1):
            textBox.delete('1.0','end')
        textBox.insert(INSERT, abbrvText)



def expandTxt( btn):
    btn.destroy()
    global abbrvText
    global originalText
    textBox.delete('1.0','end')
    textBox.insert(INSERT, originalText)
    textBtn = Button(textFrame, text="-", command=lambda: shrinkTxt(textBtn))
    myFont = font.Font(size=15)
    textBtn['font'] = myFont
    textBtn.pack(side=LEFT)
def shrinkTxt( btn):
    global abbrvText
    global originalText
    btn.destroy()
    textBox.delete('1.0','end')
    textBox.insert(INSERT, abbrvText)
    textBtn = Button(textFrame, text="+", command=lambda: expandTxt(textBtn))
    myFont = font.Font(size=15)
    textBtn['font'] = myFont
    textBtn.pack(side=LEFT)
def callback(*args):
    value = clicked.get()
    searchBar.delete(0,'end')
    searchBar.insert(INSERT, value)

def getStock():
    ticker = stockBar.get()
    price = stockScrape(ticker)
    priceText = "Price of " + ticker + " : " + price
    stock = Label(stockFrame, text=priceText)
    stock.pack()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

revenueFrame = LabelFrame(bottomFrame, text="Revenue Breakdown")
revenueFrame.pack(side=LEFT)
revenue = Label(revenueFrame, text="Revenue graph here")
revenue.pack()

stockFrame = LabelFrame(bottomFrame, text="Stock Price")
stockFrame.pack(side=LEFT)

stockBar = Entry(stockFrame, width = 50)
stockBar.pack(side=LEFT)
stockBar.insert(0, "Enter Stock Ticker")
stockBtn = Button(stockFrame, text="Search", command=lambda: getStock())
stockBtn.pack(side=LEFT)




myLabel = Label(topFrame, text = "Apparel Researcher")
myLabel.pack()

searchFrame = Frame(topFrame)
searchFrame.pack()

searchBar = Entry(searchFrame, width = 50)
searchBar.pack(side=LEFT)
searchBar.insert(0, "Enter Apparel Company Name")




name, href = getFitnessBrand("https://en.wikipedia.org/wiki/List_of_fitness_wear_brands")
searchBtn = Button(searchFrame, text="Search", command=lambda: myClick(name, href))
searchBtn.pack(side=LEFT)

textFrame = Frame(topFrame)
textFrame.pack()

clicked = StringVar()

# initial menu text
clicked.set( "" )

# Create Dropdown menu
drop = OptionMenu( searchFrame , clicked , *options )
drop.pack()
clicked.trace("w", callback)

expand = False
originalText=''
abbrvText=''


textBox = Text(textFrame, height=5)
textBox.pack(side=LEFT)

textBtn = Button(textFrame, text="+", command=lambda: expandTxt( textBtn))
myFont = font.Font(size=15)
textBtn['font'] = myFont
textBtn.pack(side=LEFT)




root.mainloop()
