import tkinter as tk
import pygame
from pygame import mixer
import random

root = tk.Tk()

root.geometry("200x50+1720+1000")
root.resizable(False, False)
root.configure(bg='black')
root.title("")
watermark = tk.Label(root, text="kdudn_", font=("Courier New", "32"))
watermark.pack(fill="both", expand=True)

audio = False;

if(audio):
	mixer.init()
	mixer.music.load('')
	mixer.music.play()
	mixer.music.set_pos(0.00)

time = 0

class Window():
	def __init__(self, lyric="", speed=25, x1=0, y1=0, x2=0, y2=0, tween="none", power=4, width=500, height=500, death=1000, bg="white", fg="black", reverse=False, title="", font="Arial", fontsize="32", textformat="center"):
		self.new_win = tk.Toplevel(root)

		self.width = width
		self.height = height

		self.bg_color = bg
		self.fg_color = fg

		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

		self.speed = speed
		self.tween = tween

		self.power = power

		self.t = 0.0

		self.new_win.after(death, self.die)

		self.new_win.geometry(f"{width}x{height}+{x1}+{y1}")
		self.new_win.title(title)
		self.new_win.attributes("-topmost", True)
		self.new_win.config(bg=self.bg_color)

		self.label = tk.Label(self.new_win, text=lyric, font=(font, fontsize), anchor=textformat, justify="left")
		self.label.pack(fill="both", expand=True)
		self.label.config(bg=self.bg_color, fg=self.fg_color)

		self.reverse = reverse

		self.move()

	def die(self):
		self.new_win.destroy()

	def flash(self):
		if self.bg_color == "black":
			self.bg_color = "white"
			self.fg_color = "black"
		else:
			self.bg_color = "black"
			self.fg_color = "white"

		self.label.config(bg=self.bg_color, fg=self.fg_color)
		self.new_win.config(bg=self.bg_color)

	def ease(self, t):
		p = self.power

		if self.tween == "none":
			return t

		elif self.tween == "in":
			return t ** p

		elif self.tween == "out":
			return 1 - ((1 - t) ** p)

		elif self.tween == "both":
			if t < 0.5:
				return (2 ** (p - 1)) * (t ** p)
			else:
				return 1 - ((-2 * t + 2) ** p) / 2

		return t

	def move(self):
		if self.reverse:
			self.flash()

		if self.t < 1:
			self.t += self.speed / 1000
			if self.t > 1:
				self.t = 1

			eased = self.ease(self.t)

			x = int(self.x1 + (self.x2 - self.x1) * eased)
			y = int(self.y1 + (self.y2 - self.y1) * eased)

			self.new_win.geometry(
				f"{self.width}x{self.height}+{x}+{y}"
			)

		self.new_win.after(20, self.move)

	def changex(self, x):
		self.x1 = self.x2
		self.y1 = self.y2
		self.x2 = x
		self.t = 0
	def changey(self, y):
		self.x1 = self.x2
		self.y1 = self.y2
		self.y2 = y
		self.t = 0

win1 = Window("Hello World", 25, 1920, 1080, 210, 110, "out", 4, 300, 300, "black", "white", False, "", 'Arial', '32', "center")
time += 1000
root.after(time, lambda:win1.changex(0))

print(time)

root.mainloop()
