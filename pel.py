import tkinter as tk
import numpy as np

root=tk.Tk()
root.geometry("640x480")

class Setup():
    def _init_(self):
        self.rf=rf
        self.phf=phf
        self.alf=alf
        self.tyf=tyf
        
    def message(self):
        rf=re.get()
        phf=phe.get()
        alf=ale.get()
        tyf=tye.get()
        print(rf)

    def ping(self):
        rf=re.get()
        alf=ale.get()
        n=1024
        Fs=48000
        dt=1/Fs
        rf=1000
        alf=45
        c=1500
        tau0=rf/c

        al0=np.deg2rad(90-alf)
        x0=rf*np.cos(al0)
        y0=rf*np.sin(al0)

        x=0
        y=0

        Rip=(x-x0)**2+(y-y0)**2
        Ri=np.sqrt(Rip)
        tau=(Ri/c)-tau0

        
        ntau=np.ceil(abs(tau)*Fs)
        utau=n+ntau
        u0=np.random.randn(1,utau.astype(int))
        t0a=u0.size-1
        t0=np.array(np.arange(1,t0a))*dt+np.min(ntau)
        ta=n-1
        t1=np.array(np.arange(1,ta))*dt
        s0=t1-tau
        S=np.interp(t0, u0,
        print(t0)

win=tk.Canvas(root)
win.create_rectangle(20,20,300,240)
win.place(x=20, y=20)

lbl=tk.Label(root)
lbl.place(x=150, y=300)

re=tk.Entry(root)
re.place(x=400, y=50)

phe=tk.Entry(root)
phe.place(x=400, y=75)

ale=tk.Entry(root)
ale.place(x=400, y=100)

tye=tk.Entry(root)
tye.place(x=400, y=125)

pr=Setup()

srt=tk.Button(root, text="START", command=pr.ping, height=3, width=10)
srt.place(x=420, y=210)

root.mainloop()
