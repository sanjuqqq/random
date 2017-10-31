from client.gui_handler import Gui_Handler
from client.Connecter import Connecter

connecter = Connecter()
connecter.connect('127.0.0.1',9999)

chattV = Gui_Handler(connecter)
chattV.buildGui()

connecter.startReceiverThread(chattV)
chattV.start()