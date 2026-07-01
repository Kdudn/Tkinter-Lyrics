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

audio = True;

if(audio):
	mixer.init()
	mixer.music.load('cuntuesday.mp3')
	mixer.music.play()
	mixer.music.set_pos(37.98)

time = 0

class Window():
	def __init__(self, lyric, speed, x1, y1, x2, y2, tween, power, width, height, death, bg, fg, reverse, title, font, fontsize, textformat):
		self.new_win = tk.Toplevel(root)

		self.width = width
		self.height = height

		self.bg_color = bg
		self.fg_color = fg

		self.current = 0

		self.new_win.after(death, self.die)

		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

		self.speed = speed
		self.tween = tween

		self.power = power

		self.t = 0.0

		self.new_win.geometry(f"{width}x{height}+{x1}+{y1}")
		self.new_win.title(title)
		self.new_win.attributes("-topmost", True)
		self.new_win.config(bg=self.bg_color)

		self.label = tk.Label(self.new_win, text=lyric, font=(font, fontsize), anchor=textformat, justify="left")
		self.label.pack(fill="both", expand=True)
		self.label.config(bg=self.bg_color, fg=self.fg_color)

		self.reverse = reverse

		if self.reverse:
			self.flash()

		self.move()

	def die(self):
		self.new_win.destroy()

	def flash(self):
		if self.fg_color == "white":
			self.fg_color = "black"
		else:
			self.fg_color = "white"

		colors = [
		    "#FF0000",  # Red
		    "#FF7F00",  # Orange
		    "#FFFF00",  # Yellow
		    "#00FF00",  # Green
		    "#00FFFF",  # Cyan
		    "#0000FF",  # Blue
		    "#8B00FF",  # Violet
		]
		self.current = (self.current + 1) % len(colors)
		self.bg_color = colors[self.current]

		self.label.config(bg=self.bg_color, fg=self.fg_color)
		self.new_win.config(bg=self.bg_color)
		self.new_win.after(479, self.flash)

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

root.after(time, lambda:Window(":)", 25, 510, 90, 610, 190, "out", 4, 700, 700, 10000000, "white", "black", True, "", 'Arial', '500', "center"))
time += 1900
root.after(time, lambda:Window("So", 25, 500, 1080, 500, 500, "out", 4, 100, 100, 970, "white", "black", False, "", 'Impact', '32', "w"))
time += 330
root.after(time, lambda:Window("I'll", 25, 550, -100, 600, 500, "out", 4, 100, 100, 640, "white", "black", False, "", 'Impact', '32', "w"))
time += 640
root.after(time, lambda:Window("C", 25, 210, -200, 210, 210, "out", 4, 100, 100, 2500, "white", "black", False, "", 'Impact', '32', "w"))
time+=320
root.after(time, lambda:Window("U", 25, -200, 210, 210, 310, "out", 4, 100, 100, 2180, "white", "black", False, "", 'Impact', '32', "w"))
time+=400
root.after(time, lambda:Window("Next", 25, 2120, 310, 210, 410, "out", 4, 150, 100, 1780, "white", "black", False, "", 'Impact', '32', "w"))
time+=500
root.after(time, lambda:Window("Tuesday", 25, 210, 1100, 210, 510, "out", 4, 200, 100, 1280, "white", "black", False, "", 'Impact', '32', "w"))
time+=1280
root.after(time, lambda:Window("If I ever get desperate", 25, 710, -100, 710, 100, "out", 4, 500, 100, 4000, "white", "black", False, "", 'Impact', '32', "center"))
time+=2000
root.after(time, lambda:Window("Or I'm so beyond faded", 25, 710, 1180, 710, 900, "out", 4, 500, 100, 2000, "white", "black", False, "", 'Impact', '32', "center"))
time+=2060
root.after(time, lambda:Window("Just said", 25, 735, 365, 835, 465, "out", 4, 200, 150, 430, "white", "black", False, "", 'Impact', '32', "center"))
time+=430
root.after(time, lambda:Window("I'll", 25, 210, -100, 210, 110, "out", 4, 100, 100, 3140, "white", "black", False, "", 'Impact', '32', "w"))
time += 640
root.after(time, lambda:Window("C", 25, 210, -200, 210, 210, "out", 4, 100, 100, 2500, "white", "black", False, "", 'Impact', '32', "w"))
time+=320
root.after(time, lambda:Window("U", 25, -200, 210, 210, 310, "out", 4, 100, 100, 2180, "white", "black", False, "", 'Impact', '32', "w"))
time+=400
root.after(time, lambda:Window("Next", 25, 2120, 310, 210, 410, "out", 4, 150, 100, 1780, "white", "black", False, "", 'Impact', '32', "w"))
time+=500
root.after(time, lambda:Window("Tuesday", 25, 210, 1100, 210, 510, "out", 4, 200, 100, 1280, "white", "black", False, "", 'Impact', '32', "w"))
time+=1230
root.after(time, lambda:Window("Kinda nice out this morning", 25, 710, -100, 710, 100, "out", 4, 500, 100, 4180, "white", "black", False, "", 'Impact', '32', "center"))
time+=2180
root.after(time, lambda:Window("I won't sit around waiting", 25, 710, 1180, 710, 900, "out", 4, 500, 100, 2000, "white", "black", False, "", 'Impact', '32', "center"))

print(time)

root.mainloop()
