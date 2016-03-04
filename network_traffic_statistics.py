
import os
import platform
import re
from Tkinter import *

root = Tk()

RX_Bytes = 0
TX_Bytes = 0
def update():
	global RX_Bytes
	global TX_Bytes
	f = os.popen('netstat -e')
	result = f.readlines()
	#print result[4]
	match = re.findall('[0-9]+', result[4])
	#print match

	rx, tx = int(match[0]), int(match[1])
	rx_rate = ((float(rx - RX_Bytes) / 8) / 1024)
	tx_rate = ((float(tx - TX_Bytes) / 8) / 1024)
	RX_Bytes = rx
	TX_Bytes = tx

	label_RX_number['text'] = "%0.3f KBps" % rx_rate
	label_TX_number['text'] = "%0.3f KBps" % tx_rate
	root.after(1000, update)

frame_system = Frame(root)
frame_system.pack()
label_os = Label(frame_system, fg="#EECCDD", bg="#3333AA", text="OS", width="10")
label_os.pack(side=LEFT)
label_osname = Label(frame_system, fg="#EECCDD", bg="#3333AA", text=platform.platform(), width="20")
label_osname.pack()

frame1 = Frame(root)
frame1.pack()
label_RX = Label(frame1, fg="#3333AA", bg="#DDDDDD", text="Received:", width="10")
label_RX.pack(side=LEFT)
label_RX_number = Label(frame1, fg="#3388CC", text="", width="20")
label_RX_number.pack()

frame2 = Frame(root)
frame2.pack()
label_TX = Label(frame2, fg="#3333AA", bg="#DDDDDD", text="Sent:", width="10")
label_TX.pack(side=LEFT)
label_TX_number = Label(frame2, fg="#3388CC", text="", width="20")
label_TX_number.pack()

root.after(1000, update)
root.mainloop()