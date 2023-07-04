import tkinter as tk
import numpy as np
import turtle as t
from tkinter.messagebox import showerror, showinfo
from tkinter import ttk

root=tk.Tk()
root.geometry("720x1280")
root.title("Гидролокатор")

class HydroAz():
    def _init_(self):
        self.rft=rft
        self.phft=phft
        self.alft=alft
        self.tyft=tyft
        self.sre=sre
        self.sale=sale
        self.stye=stye
        self.sugc=sugc
        self.sroot=sroot
        self.F=F
        self.t=t
        
##выводит введенные данные в основную программу
    def Fetch(self):
        try:
            fch=[0]*7
            fch[0]=int(self.sre.get())    ##расстояние до цели
            fch[1]=int(self.sale.get())   ##курсовой угол
            fch[2]=int(self.sphe.get())   ##пеленг
            fch[3]=int(self.sfre.get())   ##частота сигнала
            fch[4]=float(self.stie.get()) ##длительность сигнала
            fch[5]=self.salc.get()        ##на какую сторону идет поворот
            fch[6]=self.sugc.get()        ##тип сигнала
            if fch[5]=="" or fch[6]=="":
                showerror(title="Ошибка",message="Введите все данные")
            else:
                self.sroot.withdraw() ##прячет окно
                return fch
        except (ValueError, TypeError, AttributeError):
            showerror(title="Ошибка",message="Введите все данные")

    def Help(self):
        msg="ТОРПЕДА: 10-50кГц, 0.1-0.3с, непрерывный\nКОРАБЛЬ: 3-12кГц, больше 0.3с, непрерывный\nПОДЛОДКА: 0.8-16кГц, 0.1-0.3с, одиночный\nПРОЧЕЕ: все остальное\nРасстояние не больше 350-500м, больше уйдет за границы\nПри нажатии ОК может пропасть окно ввода данных, но на деле основное просто становится активным, второе никуда не пропало и не спряталось"
        showinfo(title="Help", message=msg)

##создает отдельное окно для ввода данных
    def SETUP(self):
        
        self.sroot=tk.Tk()
        self.sroot.geometry("640x480")
        self.sroot.title("Ввод данных")
        
        sui=tk.Frame(self.sroot)
        sui.pack()

        ##расстояние до цели
        srb=tk.Frame(sui)
        srb.pack()
        srd=tk.Label(srb, text="Расстояние до цели, м")
        srd.pack(side=tk.LEFT)
        self.sre=tk.Entry(srb)
        self.sre.pack(side=tk.LEFT)

        ##курсовой угол
        salb=tk.Frame(sui)
        salb.pack()
        sald=tk.Label(salb, text="Курсовой угол, град")
        sald.pack(side=tk.LEFT)
        self.sale=tk.Entry(salb)
        self.sale.pack(side=tk.LEFT)
        types=["Левый борт","Правый борт"]
        self.salc=tk.ttk.Combobox(salb, values=types)
        self.salc.pack(side=tk.LEFT)

        ##пеленг
        sphb=tk.Frame(sui)
        sphb.pack()
        sphd=tk.Label(sphb, text="Пеленг, град")
        sphd.pack(side=tk.LEFT)
        self.sphe=tk.Entry(sphb)
        self.sphe.pack(side=tk.LEFT)

        #частота сигнала
        sfrb=tk.Frame(sui)
        sfrb.pack()
        sfrd=tk.Label(sfrb, text="Частота сигнала, Гц")
        sfrd.pack(side=tk.LEFT)
        self.sfre=tk.Entry(sfrb)
        self.sfre.pack()

        #длительность сигнала
        stib=tk.Frame(sui)
        stib.pack()
        stid=tk.Label(stib, text="Длительность сигнала, с")
        stid.pack(side=tk.LEFT)
        self.stie=tk.Entry(stib)
        self.stie.pack()

        ##тип сигнала
        sugb=tk.Frame(sui)
        sugb.pack()
        sugd=tk.Label(sugb, text="Тип сигнала")
        sugd.pack(side=tk.LEFT)
        tsig=["Непрерывный","Одиночный"]
        self.sugc=tk.ttk.Combobox(sugb, values=tsig)
        self.sugc.pack(side=tk.LEFT)

        ##закрывает окно
        cat=tk.Button(self.sroot, text="CANCEL", command=self.sroot.destroy, height=1, width=10)
        cat.pack(side=tk.BOTTOM)

        ##окно помощи
        cat=tk.Button(self.sroot, text="HELP", command=self.Help, height=1, width=10)
        cat.pack(side=tk.BOTTOM)
        
        ##передает введенные данные
        okt=tk.Button(self.sroot, text="OK", command=self.Fetch, height=1, width=10)
        okt.pack(side=tk.BOTTOM)

##графическое окно гидролокатора, показывает тип найденной цели и ее положение        
    def plot(self,x,y,x0,y0,tyft,rtt,alft):
        
        sys1.penup()
        sys1.setpos(x[0],y[0])

        sys2.penup()
        sys2.setpos(x[1],y[1])

        ship.setpos(x0,y0)
        ship.shapesize(2,2)
        
        if tyft=="Торпеда":
            ship.shape("classic")
            ship.color('red')
        elif tyft=="Надводный корабль":
            ship.shape("classic")
            ship.color('red','yellow')
        elif tyft=="Подводная лодка":
            ship.shape("classic")
            ship.color('blue')
        elif tyft=="Прочее":
            ship.shape("classic")
            ship.color('green')

        if rtt=="Левый борт":
            ship.left(alft)
        elif rtt=="Правый борт":
            ship.right(alft)
            
##классификатор целей
    def CLSFK(self,F,t,sugh):
        tyft=""
        if F>=10000 and F<=50000 and t<=0.3 and t>0.1 and sugh=="Непрерывный":
            tyft="Торпеда"
            tye.configure(text=tyft)
        if F>=3000 and F<=120000 and t>0.3 and sugh=="Непрерывный":
            tyft="Надводный корабль"
            tye.configure(text=tyft)
        if F>=800 and F<16000 and t>=0.1 and t<0.3 and sugh=="Одиночный":
            tyft="Подводная лодка"
            tye.configure(text=tyft)
        elif F<800 and F>12000:
            tyft="Прочее"
            tye.configure(text=tyft)
        return tyft
    
##основная программа гидролокатора
    def ping(self):
        ##загрузка параметров
        fch=self.Fetch()
        rf=fch[0]   ##расстояние до цели
        alft=fch[1] ##курсовой угол
        alf=fch[2]  ##пеленг
        F=fch[3]    ##частота сигнала
        t=fch[4]    ##длительность сигнала
        rtt=fch[5]  ##на какую сторону идет поворот
        ugh=fch[6]  ##тип сигнала
        
        ##параметры приемной системы
        M=2       ##число приемников
        n=1024    ##число точек БПФ
        Fs=480000 ##частота дискретизации
        dt=1/Fs   ##шаг отсчетов времени
        df=Fs/n   ##шаг дискретизации
        c=1500    ##скорость звука в воде
        d=1       ##расстояние между приемниками

        ##координаты цели
        x0=rf*np.cos(np.deg2rad(90-alf))
        y0=rf*np.sin(np.deg2rad(90-alf))
        tau0=rf/c

        ##формирование сигнала и нахождение его частоты
        Tr=np.array(np.arange(0,t,dt))    ##массив времени
        Fk=np.array(np.arange(0,n*df,df)) ##массив частот
        Sg=np.sin(2*np.pi*F*Tr)           ##сигнал
        Sp=abs(np.fft.fft(Sg,n))          ##спектр
        Sf=Sp.tolist()
        Ff=Fk[Sf.index(max(Sf))]          ##частота

        ##формирование типа сигнала
        ##реализованно довольно просто: берется шесть массивов одинаковой
        ##длины, при одиночном сигнале один из массивов это массив сигнала,
        ##остальные - нули, при непрерывном генерируется пачка из трех
        ##импульсов, представляющая собой чередование массивов сигнала
        ##и нулевых
        Sq=np.zeros(len(Sg))
        Ss=[]
        scnt=0
        if ugh=="Непрерывный":
            for i in range(0,3):
                Ss.append(Sg)
                Ss.append(Sq)
        elif ugh=="Одиночный":
            Ss.append(Sg)
            for i in range(0,5):
                Ss.append(Sq)
                
        ##определение типа сигнала
        ##полученный массив массивов проверяется поэлементно на соотвествие
        ##элементам массива сигнала, считается количество подходящих элементов
        ##и затем оно делится на длину массива сигнала. если результат деления
        ##равен 1, сигнал одиночный, иначе непрерывный
        for i in range (0,len(Ss)):
            Sw=Ss[i]
            for j in range (0,len(Sw)):
                if Sw[j]==Sg[j]:
                    scnt=scnt+1
                    
        if round(scnt/len(Sg))>1:
            sugh="Непрерывный"
        else:
            sugh="Одиночный"
                
        tyft=self.CLSFK(F,t,sugh)

        ##координаты приемников
        xl=1
        x=[-0.5, 0.5]
        y=[0, 0]

        ##нахождение расстояния
        tau=np.zeros(M)
        for i in range(0,M):
            Rip=(x[i]-x0)**2+(y[i]-y0)**2
            Ri=np.sqrt(Rip)
            tau[i]=(Ri/c)-tau0

        Tt=(1/2)*np.sqrt(abs((2*(tau[0]**2))+(2*(tau[1]**2))-(xl**2)))
        Rt=(Tt+tau0)*c-Tt*c
        re.configure(text=round(Rt))

        ##нахождение пеленга
        Pg=np.arccos(y0/Rt)
        Az=np.rad2deg(Pg)
        if x0<0:
            Az=360-Az
        phe.configure(text=round(Az,1))

        ##нахождение курсового угла цели
        rbe=90+Az
        rbf=180-rbe
        ale.configure(text=round(rbf,1))
        
        self.plot(x,y,x0,y0,tyft,rtt,alft)

##фунция начала программы для кнопки в основном окне
    def start(self):
            self.ping()
            self.sroot.destroy()
            
##формирование основного окна

##графическое окно
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

ui=tk.Frame(root)
ui.pack()

##расстояние до цели
rb=tk.Frame(ui)
rb.pack()
rd=tk.Label(rb, text="Расстояние до цели, м:")
rd.pack(side=tk.LEFT)
re=tk.Label(rb, text="0")
re.pack(side=tk.LEFT)

##курсовой угол
alb=tk.Frame(ui)
alb.pack()
ald=tk.Label(alb, text="Курсовой угол, град:")
ald.pack(side=tk.LEFT)
ale=tk.Label(alb, text="0")
ale.pack(side=tk.LEFT)

##пеленг
phb=tk.Frame(ui)
phb.pack()
phd=tk.Label(phb, text="Пеленг, град:")
phd.pack(side=tk.LEFT)
phe=tk.Label(phb, text="0")
phe.pack(side=tk.LEFT)

##тип цели
tyb=tk.Frame(ui)
tyb.pack()
tyd=tk.Label(tyb, text="Тип цели:")
tyd.pack(side=tk.LEFT)
tye=tk.Label(tyb, text="undefined")
tye.pack(side=tk.LEFT)

pr=HydroAz()

##начинает программу
srt=tk.Button(root, text="START", command=pr.start, height=1, width=10)
srt.pack(side=tk.BOTTOM)

##выводит окно ввода данных
opt=tk.Button(root, text="SETUP", command=pr.SETUP, height=1, width=10)
opt.pack(side=tk.BOTTOM)

root.mainloop()
