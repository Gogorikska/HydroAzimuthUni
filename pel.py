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
        print(rf)
        alf=ale.get()
        M=2
        n=1024
        Fs=48000
        dt=1/Fs
        rf=1000
        alf=45
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
            print(Rip)
            Ri=np.sqrt(Rip)
            print(Ri)
            tau[i]=(Ri/c)-tau0
            print(tau)
            ntau[i]=np.ceil(abs(tau[i])*Fs)
            
        for i in range(0,M):
            utau=n+np.sum(ntau)
            print(utau)
            u0=np.random.randn(1,utau.astype(int))
            print(u0)
            t0a=u0.size
            print(t0a)
            t0=np.array(np.arange(1,t0a+1))*dt+np.min(tau)
            print(len(t0))
            ta=n+1
            t1=np.array(np.arange(1,ta))*dt
            s0=t1-tau[i]
            print(len(s0))
            u00=np.ndarray.flatten(u0)
            print(u00.size)
            S=np.interp(s0, t0, u00)
            Y[i,]=np.fft.fft(S,n)

        Yc=np.conjugate(Y)
        Ym=Y*Yc
        Yii=abs(np.fft.ifft(Ym,n))
        Yi=np.fft.ifftshift(Yii)
        Pi=max(Yi)
        Yi1=Yi.tolist()
        Pg=Yi1.index(Pi)

        Tc1=-(n-1)/2
        Tc2=(n-1)/2
        Tc=np.array(np.arange(Tc1,Tc2))
        Nk=Tc*dt
        ar=Nk*c/d
        alsr=abs(np.emath.arcsin(ar))
        als=np.rad2deg(alsr)
        alsl=als.tolist()
        ping=alsl[Pg]
        print(ping)

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
