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
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    bar1 = FigureCanvasTkAgg(fig1, revenueFrame)
    bar1.get_tk_widget().pack()

def getPie(name):
    response_count = 0
    HOST ='173.255.242.108'
    PORT =2113
    # List of valid companies to use in link.send()
    # [adidas, asics, athleta, callaway, canterbury, lululemon athletica, nike, puma, raymond ltd, sondico, under armour]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as link:
        link.connect((HOST, PORT))  # Sets up connection to specified host and port
        # .encode() is used to convert str to byte. Got an error when .encode() was not used
        link.send(name.encode())
        flag = True
        while flag == True:

            response = link.recv(1024)  # Create a buffer of 1024 bytes to hold the response from GET request

            if not response:
                break

            if response_count == 0:
                # Decode to turn bytes back to str
                pie_data = eval(response.decode())

            if response_count == 1:
                pie_labels = eval(response.decode())

            response_count += 1
            if response_count > 1:
                flag = False
    print(name)
    print(type(pie_data))
    print(pie_labels)
    graph(pie_data, pie_labels)

originalText=''
root = Tk()
root.title("Aparel Researcher")

# clicking + then search doesnt reset it back to +
count = 0
abbrvText = ''
originalText = ''
options = ['adidas', 'asics', 'athleta', 'callaway', 'canterbury', 'lululemon athletica', 'nike', 'puma', 'raymond ltd', 'sondico', 'under armour']

    # plt.show()




def myClick(name, href):
    global count
    global abbrvText
    global originalText
    count += 1
    user_input = searchBar.get()
    getPie(user_input)
    url = get_href(user_input, name, href)
    originalText = get_text(url)

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
    # widget.destroy()
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

figure2 = plt.Figure(figsize=(6,5),dpi=100)
ax2 = figure2.add_subplot(111)
bar2 = FigureCanvasTkAgg(figure2, assetFrame)
bar2.get_tk_widget().pack()
data2 = np.random.normal(20000,25000,5000)
ax2.hist(data2)
# plt.show()


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
