
### CREATED BY DARYL CECILE > GITHUB: DARCECTECH
## YOU MAY USE AND AMMEND THE CODE AS LONG AS IT IS MADE EXPLICIT IN NEW ITERATIONS
## IF YOU HAVE ANY SUGGESTIONS, PLEASE LET ME KNOW.
## I AM PLANNING TO CHANGE THE LICENSE TO MIT-LICENSE FOR THIS PROJECT ONCE IT IS COMPLETE

import tkinter as tk
from tkinter.font import Font
import keyword
from string import *
import plexer

class BlitzIO(tk.Frame):

	Xplexer = plexer

	tags = {'__string': 'blue',
			'__integer': 'purple',
			'__function': 'skyblue',
			'__function_parameter': 'orange',
			'__variable': 'hotpink',
			'__boolean': 'lime'}

	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.text = tk.Text(self, bd=0)
		self.text.insert("end", "Select part of text and then click 'Bold'...")
		self.text.focus()
		self.text.pack(fill="both", expand=True)

		self.text.tag_configure("STRINGs", foreground="blue")

		self.config_tags()
		self.text.bind('<Key>', self.key_press)

	def parse_tokens(self,strx):
		self.Xplexer.parseIntoTokens(strx)

	def config_tags(self):
		for tag, val in self.tags.items():
			self.text.tag_config(tag, foreground=val)

	def remove_tags(self, start, end):
		for tag in self.tags.keys():
			self.text.tag_remove(tag, start, end)

	def key_press(self, key):
		theTokens = self.Xplexer.tokens
		lineNum = 0
		for line in self.text.get("1.0","end").splitlines():
			lineNum+=1
			self.parse_tokens(line)
			theTokens = self.Xplexer.tokens
			print(line)
			for i in range(0,len(theTokens[3])):
				print(theTokens)
				self.text.tag_add('__'+theTokens[3][i].lower(),str(lineNum)+"."+str(theTokens[1][i]),str(lineNum)+"."+str(theTokens[2][i]))