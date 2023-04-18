import tkinter as tk
import numpy as np
import turtle as t
from tkinter import messagebox

root=tk.Tk()
root.geometry("640x480")

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

        ship.penup()
        ship.setpos(x0,y0)

    def ping(self):
        rf=int(re.get())
        alf=int(ale.get())
        M=2
        n=1024
        Fs=48000
        dt=1/Fs
        c=1500
        d=1
        tau0=rf/c

        ##координаты цели
        al0=np.deg2rad(90-alf)
        x0=rf*np.cos(al0)
        y0=rf*np.sin(al0)

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
        if re.get()=='' or ale.get()=='':
            messagebox.showinfo('Ошибка','Введите все необходимые данные')
        elif re.get()!='' and int(re.get())<0:
            messagebox.showinfo('Ошибка','Расстояние не может быть отрицательным')
        else:
            self.ping()

win=tk.Canvas(root)
win.create_rectangle(20,20,300,240)
win.place(x=20, y=20)
sys1=t.RawTurtle(win)
sys1.seth(90)
sys1.shape("circle")
sys2=t.RawTurtle(win)
sys2.seth(90)
sys2.shape("circle")
ship=t.RawTurtle(win)
ship.seth(90)
ship.shape("circle")


lbl=tk.Label(root)
lbl.place(x=150, y=300)

##расстояние до цели
re=tk.Entry(root)
re.place(x=512, y=50)
rd=tk.Label(root, text="Расстояние до цели")
rd.place(x=400, y=50)

##курсовой угол
ale=tk.Entry(root)
ale.place(x=512, y=75)
ald=tk.Label(root, text="Курсовой угол")
ald.place(x=400, y=75)

##пеленг
phe=tk.Label(root, text="0")
phe.place(x=512, y=100)
phd=tk.Label(root, text="Пеленг")
phd.place(x=400, y=100)

##тип цели
tye=tk.Label(root, text="undefined")
tye.place(x=512, y=125)
tyd=tk.Label(root, text="Тип цели")
tyd.place(x=400, y=125)

pr=Setup()

srt=tk.Button(root, text="START", command=pr.start, height=3, width=10)
srt.place(x=470, y=210)

root.mainloop()
