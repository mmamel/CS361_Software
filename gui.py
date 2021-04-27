from tkinter import * # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import tkinter.font as font

root = Tk()
root.title("Aparel Researcher")
def myClick():
    myLabel = Label(topFrame, text= searchBar.get())
    myLabel.grid(row=2)
def expandTxt(widget, btn):
    widget.destroy()
    btn.destroy()
    textBox = Text(textFrame, height=30)
    textBox.insert(INSERT, originalText)
    textBox.pack(side=LEFT)
    textBtn = Button(textFrame, text="-", command=lambda: shrinkTxt(textBox, textBtn))
    myFont = font.Font(size=15)
    textBtn['font'] = myFont
    textBtn.pack(side=LEFT)
def shrinkTxt(widget, btn):
    widget.destroy()
    btn.destroy()
    textBox = Text(textFrame, height=5)
    textBox.insert(INSERT, abbrvText)
    textBox.pack(side=LEFT)
    textBtn = Button(textFrame, text="+", command=lambda: expandTxt(textBox, textBtn))
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

searchBtn = Button(searchFrame, text="Search", command=myClick)
searchBtn.pack(side=LEFT)

textFrame = Frame(topFrame)
textFrame.pack()

#add web scraper component here
expand = False
originalText="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
abbrvText=''


textBox = Text(textFrame, height=5)
if len(originalText) < 150:
    textBox.insert(INSERT, originalText)
    textBox.pack()
else:
    abbrvText=originalText[:150] + "..."
    textBox.insert(INSERT, abbrvText)
    textBox.pack(side=LEFT)
    textBtn = Button(textFrame, text="+", command=lambda: expandTxt(textBox, textBtn))
    myFont = font.Font(size=15)
    textBtn['font'] = myFont
    textBtn.pack(side=LEFT)


# button_quit = Button(root, text="Exit Program", command=root.quit)



root.mainloop()
