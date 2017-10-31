from server.socket_handler import Socket_Handler
from server.gui_handler import Gui_Handler

sock_hand = Socket_Handler()
sock_hand.acceptConnection()

gui_hand = Gui_Handler(sock_hand)
gui_hand.buildGui()

sock_hand.startReceiver(gui_hand)
gui_hand.start()