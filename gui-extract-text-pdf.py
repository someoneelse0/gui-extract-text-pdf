#!/usr/bin/python3
#-*- coding:utf8 -*-

import PyPDF2 as pdf, tkinter as tk

t=tk.Tk()
t.title("Text extractor from pdf")

fpdf=tk.StringVar()
wp=tk.StringVar()

def p(fn,wp):
	p=pdf.PdfReader(fn+".pdf")
	oo=open(wp,"w")
	for i in p.pages:
		oo.write(i.extract_text())
	

tl0=tk.Label(t,text="Portable File Format (pdf) to read: ")
tl0.grid(row=0,column=0)
te0=tk.Entry(t,textvariable=fpdf)
te0.grid(row=0,column=1)
l0=tk.Label(t,text="(without extension)")
l0.grid(row=1,column=1)
tl1=tk.Label(t,text="Filename to write: ")
tl1.grid(row=2,column=0)
te1=tk.Entry(t,textvariable=wp)
te1.grid(row=2,column=1)
b0=tk.Button(t,text="Read and write",command=lambda:p(fpdf.get(),wp.get()))
b0.grid(row=4,column=2,columnspan=2)

t.mainloop()
