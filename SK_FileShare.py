try:	
	import platform as plt
	import easygui as eg
	import time as tk
	import os
	import pyperclip as pp
	try:
	    from tkinter import *
	except:
	    exit()



	uk = b'\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00f\x00i\x00l\x00e\x00.\x00i\x00o\x00'

	ck = b'\xff\xfec\x00u\x00r\x00l\x00 \x00-\x00F\x00'



	plt = plt.system()


	root = Tk()
	root.iconbitmap(default='Sk_FILESHARE.ico')
	root.geometry('250x250')
	root.title("SK_FILESHARE")
	osk = b'\xff\xfeW\x00i\x00n\x00d\x00o\x00w\x00s\x00'
	global button_copy  
	def file_select():
		def click():
			browse = eg.fileopenbox()
			if plt == osk:
				br = str(browse)
				cmd = os.popen(ck.decode('utf-16', 'strict') + ' "file=@"'+br + " "+uk.decode('utf-16', 'strict'))
				link = cmd.read()
				return link[45:73]
			else:
				br = str(browse)
				cmd = os.popen(ck.decode('utf-16', 'strict') + ' "file=@"'+br + " "+uk.decode('utf-16', 'strict'))
				link = cmd.read()
				return link[45:73]
		link = click()
		def copy_exit():
			pp.copy(link)
			button_copy.config(root, text="Copy link & Exit", command=exit())
			button_copy.place(relx=0.5, rely=0.5, anchor=CENTER)

		label_credit = Label(root, text="Credit: file.io & Created by SK")
		label_credit.pack(side="bottom")
		button_direc = Button(root, text="Browse", command=click)
		button_direc.pack(side=TOP, anchor=NE)
		label_direc = Label(root, text="Select File: ")
		label_direc.place(relx=0.0, rely=0.0, anchor=NW)
		button_copy = Button(root, text="Copy link & Exit", command=copy_exit)
		button_copy.place(relx=0.5, rely=0.5, anchor=CENTER)


	file_select()






	
	root.mainloop()
except KeyboardInterrupt:
	try:
		tk.sleep(5)
	except:
		exit()