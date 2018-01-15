from tkinter import ttk
import tkinter as tk

xpad = 3
ypad = 5

class Application(ttk.Frame):

	step_val = 1
	
	def __init__(self, master=None):
		super().__init__(master)
		self.root = master
		self.pack()
		self.winfo_toplevel().title("IDLE Game")
		self.create_widgets()
		
	def create_widgets(self):
		# Add buttons
		#self.startb = ttk.Button(self)
		#self.startb["text"] = "Step"
		#self.startb["command"] = self.step_prog
		#self.startb.grid(column=0, padx=xpad, pady=ypad, row = 0)
		#
		#self.stopb = ttk.Button(self)
		#self.stopb["text"] = str(self.step_val)
		#self.stopb["command"] = self.inc_step_val
		#self.stopb.grid(column=3, padx=xpad, pady=ypad, row = 0)
		#
		#self.progbar = ttk.Progressbar(self)
		#self.progbar.grid(column=1, padx=xpad, pady=ypad, row = 0)
		
		# Add items containing buttons and progress bars
		self.item1 = Item(self.root, "No. 1")
		self.item2 = Item(self.root, "No. 2")
		
		# Add label fields
		
	def step_prog(self):
		self.progbar.step(self.step_val)
		
	def stop_prog(self):
		self.progbar.stop()
		
	def inc_step_val(self):
		if(self.step_val == 3):
			self.step_val = 1
		else:
			self.step_val = self.step_val + 1
		self.stopb["text"] = str(self.step_val)
		
class Item(ttk.LabelFrame):
	count = 0
	
	def __init__(self, master, name):	
		ttk.LabelFrame.__init__(self, master)
		self.pack()
		self.step_val = 1
		self.create_widgets(name)
		
	def create_widgets(self, name):
		self.runb = ttk.Button(self)
		self.progbar = ttk.Progressbar(self)
		self.label = ttk.Label(self)
	
		self.runb["text"] = str(name)
		self.runb["command"] = self.on_button
		self.runb.grid(column=0, padx=xpad, pady=ypad, row = Item.count)
		
		self.progbar.grid(column=1, padx=xpad, pady=ypad, row = Item.count)
		print(self.progbar.config())
		
		Item.count = Item.count + 1
		
		
	def on_button(self):
		self.progbar.step(self.step_val)
		
		
root = tk.Tk()
app = Application(master=root)
app.mainloop()