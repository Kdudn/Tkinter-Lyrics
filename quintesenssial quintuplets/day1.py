import tkinter as tk
import pygame
from pygame import mixer

root = tk.Tk()

root.geometry("200x50+1720+1000")
root.resizable(False, False)
root.configure(bg='black')
root.title("")
root.attributes("-topmost", True)
watermark = tk.Label(root, text="kdudn_", font=("Courier New", "32"))
watermark.pack(fill="both", expand=True)

audio = True;

if(audio):
	mixer.init()
	mixer.music.load('day1.mp3')
	mixer.music.play()
	mixer.music.set_pos(51.00)

time = 0

class Window():
	def __init__(self, lyric="", speed=15, x1=0, y1=0, x2=0, y2=0, tween="none", power=4, width=500, height=500, death=1000, bg="white", fg="black", reverse=False, title="", font="Arial", fontsize="32", textformat="center"):
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

		self.label = tk.Label(self.new_win, text=lyric, font=(font, fontsize), anchor=textformat, justify="center")
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

time+=5000
root.after(time, lambda:Window(lyric="약", x1=760, y1=1920, x2=760, y2=500, tween="out", width=100, height=100, death=2900))
time+=580
root.after(time, lambda:Window(lyric="속", x1=860, y1=1920, x2=860, y2=500, tween="out", width=100, height=100, death=2320))
time+=610
root.after(time, lambda:Window(lyric="해", x1=960, y1=1920, x2=960, y2=500, tween="out", width=100, height=100, death=1710))
time+=610
root.after(time, lambda:Window(lyric="줘", x1=1060, y1=1920, x2=1060, y2=500, tween="out", width=100, height=100, death=1100))
time+=1010
root.after(time, lambda:Window(lyric="K\nI\nS\nS", x1=660, y1=540, x2=660, y2=340, tween="out", width=200, height=400, speed=25, fontsize=64, font="Engravers MT", death=5000, bg="#1ebeda", fg="white"))
time+=300
root.after(time, lambda:Window(lyric="K\nI\nS\nS", x1=860, y1=540, x2=860, y2=340, tween="out", width=200, height=400, speed=25, fontsize=64, font="Engravers MT", death=4700, bg="#1edb63", fg="white"))
time+=300
root.after(time, lambda:Window(lyric="K\nI\nS\nS", x1=1060, y1=540, x2=1060, y2=340, tween="out", width=200, height=400, speed=25, fontsize=64, font="Engravers MT", death=4400, bg="#ddfb54", fg="white"))
time+=300
root.after(time, lambda:Window(lyric="단", x1=510, y1=1920, x2=510, y2=500, tween="out", width=100, height=100, death=4100))
time+=300
root.after(time, lambda:Window(lyric="하루도", x1=610, y1=1920, x2=610, y2=500, tween="out", width=300, height=100, death=3800))
time+=600
root.after(time, lambda:Window(lyric="빼먹지", x1=910, y1=1920, x2=910, y2=500, tween="out", width=300, height=100, death=3200))
time+=1500
root.after(time, lambda:Window(lyric="말고", x1=1210, y1=1920, x2=1210, y2=500, tween="out", width=200, height=100, death=1700))
time+=2000
root.after(time, lambda:Window(lyric="L\nO\nV\nE", x1=660, y1=540, x2=660, y2=340, tween="out", width=200, height=400, speed=25, fontsize=64, font="Engravers MT", death=5230, bg="#d668e7", fg="white"))
time+=300
root.after(time, lambda:Window(lyric="L\nO\nV\nE", x1=860, y1=540, x2=860, y2=340, tween="out", width=200, height=400, speed=25, fontsize=64, font="Engravers MT", death=4930, bg="#e74b4b", fg="white"))
time+=300
root.after(time, lambda:Window(lyric="L\nO\nV\nE", x1=1060, y1=540, x2=1060, y2=340, tween="out", width=200, height=400, speed=25, fontsize=64, font="Engravers MT", death=4630, bg="grey"))
time+=300
root.after(time, lambda:Window(lyric="잠들기", x1=560, y1=1920, x2=560, y2=500, tween="out", width=300, height=100, death=4330))
time+=730
root.after(time, lambda:Window(lyric="전", x1=860, y1=1920, x2=860, y2=500, tween="out", width=100, height=100, death=3600))
time+=300
root.after(time, lambda:Window(lyric="꼭", x1=960, y1=1920, x2=960, y2=500, tween="out", width=100, height=100, death=3300))
time+=300
root.after(time, lambda:Window(lyric="속삭여줘", x1=1060, y1=1920, x2=1060, y2=500, tween="out", width=300, height=100, death=3000))
time+=3000
root.after(time, lambda:Window(lyric="네가", x1=660, y1=1920, x2=660, y2=500, tween="out", width=200, height=100, death=2700))
time+=770
root.after(time, lambda:Window(lyric="원한", x1=860, y1=1920, x2=860, y2=500, tween="out", width=200, height=100, death=1930))
time+=650
root.after(time, lambda:Window(lyric="만큼", x1=1060, y1=1920, x2=1060, y2=500, tween="out", width=200, height=100, death=1280))
time+=1280
root.after(time, lambda:Window(lyric="내가", x1=610, y1=1920, x2=610, y2=500, tween="out", width=200, height=100, death=2400))
time+=820
root.after(time, lambda:Window(lyric="기다린", x1=810, y1=1920, x2=810, y2=500, tween="out", width=300, height=100, death=1580))
time+=600
root.after(time, lambda:Window(lyric="만큼", x1=1110, y1=1920, x2=1110, y2=500, tween="out", width=200, height=100, death=980))
time+=980
root.after(time, lambda:Window(lyric="마음", x1=460, y1=1920, x2=460, y2=500, tween="out", width=200, height=100, death=4380))
time+=200
root.after(time, lambda:Window(lyric="다해", x1=660, y1=1920, x2=660, y2=500, tween="out", width=200, height=100, death=4180))
time+=1190
root.after(time, lambda:Window(lyric="안아줘", x1=860, y1=1920, x2=860, y2=500, tween="out", width=300, height=100, death=2990))
time+=990
root.after(time, lambda:Window(lyric="아껴줘", x1=1160, y1=1920, x2=1160, y2=500, tween="out", width=300, height=100, death=2000))

print(time)

root.mainloop()
