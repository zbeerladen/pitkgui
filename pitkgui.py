#!/usr/bin/env python
import sys, os, time, socket
from Tkinter import *
from tkFont import Font
from subprocess import *

# Get Your External IP Address
def get_ip():
	ip_msg = "Not connected"
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		s.connect(('<broadcast>', 0))
		ip_msg = s.getsockname()[0]
	except Exception:
		pass
	return ip_msg

# Startx
def startx():
	command = "/usr/bin/startx"
	process = Popen(command.split(), stdout=PIPE)
	output = process.communicate()[0]
	return output

# Restart Raspberry Pi
def restart():
	command = "/usr/bin/sudo /sbin/shutdown -r now"
	process = Popen(command.split(), stdout=PIPE)
	output = process.communicate()[0]
	return output

# Shutdown Raspberry Pi
def shutdown():
	command = "/usr/bin/sudo /sbin/shutdown -h now"
	process = Popen(command.split(), stdout=PIPE)
	output = process.communicate()[0]
	return output

# Get time and date
def get_date():
	d = time.strftime("%a, %d %b %Y  %H:%M:%S", time.localtime())
	return d

def get_temp():
	command = "vcgencmd measure_temp"
	process = Popen(command.split(), stdout=PIPE)
	output = process.communicate()[0]
	temp = output[5:-1]
	return temp

def get_clock():
	command = "vcgencmd measure_clock arm"
	process = Popen(command.split(), stdout=PIPE)
	output = process.communicate()[0]
	clock = output.split("=")
	clock = int(clock[1][:-1]) / 1024 /1024
	clock = str(clock) + "MHz"
	return clock

def get_volts():
	command = "vcgencmd measure_volts"
	process = Popen(command.split(), stdout=PIPE)
	output = process.communicate()[0]
	volts = output[5:-1]
	return volts


class PitkGui:
  def __init__(self, parent):

	#--- main frame
	main_bg = "black"
	main_fg = "white"
	
	#--- labels
	labFont = Font(family="Courier", size=11)
	labFont.configure(weight = "bold")
	
	#--- pulsanti
	butFont = Font(family="Helvetica", size=11)
	butFont.configure(weight = "bold")
	but_width = 10
	but_height = 0
	but_padx = "3m"
	but_pady = "1m"
	but_relief = FLAT
	but_borderwidth = 1
	but_hlcol = "red"
	but_hlbg = "red"
	but_bg = "#8B0000"
	but_fg = "white"
	but_actbg = "red"
	but_actfg = "white"
	
	#--------------------- fine costanti ----------------

	self.myParent = parent
	
	#--------------------- FRAMES -----------------------
	### Il quadro principale si chiama 'myBox1'
	self.myBox1 = Frame(parent, 
		background=main_bg,
	)
	self.myBox1.pack(side = TOP,
	  fill = BOTH,
	  expand = YES,
	)

	# Il quadro dei pulsanti alto
	self.button_square = Frame(self.myBox1,
		background=main_bg,
		#relief=RAISED, borderwidth=1
	)
	self.button_square.pack(side = TOP,
	  padx=5,
	  pady=5,
	  fill = BOTH,
	  expand = YES,
	)

	# quadro centrale
	self.central_square = Frame(self.myBox1,
		background=main_bg,
		relief=FLAT, borderwidth=1,
		padx = 5,
		pady = 5,
	)
	self.central_square.pack(side = TOP,
	  fill = BOTH,
	  expand = YES,
	  ipadx = 5,
	  ipady = 5,
	)

	# Il quadro dei pulsanti basso
	self.bottom_square = Frame(self.myBox1,
		padx=5,
		pady=5,
		background=main_bg,
		#relief=RAISED, borderwidth=1
	)
	self.bottom_square.pack(side = TOP,
	  fill = BOTH,
	  expand = YES,
	)
	
	# quadro sinistra
	self.left_square = Frame(self.central_square,
		background=main_bg,
		#borderwidth = 5,
		#relief = RIDGE,
	)
	self.left_square.pack(side = LEFT,
	  fill = BOTH,
	  expand = YES,
	)

	# quadro destra
	self.right_square = Frame(self.central_square, 
		background=main_bg,
		#borderwidth = 5,
		#relief = RIDGE,
	)
	self.right_square.pack(side = RIGHT,
	  fill = BOTH,
	  expand = YES,
	)
	#--------------------- FIXED LABELS -----------------------
	# etichette sinistra
	# IP
	self.label1 = Label(self.left_square, 
		background=main_bg, foreground=main_fg,
		text="IP: ", 
		anchor='w', 
		font=labFont,
	)
	self.label1.pack(
		fill=X, 
		expand = YES
	)
	
	# Temp
	self.label2 = Label(self.left_square, 
		background=main_bg, foreground=main_fg,
		text="Temp: ", 
		anchor='w', 
		font=labFont,
	)
	self.label2.pack(
		fill=X, 
		expand = YES
	)
	
	# Date
	self.label3 = Label(self.left_square, 
		background=main_bg, foreground=main_fg,
		text="Date: ", 
		anchor='w', 
		font=labFont,
	)
	self.label3.pack(
		fill=X, 
		expand = YES
	)
	
	# Volts
	self.label4 = Label(self.left_square, 
		background=main_bg, foreground=main_fg,
		text="Core: ", 
		anchor='w', 
		font=labFont,
	)
	self.label4.pack(
		fill=X, 
		expand = YES
	)
	
	# Clock
	self.label5 = Label(self.left_square, 
		background=main_bg, foreground=main_fg,
		text="Clock: ", 
		anchor='w', 
		font=labFont,
	)
	self.label5.pack(
		fill=X, 
		expand = YES
	)
	

	#--------------------- VAR LABELS -----------------------
	# etichette destra
	self.label1var = Label(self.right_square, 
		background=main_bg, foreground=main_fg,
		text=get_ip(), 
		anchor='w', 
		font=labFont,
	)
	self.label1var.pack(
		fill=X, 
		expand = YES
	)
	
	#var_temp = StringVar();
	#var_temp.set(get_temp());
	self.label2var = Label(self.right_square, 
		background=main_bg, foreground=main_fg,
		#textvariable=var_temp, 
		anchor='w', 
		font=labFont,
	)
	self.label2var.pack(
		fill=X, 
		expand = YES
	)
	
	#var_date = StringVar()
	#var_date.set(get_date())
	self.label3var = Label(self.right_square, 
		background=main_bg, foreground=main_fg,
	#	textvariable=var_date, 
		anchor='w', 
		font=labFont,
	)
	self.label3var.pack(
		fill=X, 
		expand = YES
	)
	self.label4var = Label(self.right_square, 
		background=main_bg, foreground=main_fg,
		text=get_volts(), 
		anchor='w', 
		font=labFont,
	)
	self.label4var.pack(
		fill=X, 
		expand = YES
	)
	self.label5var = Label(self.right_square, 
		background=main_bg, foreground=main_fg,
		text=get_clock(), 
		anchor='w', 
		font=labFont,
	)
	self.label5var.pack(
		fill=X, 
		expand = YES
	)
	
	# Vengono ora aggiunti i pulsanti a 'button_square'
	#--------------------- TOP BUTTONS -----------------------
	self.pulsante1 = Button(self.button_square, command = self.buttonPress1)
	self.pulsante1.configure(text = "STARTX")
	self.pulsante1.configure(
	  width = but_width, height = but_height,
	  padx = but_padx, pady = but_pady,
	  relief = but_relief, borderwidth = but_borderwidth, 
	  highlightbackground = but_hlbg, highlightcolor = but_hlcol,
	  activebackground = but_actbg, activeforeground = but_actfg,
	  background = but_bg, foreground = but_fg,
	  font=butFont,
	  )
	self.pulsante1.pack(side = LEFT)
	self.pulsante1.bind("<Return>", self.buttonPress1_a)

	self.pulsante2 = Button(self.button_square, command = self.buttonPress2)
	self.pulsante2.configure(text = "EXIT")
	# default focus
	self.pulsante2.focus_force()
	self.pulsante2.configure(
	  width = but_width, height = but_height,
	  padx = but_padx, pady = but_pady,
	  relief = but_relief, borderwidth = but_borderwidth, 
	  highlightbackground = but_hlbg, highlightcolor = but_hlcol,
	  activebackground = but_actbg, activeforeground = but_actfg,
	  background = but_bg, foreground = but_fg,
	  font=butFont,
	  )
	self.pulsante2.pack(side = RIGHT)
	self.pulsante2.bind("<Return>", self.buttonPress2_a)

	#-------------------- BOTTOM BUTTONS ----------------------
	self.pulsante3 = Button(self.bottom_square, command = self.buttonPress3)
	self.pulsante3.configure(text = "REBOOT")
	self.pulsante3.configure(
	  width = but_width, height = but_height,
	  padx = but_padx, pady = but_pady,
	  relief = but_relief, borderwidth = but_borderwidth, 
	  highlightbackground = but_hlbg, highlightcolor = but_hlcol,
	  activebackground = but_actbg, activeforeground = but_actfg,
	  background = but_bg, foreground = but_fg,
	  font=butFont,
	  )
	self.pulsante3.pack(side = LEFT)
	self.pulsante3.bind("<Return>", self.buttonPress3_a)

	self.pulsante4 = Button(self.bottom_square, command = self.buttonPress4)
	self.pulsante4.configure(text = "SHUTDOWN")
	self.pulsante4.configure(
	  width = but_width, height = but_height,
	  padx = but_padx, pady = but_pady,
	  relief = but_relief, borderwidth = but_borderwidth, 
	  highlightbackground = but_hlbg, highlightcolor = but_hlcol,
	  activebackground = but_actbg, activeforeground = but_actfg,
	  background = but_bg, foreground = but_fg,
	  font=butFont,
	  )
	self.pulsante4.pack(side = RIGHT)
	self.pulsante4.bind("<Return>", self.buttonPress4_a)
	
	
  def buttonPress1(self):
	startx();

  def buttonPress2(self):
	self.myParent.destroy()

  def buttonPress3(self):
	restart();

  def buttonPress4(self):
	shutdown();

  # event management (not really used now)
  def buttonPress1_a(self, event):
	self.buttonPress1()
  def buttonPress2_a(self, event):
	self.buttonPress2()
  def buttonPress3_a(self, event):
	self.buttonPress3()
  def buttonPress4_a(self, event):
	self.buttonPress4()
  
  # REFRESH VARS
  def do_refresh(self, date, temp):
	var_date = StringVar()
	var_date.set(date)
	self.label3var.configure(textvariable=var_date);
	var_temp = StringVar();
	var_temp.set(temp);
	self.label2var.configure(textvariable=var_temp);
	# redraw
	root.update_idletasks();

	
# MAIN
root = Tk()
root.geometry("320x240")
pitkGui = PitkGui(root)

def task():
	pitkGui.do_refresh(get_date(), get_temp())
	root.after(1000, task)

root.after(0, task)
root.mainloop()
