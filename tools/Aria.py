import tkinter as tk
from tkinter.font import Font

class AriaIO(tk.Frame):
	"""docstring for AriaIO"""
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)

		self.toolbar = tk.Frame(self, bg="#eee")
		self.toolbar.pack(side="top", fill="x")

		self.bold_btn = tk.Button(self.toolbar, text="Bold", command=self.make_bold)
		self.bold_btn.pack(side="left")

		# self.clear_btn = tk.Button(self.toolbar, text="Clear", command=self.clear)
		# self.clear_btn.pack(side="left")

		self.bold_font = Font(family="Segoe UI", size=14, weight="bold")

		self.text = tk.Text(self, bd=0)
		self.text.insert("end", "Select pdart of text and then click 'Bold'...")
		self.text.focus()
		self.text.pack(fill="both", expand=True)

		self.text.tag_configure("BOLD", font=self.bold_font)
		self.text.tag_configure("STRINGs", foreground="blue")

	def make_bold(self):
		# dampen the errors
		# try:
		self.text.tag_add("STRINGs", "sel.first", "sel.last")        
		# except tk.TclError:
		# 	pass

	def colorize(self,start,end):
		# try:
		self.text.tag_add("STRINGs","1.0")
		# except tk.TclError:
		# 	pass

	def clear(self):
		self.text.tag_remove("BOLD",  "1.0", 'end')
		
	def getFull(self):
		return self.text.get("1.0","end-1c")