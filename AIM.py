from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pygame import mixer
import os
import sys

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

	ttk.Label(tab2, text="Written and Programmed by:\nNicholas Messina\nNicholas Mirigliani\n\n",
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
			"Good day. I am pleased to engage in discourse regarding the origins of AOL Instant Messenger (AIM).",
			"Indeed, the genesis of AIM traces back to the early 1990s when AOL, or America Online, sought to capitalize on the burgeoning popularity of the internet. Recognizing the need for real-time communication, they introduced AIM in 1997, providing users with instant messaging capabilities.",
			"In its nascent stages, AIM revolutionized online communication, offering users the ability to exchange messages instantaneously with friends and family, irrespective of geographical constraints. Its user-friendly interface and innovative features quickly garnered widespread adoption.",
			"Precisely. AIM boasted an array of chatrooms catering to diverse interests, fostering communities centered around topics ranging from music to sports. These chatrooms facilitated interactions among users worldwide, epitomizing the democratization of digital communication.",
			"Over the years, AIM underwent several iterations, introducing enhanced features such as file sharing, voice and video chat, and customizable profiles. However, with the advent of social media platforms and the proliferation of smartphones, AIM gradually declined in relevance, ultimately ceasing operations in 2017.",
			"You're most welcome. Farewell, and may your reminiscences of AIM bring you solace."
		]

		messages = [
			"Hey! :D OMG, AIM was like, so iconic, right? Tell me how it all started!",
			"Woah, that's ancient! :P What was it like in the beginning?",
			"Sounds lit! XD Did it have those iconic chatrooms from the start?",
			"That's so cool! :0 How did it evolve over time?",
			" Aww, RIP AIM! :'( It was such a vibe. Thanks for the history lesson, though! Gonna go cry about the good ol' days now. TTYL!"
		]
	elif item_name == "Technician":
		responses = [
			"Greetings. I'm here to discuss the technical intricacies of AOL Instant Messenger (AIM) and its features.",
			"Certainly. AIM was renowned for its diverse array of features, foremost among them being instant messaging, enabling users to exchange text-based messages in real-time with individuals on their contact list.",
			"In addition to basic messaging, AIM boasted features such as chatrooms, where users could engage in group discussions centered around specific topics of interest. Furthermore, it facilitated file sharing, enabling users to exchange documents, images, and multimedia files effortlessly.",
			"Indeed, AIM was at the forefront of innovation in its time. It introduced voice and video chat capabilities, allowing users to communicate using audio and video streams, thereby enhancing the richness of their interactions.",
			"Certainly. AIM offered customizable user profiles, allowing individuals to personalize their presence on the platform with avatars, status messages, and profile information. Additionally, it incorporated buddy lists and status indicators, enabling users to monitor the online presence of their contacts and initiate conversations accordingly.",
			"You're welcome. Should you have any further inquiries regarding AIM or other technical matters, do not hesitate to reach out."
		]
		messages = [
			"Hey there! AIM was like, my jam back in the day :P. Tell me all about its features!",
			"Oh yeah, I remember that! It was so convenient. XD What else did it offer?",
			"That's rad! I used to hang out in those chatrooms all the time. Did it have anything else?",
			"Wow, that's advanced stuff! :D AIM was way ahead of its time. Any other cool features?",
			"Awesome! :0 I miss those features. AIM was the bomb. Thanks for the info, dude!"
		]
	elif item_name == "Anthropologist":
		responses = [
			"I am prepared to delve into the cultural impact of AOL Instant Messenger (AIM), with a particular focus on its distinctive feature: away messages.",
			"Certainly. Away messages on AIM served as a unique form of self-expression and communication. Users utilized them to convey their current status, mood, or activities to their contacts when they were not actively engaged in conversations.",
			"Away messages became a canvas for creativity and wit, allowing individuals to showcase their personality, sense of humor, or current interests through cleverly crafted messages, song lyrics, quotes, or anecdotes. They fostered a sense of community and connection among users, providing glimpses into each other's lives and facilitating conversations.",
			"Indeed, away messages also played a role in social dynamics and communication etiquette. They signaled to others whether a user was available for conversation or not, thereby influencing the timing and nature of interactions. Additionally, they often sparked curiosity or conversation when they were particularly intriguing or cryptic.",
			"Away messages encapsulated the spirit of the early internet era, characterized by a blend of informality, creativity, and spontaneity. They became emblematic of online culture during that time, leaving an indelible mark on the digital landscape and influencing subsequent forms of online expression.",
			"You're welcome. Should you have any further inquiries about AIM or other cultural phenomena, feel free to ask."
		]
		messages = [
			"Hey! AIM was like, my childhood! XP I loved setting away messages. Tell me how they shaped our culture!",
			"Yeah, I remember. It was like a mini-blog before blogs were a thing! How did they influence our culture? :0",
			"Totally! I loved reading my friends' away messages. X) It was like a window into their souls. :0 Did they have any deeper significance?",
			"Ah, that makes sense! :) Away messages were like our status updates before social media took over. Anything else noteworthy about them?",
			"Wow, I never realized how deep they were! Thanks for enlightening me ttyl!"
		]
	elif item_name == "joe1":
		responses = [
			"hey! party tonite gonna be so fun!",
			"fo sho! miss hanging wit everyone. gonna be awesome.",
			"pick ur outfit yet?",
			"same lol, gotta find somethin' fresh",
			"true! what time u heading out?",
			"sounds good, im down. let's make it a night to remember!"
		]
		messages = [
			"yo!! so excited! haven't seen u in a bit",
			"yeah, been ages. gonna be gr8!",
			"nah, still deciding lol",
			"haha we're so on our game.",
			"thinkin' 'bout 9, u?"
		]
	elif item_name == "cyberninja82":
		responses = [
			"Hey there! How's it going?",
			"Good, thanks! What's up with you?",
			"Not much, just wanted to see if you're free tonight.",
			"Yeah, I'm free. What's going on?",
			"Thinking of having a movie night. You in?",
			"Definitely! It's been ages since we've had one.",
			"I know, right? Any movie preferences?",
			"Hmm, maybe a comedy or action flick?",
			"Sounds good to me. What time should we start?",
			"Works for me. Can't wait!",
			"Same here! It's gonna be a blast."
		]
		messages = [
			"Hey! I'm doing well, thanks for asking. How about you?",
			"Doing great, thanks! Just relaxing at home.",
			"Nice! Got any plans for tonight?",
			"Not really, just chilling. What's up?",
			"Thinking of hosting a movie night. Interested?",
			"Absolutely! Movie nights are always fun.",
			"Totally agree! Any movie preferences?",
			"I'm up for anything, but maybe a comedy?",
			"How about starting around 7?",
			"Sounds perfect! Looking forward to it.",
		]
	else:
		responses = [
			"Hey! How's your day?",
			"Pretty good! Yours?",
			"Busy with work, as usual.",
			"Tell me about it. Any plans tonight?",
			"Just chilling at home. You?",
			"Thinking of hitting the café downtown.",
			"Mind if I join?",
			"Of course not! Let's meet at 7?",
			"Sounds good. See you then!"
		]
		messages = [
			"Hey there! It's been pretty good, thanks. What about you?",
			"Hey! It's been alright, just been busy.",
			"I understand. Work can be draining sometimes.",
			"Yeah, it can. I'm just glad it's almost over.",
			"Same here. Gonna relax at home tonight.",
			"That sounds nice. I might check out that new café.",
			"Mind if I tag along?",
			"Not at all! The more the merrier.",
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
				if msg_counts[name]["n_res"] <= len(responses):
					inputText.insert('end', "Please begin typing...", "Prompt")
				else:
					inputText.insert('end', "END OF CONVERSATION.", "Prompt")

				text.insert('end', "You","You")
				text.insert('end',": " + messages[msg_counts[name]["n_msg"]] + "\n")
				text.insert('end', name, "Other")
				text.insert('end', ": " + responses[msg_counts[name]["n_res"]] + "\n")
				text.yview_moveto(1.0)
				text.configure(state='disabled')

				msg_counts[name]["i_msg"] = 0
				msg_counts[name]["n_msg"] += 1

				mixer.init()
				sound_path = os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")), "sounds", "msg.mp3")
				sound = mixer.Sound(sound_path)
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
