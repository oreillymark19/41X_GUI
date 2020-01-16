import csv
import os
import sys
import glob
from csv import reader
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

env = input('Input folder where data files are stored: ')

files = glob.glob(env + '/*.csv')
numSessions = len(files)

with open(env + '/raw.csv', 'r') as raw:
  rawplotdata = csv.reader(raw, delimiter=',')
  rawdata = []
  rawdatatimepoints = []
  for row in rawplotdata:
    raw = row[0]
    rawtp = row[1]

    rawdata.append(float(raw))
    rawdatatimepoints.append(float(rawtp))
    
with open(env + '/rectified.csv', 'r') as rectified:
  rectifiedplotdata = csv.reader(rectified, delimiter=',')
  rectifieddata = []
  rectifieddatatimepoints = []
  for row in rectifiedplotdata:
    rectified = row[0]
    rectifiedtp = row[1]

    rectifieddata.append(float(rectified))
    rectifieddatatimepoints.append(float(rectifiedtp))

with open(env + '/enveloped.csv', 'r') as env:
  envplotdata = csv.reader(env, delimiter=',')
  envdata = []
  envdatatimepoints = []
  for row in envplotdata:
    env = row[0]
    envtp = row[1]

    envdata.append(float(env))
    envdatatimepoints.append(float(envtp))

with open(env + '/compare.csv', 'r') as comp:
  compplotdata = csv.reader(comp, delimiter=',')
  compdata = []
  compdata2 = []
  compdatatimepoints = []
  for row in compplotdata:
    comp = row[0]
    comp2 = row[1]
    comptp = row[2]

    compdata.append(float(comp))
    compdata2.append(float(comp2))
    compdatatimepoints.append(float(comptp))



for x in range (1, numSessions):
    print('Looking at file %d' % (x))
    with open(env + '/test1.csv', 'r') as f:
              data = csv.reader(f, delimiter=',')
              dates = []
              colors = []
              TreatFreqList = []
              degenList = []
              treattimelist = []
              variable4list = []
              variable5list = []
              variable6list = []
              for row in data:
                  treatfreqholder = row[0]
                  degenholder = row[1]
                  treattimeholder = row[2]
                  variable4hold = row[3]
                  variable5hold = row[4]
                  variable6hold = row[5]

                  TreatFreqList.append(treatfreqholder)
                  degenList.append(degenholder)
                  treattimelist.append(treattimeholder)
                  variable4list.append(variable4hold)
                  variable5list.append(variable5hold)
                  variable6list.append(variable6hold)

              datestr = ''.join(dates)
              colorstr = ''.join(colors)
    TreatFreqstr = ''.join(TreatFreqList)
    degenstr = ''.join(degenList)
    treattimestr = ''.join(treattimelist)
    variable4str = ''.join(variable4list)
    variable5str = ''.join(variable5hold)
    variable6str = ''.join(variable6hold)

listopt = ['Dashboard', 'Raw EMG Data', 'Rectified EMG Data', 'Enveloped EMG Data', 'Degeneration Plot']

def GUIFrame():
    
    root = Tk()
    root.configure(background = "#7EB6FF")
    root.title("Selection Window")
    root.geometry("500x175")
    root.resizable(1,1)
    selected = StringVar(root)
    selected.set('Select an Option')
    dropdown = OptionMenu(root, selected,'Dashboard', 'Raw EMG Data', 'Rectified EMG Data', 'Enveloped EMG Data', 'Degeneration Plot')
    dropdown.config(bg = "white", fg = "#3D3D3D	", font="{Georgia} 24 bold", width=20, height=2)
    dropdown.pack()
    
    

    def WindowSelect():
       if selected.get() == 'Dashboard':
           loadDash(root)
       elif selected.get() == 'Raw EMG Data':
           RawData(root)
       elif selected.get() == 'Rectified EMG Data':
           RectifiedData(root)
       elif selected.get() == 'Enveloped EMG Data':
           EnvelopedData(root)
       elif selected.get() == 'Degeneration Plot':
           CompData(root)

    def loadDash(root):
        t = Toplevel(root)
        t.wm_title("Dashboard")
        t.configure(background = "#7EB6FF")

        Title = Label(t, text="Treatment Dashboard", borderwidth=10, relief="ridge", fg = "#3D3D3D",bg = "#EE6363", font = "Verdana 36 bold")
        Title.grid(row=1, column=1, sticky=E+W, padx=(50,50), pady=(50,0), columnspan=3)
        
        
        TreatFreq=Label(t, text="Times treatment used", borderwidth=5, relief="ridge", fg = "#3D3D3D",bg = "#EE6363", font = 
          "Verdana 20 bold")
        TreatFreq.grid(row=2, column=1, sticky=E+W, padx=(50,50), pady=(50,0))
        
        Label(t, text = TreatFreqstr, fg = "#3D3D3D",bg = "#7EB6FF", font = "Verdana 36 bold").grid(row=3,column=1,sticky=S, padx = (50,50))

        Degen = Label(t, text="Percent Degeneration",borderwidth=5, relief="ridge", fg = "#3D3D3D",bg = "#EE6363", font = 
          "Verdana 20 bold").grid(row=2, column=2, sticky=E+W, padx=(50,100), pady=(50,0))
        
        Label(t, text = degenstr + "%", fg = "#3D3D3D",bg = "#7EB6FF", font = "Verdana 36 bold").grid(row=3, column=2, sticky=S, padx=(50,100))

        treattime = Label(t, text="Total Treatment Time", borderwidth=5, relief="ridge", fg = "#3D3D3D",bg = "#EE6363", 
          font = "Verdana 20 bold").grid(row=2, column=3, sticky=E+W, padx=(50,50), pady=(50,0))
        
        Label(t, text = treattimestr + " min", fg = "#3D3D3D",bg = "#7EB6FF", font = "Verdana 36 bold").grid(row=3, column=3, sticky=S, padx=(50,50))

        variable4 = Label(t, text="Variable 4",borderwidth=5, relief="ridge", fg = "#3D3D3D",bg = "#EE6363", 
          font = "Verdana 20 bold")
        variable4.grid(row=4, column=1, sticky=E+W , padx=(50,50), pady=(50,0))
        
        Label(t, text = variable4str, fg = "#3D3D3D",bg = "#7EB6FF", font = "Verdana 36 bold").grid(row=5, column=1, sticky=S, padx=(50,50), pady=(0,50))

        variable5 = Label(t, text="Variable 5", borderwidth=5, relief="ridge", fg = "#3D3D3D",bg = "#EE6363", 
          font = "Verdana 20 bold").grid(row=4, column=2, sticky=E+W, padx=(50,100), pady=(50,0))
        
        Label(t, text = variable5str, fg = "#3D3D3D",bg = "#7EB6FF", font = "Verdana 36 bold").grid(row=5, column=2, sticky=S, padx=(50,100), pady=(0,50))
        
        variable6 = Label(t, text="Variable 6",borderwidth=5, relief="ridge", fg = "#3D3D3D",bg = "#EE6363",
         font = "Verdana 20 bold").grid(row=4, column=3, sticky=E+W, padx=(50,50), pady=(50,0))
        
        Label(t, text = variable6str, fg = "#3D3D3D",bg = "#7EB6FF", font = "Verdana 36 bold").grid(row=5, column=3, sticky=S, padx=(50,50), pady=(0,50))

    def RawData(root):
      p = Toplevel(root)
      p.wm_title("Raw EMG Data")
      fig = Figure(figsize=(5,5), dpi=100)
      a = fig.add_subplot(111)
      a.plot(rawdatatimepoints, rawdata)

      canvas = FigureCanvasTkAgg(fig, p)
      canvas.show()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

      toolbar = NavigationToolbar2TkAgg(canvas, p)
      toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def RectifiedData(root):
      q = Toplevel(root)
      q.wm_title("Rectified EMG Data")
      fig = Figure(figsize=(5,5), dpi=100)
      recplot = fig.add_subplot(111)
      recplot.plot(rectifieddatatimepoints, rectifieddata)

      canvas = FigureCanvasTkAgg(fig, q)
      canvas.show()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

      toolbar = NavigationToolbar2TkAgg(canvas, q)
      toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def EnvelopedData(root):
      l = Toplevel(root)
      l.wm_title("Enveloped EMG Data")
      fig = Figure(figsize=(5,5), dpi=100)
      envplot = fig.add_subplot(111)
      envplot.plot(envdatatimepoints, envdata)

      canvas = FigureCanvasTkAgg(fig, l)
      canvas.show()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

      toolbar = NavigationToolbar2TkAgg(canvas, l)
      toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def CompData(root):
      w = Toplevel(root)
      #w.configure(background = "#7EB6FF")
      w.wm_title("Degeneration Plot")
      fig = Figure(figsize=(6,6), dpi=100, facecolor = '#7EB6FF')
      fig.suptitle('Degeneration Plot', fontsize=14, fontweight='bold')
      compplot = fig.add_subplot(111, axisbg="white")
      compplot.plot(compdatatimepoints, compdata, label = "Functional Limb Strength")
      compplot.plot(compdatatimepoints, compdata2, label = "Injured Limb Strength")
      compplot.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=4, ncol=2, borderaxespad=0)
      compplot.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
      #compplot.set_axis_bgcolor('#7EB6FF')
      canvas = FigureCanvasTkAgg(fig, w)
      canvas.show()
      canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

      toolbar = NavigationToolbar2TkAgg(canvas, w)
      toolbar.update()
      canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    button = Button(root, text='Go', command=WindowSelect)
    button.config(bg = "white", fg = "#3D3D3D", font = "{Georgia} 24 bold", width = 11,height =1)
    button.pack()
    root.mainloop()
 
              
GUIFrame()

    

    
