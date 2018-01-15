from tkinter import ttk
import tkinter as tk

xpad = 3
ypad = 5

class Application(ttk.Frame):

	step_val = 1
	
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.winfo_toplevel().title("IDLE Game")
		self.create_widgets()
		
	def create_widgets(self):
		# Add buttons
		self.startb = ttk.Button(self)
		self.startb["text"] = "Step"
		self.startb["command"] = self.step_prog
		self.startb.grid(column=0, padx=xpad, pady=ypad, row = 0)
		
		self.stopb = ttk.Button(self)
		self.stopb["text"] = str(self.step_val)
		self.stopb["command"] = self.inc_step_val
		self.stopb.grid(column=3, padx=xpad, pady=ypad, row = 0)
		
		self.progbar = ttk.Progressbar(self)
		self.progbar.grid(column=1, padx=xpad, pady=ypad, row = 0)
		
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
		
root = tk.Tk()
app = Application(master=root)
app.mainloop()