# Import module
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pygame import mixer
import time

global open_windows
global msg_counts
def startup():
	STARTUP_WIDTH = 275
	STARTUP_HEIGHT = 300
	IMAGE_WIDTH = 250
	IMAGE_HEIGHT = 200
	STARTUP_FONT = ("TkDefaultFont", 12)

	splash_root = Tk()
	ttk.Style().theme_use("classic")
	splash_root.geometry("{}x{}".format(STARTUP_WIDTH,STARTUP_HEIGHT))
	splash_root.title("AIM: Sign On")

	mainframe = ttk.Frame(splash_root, padding = "10 10 10 10")
	mainframe.grid(column=0, row=0, sticky='nwes')
	splash_root.columnconfigure(0, weight=1)
	splash_root.rowconfigure(0, weight=1)

	splash_image = Image.open("images/splash.png").resize((IMAGE_WIDTH, IMAGE_HEIGHT))
	splash_image_tk = ImageTk.PhotoImage(splash_image)
	ttk.Label(mainframe, image=splash_image_tk).grid(column=0, row=0)

	separator = ttk.Separator(mainframe, orient='horizontal')
	separator.grid(column=0, row=1, pady=10, sticky='ew')

	load_text = StringVar()
	load_text.set("Logging in")
	load_label = ttk.Label(mainframe,textvariable=load_text, font=STARTUP_FONT)
	load_label.grid(column=0,row=2)

	splash_root.resizable(False, False)
	splash_root.after(5000, lambda: end_startup(splash_root,load_text))
	splash_root.after(300, lambda: load(splash_root, load_text))
	ttk.Button(mainframe, text="Cancel", command=lambda: splash_root.destroy()).grid(column=0, row=3)
	open_windows["startup"] = True

	splash_root.mainloop()
def load(splash_root, load_text):
	if("Logging in" in load_text.get()):
		if "....." in load_text.get():
			load_text.set("Logging in")
		else:
			load_text.set(load_text.get()+".")
		splash_root.after(300, lambda: load(splash_root, load_text))
def end_startup(splash_root, load_text):
	load_text.set("Login success!")
	splash_root.after(2000, lambda: destroy_startup(splash_root))
def destroy_startup(splash_root):
	splash_root.destroy()
	open_windows["startup"] = False
	buddylist()

def buddylist():
	bd = Tk()
	ttk.Style().theme_use("classic")
	BUDDY_WIDTH = 275
	BUDDY_HEIGHT = 575
	IMAGE_WIDTH = 250
	IMAGE_HEIGHT = 200
	# BUDDY_FONT = ("TkDefaultFont", 12)

	bd.geometry("{}x{}".format(BUDDY_WIDTH, BUDDY_HEIGHT))
	bd.title("AIM: Buddy List")
	mainframe = ttk.Frame(bd, padding="10 10 10 10")
	mainframe.grid(column=0, row=0, sticky='nwes')
	bd.columnconfigure(0, weight=1)
	bd.rowconfigure(0, weight=1)

	image = Image.open("images/splash.png").resize((IMAGE_WIDTH, IMAGE_HEIGHT))
	image_tk = ImageTk.PhotoImage(image)
	ttk.Label(mainframe, image=image_tk).grid(column=0, row=0)

	ttk.Label(mainframe,
			  text="Welcome to AOL Instant Messenger. To learn about the history and technology behind AIM, please talk to our experts below!",
			  wraplength=BUDDY_WIDTH-25).grid(column=0, row=1)

	separator = ttk.Separator(mainframe, orient='horizontal')
	separator.grid(column=0, row=2, pady=10, sticky='ew')

	notebook = ttk.Notebook(mainframe)
	tab1 = ttk.Frame(notebook)
	notebook.add(tab1, text="Online")
	tab2 = ttk.Frame(notebook)
	notebook.add(tab2, text="About")

	tree = ttk.Treeview(tab1)
	tree.insert("", "end", iid="experts", text="Experts", values=("Historian", "Technicial", "Anthropologist"))
	tree.insert("experts", "end", iid="hist", text="Historian")
	tree.insert("experts", "end", iid="tech", text="Technician")
	tree.insert("experts", "end", iid="anth", text="Anthropologist")
	tree.insert("", "end", iid="friends", text="Friends", values=("joe1", "cyberninja82", "Susan_abc"))
	tree.insert("friends", "end", iid="joe", text="joe1")
	tree.insert("friends", "end", iid="ninja", text="cyberninja82")
	tree.insert("friends", "end", iid="sus", text="Susan_abc")
	tree.bind("<Double-1>", lambda event: buddy_clicked(event, tree))
	tree.pack(expand=True, fill="both")

	ttk.Label(tab2, text="Written and Programmed by:\nNicholas Messina\nNicholas Mirigliani\n\nSources:\nnone yet lol\n\n\n\n\n\ntest",
			  background="white", borderwidth=2, relief="solid", anchor="center").pack(expand=True, fill="both")
	notebook.grid(column=0,row=3)

	ttk.Button(mainframe, text="Quit", command=lambda: bd.destroy()).grid(column=0,row=4)

	bd.resizable(False, False)

	open_windows["buddy_list"] = True
	bd.mainloop()
def buddy_clicked(event, tree):
	item = tree.selection()[0]
	parent_item = tree.parent(item)
	item_name = tree.item(item, "text")
	if parent_item:
		parent_text = tree.item(parent_item, "text")
		if parent_text == "Experts" or parent_text == "Friends":
			open_chat(item_name)
def open_chat(item_name):
	global msg_counts
	IMAGE_WIDTH = 250
	IMAGE_HEIGHT = 200
	responses = []
	messages = []
	if(item_name == "Historian"):
		responses = [
			"Hello, I am the historian, what would you like to know about? This is going to be a REALLY long message. Sorry about that.",
			"I am still learning, but I know it was awesome.",
			"Of course, see you!"
		]
		messages = [
			"I would love to know about AOL IM.",
			"Thanks, that is really helpful..."
		]
	else:
		responses = [
			"not implemented!",
			"still not implemented"
		]
		messages = [
			"not implemented"
		]
	def update_input(event, name):
		global msg_counts
		if msg_counts[name]["n_msg"] < len(messages):
			inputText.configure(state='normal')
			inputText.delete('1.0', 'end')
			inputText.insert('end', messages[msg_counts[name]["n_msg"]][0:msg_counts[name]["i_msg"]])
			msg_counts[name]["i_msg"] += 1

			# If the current message is done being typed...
			if msg_counts[name]["i_msg"] == len(messages[msg_counts[name]["n_msg"]])+2:
				msg_counts[name]["n_res"] += 1

				text.configure(state='normal')
				inputText.delete('1.0', 'end')
				if msg_counts[name]["n_msg"] > len(messages):
					inputText.insert('end', "Please begin typing...", "Prompt")
				else:
					inputText.insert('end', "END OF CONVERSATION.", "Prompt")

				text.insert('end', "You","You")
				text.insert('end',": " + messages[msg_counts[name]["n_msg"]] + "\n")
				text.insert('end', name, "Other")
				text.insert('end', ": " + responses[msg_counts[name]["n_res"]] + "\n")
				text.configure(state='disabled')

				msg_counts[name]["i_msg"] = 0
				msg_counts[name]["n_msg"] += 1

				mixer.init()
				sound = mixer.Sound("sounds/msg.mp3")
				sound.play()

			inputText.configure(state='disabled')

	if not open_windows[item_name.lower()]:

		mixer.init()
		sound = mixer.Sound("sounds/msg.mp3")
		sound.play()

		msg_counts[item_name]["i_msg"] = 0
		msg_counts[item_name]["n_msg"] = 0
		msg_counts[item_name]["n_res"] = 0
		open_windows[item_name.lower()] = True
		WIN_HEIGHT = 430
		WIN_WIDTH = 780

		chat = Toplevel()
		chat.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))

		ttk.Style().theme_use("classic")
		# chat.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))
		chat.title("AIM: Chat with " + item_name)

		mainframe = ttk.Frame(chat)
		mainframe.grid(column=0, row=0, sticky='nwes')

		leftframe = ttk.Frame(mainframe)
		leftframe.grid(column=0, row=0)

		splash_image = Image.open("images/splash.png").resize((IMAGE_WIDTH, IMAGE_HEIGHT))
		splash_image_tk = ImageTk.PhotoImage(splash_image)
		ttk.Label(leftframe, image=splash_image_tk, width=IMAGE_WIDTH).grid(column=0, row=0, sticky='n', pady=10, padx=10)

		profileFrame = ttk.Frame(leftframe)
		profileFrame.grid(column=0,row=1)

		other_image = Image.open("images/{}.png".format(item_name)).resize((75, 75))
		other_image_tk = ImageTk.PhotoImage(other_image)
		ttk.Label(profileFrame, image=other_image_tk, width=IMAGE_WIDTH).grid(column=0, row=0, sticky='n')
		ttk.Label(profileFrame, text=item_name).grid(column=0, row=1, sticky='n')

		you_image = Image.open("images/you.png").resize((75, 75))
		you_image_tk = ImageTk.PhotoImage(you_image)
		ttk.Label(profileFrame, image=you_image_tk, width=IMAGE_WIDTH).grid(column=0, row=2, sticky='n')
		ttk.Label(profileFrame, text="You").grid(column=0, row=3, sticky='n')

		rightframe = ttk.Frame(mainframe)
		rightframe.grid(column=1, row=0)
		text = Text(rightframe, width=60, height=15, wrap='word')
		text.tag_config("You", foreground="blue")
		text.tag_config("Other", foreground="red")

		text.insert('end', item_name, "Other")
		text.insert('end', ": " + responses[0] + "\n")
		text.configure(state='disabled')
		text.configure(font=("Times", 12))
		text.grid(column=1, row=0, padx=10, pady=10, sticky='nwes')

		inputText = Text(rightframe, state='disabled',width=60, height=5,wrap='word')
		inputText.tag_config("Prompt", foreground="gray")
		inputText.configure(state='normal')

		inputText.insert('end', "Please begin typing...", "Prompt")
		inputText.configure(state='disabled')
		inputText.configure(font=("Times", 12))
		inputText.grid(column=1, row=1, padx=10, pady=10,sticky='nw')

		inputText.bind("<Key>", lambda event: update_input(event, item_name))

		# send_button = Button(mainframe, text="Send")
		# send_button.grid(column=1, row=1)

		chat.resizable(False, False)
		chat.protocol("WM_DELETE_WINDOW", lambda: close_chat(chat, item_name))
		chat.mainloop()

	else:
		print("The window is already open!")

def close_chat(chat, item_name):
	open_windows[item_name.lower()] = False
	chat.destroy()

if __name__ == "__main__":
	open_windows = {"startup": False,
					"buddy_list": False,
					"historian": False,
					"technician": False,
					"anthropologist": False,
					"joe1": False,
	   				"cyberninja82": False,
					"susan_abc": False}
	msg_counts = {"Historian":{"i_msg":0,
							   "n_msg":0,
							   "n_res":0},
				  "Technician": {"i_msg": 0,
								"n_msg": 0,
								"n_res": 0},
				  "Anthropologist": {"i_msg": 0,
								"n_msg": 0,
								"n_res": 0},
				  "joe1": {"i_msg": 0,
								"n_msg": 0,
								"n_res": 0},
				  "cyberninja82": {"i_msg": 0,
								"n_msg": 0,
								"n_res": 0},
				  "Susan_abc": {"i_msg": 0,
								"n_msg": 0,
								"n_res": 0},
				  }
	startup()
