import tkinter as tk
import numpy as np
import turtle as t
import scipy as sp
from tkinter import messagebox

root=tk.Tk()
root.geometry("720x1280")

class Setup():
    def _init_(self):
        self.rf=rf
        self.phf=phf
        self.alf=alf
        self.tyf=tyf
        
    def plot(self,x,y,x0,y0):
        
        sys1.penup()
        sys1.setpos(x[0],y[0])

        sys2.penup()
        sys2.setpos(x[1],y[1])

    def ping(self):
        M=2
        n=1024
        Fs=48000
        dt=1/Fs
        c=1500
        d=1

        ##координаты цели
        [x0, y0]=ship.pos()
        al0=np.arctan(abs(y0)/abs(x0))
        if x0>0 and y0>0:
            al0=(np.pi/2)-al0
        elif x0>0 and y0<0:
            al0=al0+(np.pi/2)
        elif x0<0 and y0<0:
            al0=(np.pi/2)-al0+np.pi
        elif x0<0 and y0>0:
            al0=al0+(np.pi/2)+np.pi
        rf=round(abs(y0)/abs(np.cos(al0)))
        alf=round(np.rad2deg(al0))
        tau0=rf/c
        
        re.configure(text=rf)
        ale.configure(text=alf)

        ##координаты приемников
        x=np.array([0,0])
        y=np.array([-0.5,0.5])

        Y=np.zeros([M,n])
        tau=np.zeros(M)
        ntau=np.zeros(M)
        for i in range(0,M):
            Rip=(x[i]-x0)**2+(y[i]-y0)**2
            Ri=np.sqrt(Rip)
            tau[i]=(Ri/c)-tau0
            ntau[i]=np.ceil(abs(tau[i])*Fs)
            
        for i in range(0,M):
            utau=n+np.sum(ntau)
            u0=np.random.randn(1,utau.astype(int))
            t0a=u0.size
            t0=np.array(np.arange(1,t0a+1))*dt+np.min(tau)
            ta=n+1
            t11=np.array(np.arange(1,ta))*dt
            t1=t11-tau[i]
            u00=np.ndarray.flatten(u0)
            S=np.interp(t1, t0, u00)
            Y[i,]=np.fft.fft(S,n)

        Yc=np.conjugate(Y[1,])
        Ym=Y[0,]*Yc
        Ypi=abs(np.fft.ifft(Ym,n))
        Yp=np.fft.ifftshift(Ypi)
        Yi=abs(Yp)
        Pi=max(Yi)
        Yi1=Yi.tolist()
        Pg=Yi1.index(Pi)+1

        Tc1=-(n-1)/2
        Tc2=(n-1)/2
        Tc=np.array(np.arange(Tc1,Tc2))
        Nk=Tc*dt
        ar=Nk*c/d
        alsr=abs(np.emath.arcsin(ar))
        als=np.rad2deg(alsr)
        alsl=als.tolist()
        ping=round(alsl[Pg])
        phe.configure(text=ping)
        self.plot(x,y,x0,y0)
        
    def start(self):
            self.ping()
            

win=tk.Canvas(root, width=720, height=720)
win.pack(anchor=tk.NW)

scr=t.TurtleScreen(win)

sys1=t.RawTurtle(scr)
sys1.seth(90)
sys1.shape("circle")

sys2=t.RawTurtle(scr)
sys2.seth(90)
sys2.shape("circle")

ship=t.RawTurtle(scr)
ship.seth(90)
ship.shape("circle")
ship.penup()
scr.onclick(ship.goto)

ui=tk.Frame(root)
ui.pack()

##расстояние до цели
rb=tk.Frame(ui)
rb.pack()
rd=tk.Label(rb, text="Расстояние до цели")
rd.pack(side=tk.LEFT)
re=tk.Label(rb, text="0")
re.pack(side=tk.LEFT)

##курсовой угол
alb=tk.Frame(ui)
alb.pack()
ald=tk.Label(alb, text="Курсовой угол")
ald.pack(side=tk.LEFT)
ale=tk.Label(alb, text="0")
ale.pack(side=tk.LEFT)

##пеленг
phb=tk.Frame(ui)
phb.pack()
phd=tk.Label(phb, text="Пеленг")
phd.pack(side=tk.LEFT)
phe=tk.Label(phb, text="0")
phe.pack(side=tk.LEFT)

##тип цели
tyb=tk.Frame(ui)
tyb.pack()
tyd=tk.Label(tyb, text="Тип цели")
tyd.pack(side=tk.LEFT)
tye=tk.Label(tyb, text="undefined")
tye.pack(side=tk.LEFT)

pr=Setup()

srt=tk.Button(root, text="START", command=pr.start, height=1, width=10)
srt.pack(side=tk.BOTTOM)

root.mainloop()
