import tkinter as Tkinter

class Gui_Handler:
    def __init__(self,connector_):
        self.connector = connector_
        self.root = Tkinter.Tk()

    def buildGui(self):

        #we build the chattContent
        scroll = Tkinter.Scrollbar(self.root)
        scroll.grid(row = 0, column = 1, sticky=Tkinter.N+Tkinter.S)

        self.chattContents = Tkinter.Text(self.root, yscrollcommand  = scroll.set)
        self.chattContents.grid(row = 0,column = 0)

        scroll.config(command=self.chattContents.yview)

        #we build the Enry
        self.entryOfUser = Tkinter.Entry(self.root)
        self.entryOfUser.grid(row = 1,column = 0)

        #we build the button
        self.buttonToTrigg = Tkinter.Button(self.root, text = "enter", command = self.sendMsgToConnector)
        self.buttonToTrigg.grid(row = 1,column = 1)

    def sendMsgToConnector(self):
        self.connector.sendMsg(self.entryOfUser.get())

    def start(self):
        self.root.mainloop()

    def showMessage(self,text):
        self.chattContents.insert(Tkinter.END,text+"\n")
