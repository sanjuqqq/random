import socket
import _thread

class Socket_Handler:
    def __init__(self):
        self.serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSocket.bind(('',9999))
        self.serverSocket.listen()

    def acceptConnection(self):
        self.clientSocket, self.addr = self.serverSocket.accept()

    def sendMsg(self,text):
        self.clientSocket.send(str.encode(text))
#nigga
    def startReceiver(self,chattViewer_):
        self.chattViewer = chattViewer_
        _thread.start_new_thread(self.func_to_receiver,())

    def func_to_receiver(self):
        while True:
            msg = self.clientSocket.recv(1024).decode()
            self.chattViewer.showMessage(msg)
