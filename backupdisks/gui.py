#!/usr/bin/env python3

import tkinter as tk
from tkinter import Tk
from tkinter.ttk import Frame
import os
import sys
import subprocess

diskName='BVHBUP{XXXX}' # TODO

def main():

	frame = Frame()
	frame.grid()
	
	tk.Label(frame, text='').grid() 
	tk.Label(frame, text='    ~~~ BACKUP DISK :' + diskName + ': CONNECTED ~~~    ').grid()
	tk.Label(frame, text='').grid() 

	tk.Button(frame, text='BACKUP EVERYTHING', command=all).grid()
	tk.Label(frame, text='').grid() 
	
	tk.Label(frame, text='...or...').grid() 
	tk.Button(frame, text='- Sync SVN -',     command=svnsync).grid()
	tk.Button(frame, text='- Pull Git -',     command=gitpull).grid()
	tk.Button(frame, text='- Backup files -', command=files  ).grid()

	tk.Label(frame, text='').grid() 
	tk.Button(frame, text='< Quit >', command=sys.exit).grid()
	tk.Label(frame, text='').grid() 

	frame.master.title('Backup')
	frame.mainloop()
	
def all():
	svnsync()
	gitpull()
	files()
	
def svnsync():
	p = subprocess.Popen('gnome-terminal -e ./syncall.sh', shell=True, cwd='svnsync', start_new_session=True)
	
def gitpull():
	p = subprocess.Popen('gnome-terminal -e ./pullall.sh', shell=True, cwd='git', start_new_session=True)
	
def files():
	p = subprocess.Popen('gnome-terminal -e ./run.sh', shell=True, cwd='rsnapshot', start_new_session=True)
	
main()

