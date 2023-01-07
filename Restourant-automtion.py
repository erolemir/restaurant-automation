from tkinter import *

class Odev:
    def __init__(self):
        self.pencere=Tk()
        self.pencere.title("Emirhan Erol")
        self.pencere.geometry("850x600+350+50")
        self.pencere.resizable(FALSE,FALSE)
        self.pencere.configure(background="grey10")
        self.yemekler()
        self.icecekler()
        self.mezeler()
        self.hesapla()
        self.fis()

# Yemekleri bu bölümde tanımlıyorum.
    def yemekler(self):
        self.baslik = Label(self.pencere,text="Günlük Yemekler",font=("Arial",20,"bold","underline"),bg="grey10",fg="#EEEEEE")
        self.baslik.place(x=50,y=40)
        
        self.pilav= Label(self.pencere,text="Pilav",fg="#EEEEEE",bg="grey10") 
        self.pilav.place(x=50,y=90)
        self.pilavEntry= Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.pilavEntry.insert(0, "0")
        self.pilavEntry.place(x=150,y=90)
        
        self.tavuk=Label(self.pencere,text="Tavuk",fg="#EEEEEE",bg="grey10")
        self.tavuk.place(x=50,y=120)
        self.tavukEntry=Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.tavukEntry.insert(0, "0")
        self.tavukEntry.place(x=150,y=120)
        
        self.makarna= Label(self.pencere,text="Makarna",fg="#EEEEEE",bg="grey10")
        self.makarna.place(x=50,y=150)
        self.makarnaEntry= Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.makarnaEntry.insert(0, "0")
        self.makarnaEntry.place(x=150,y=150)
        
        self.kofteler= Label(self.pencere,text="Köfteler",fg="#EEEEEE",bg="grey10")
        self.kofteler.place(x=50,y=180)
        self.koftelerEntry= Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.koftelerEntry.insert(0, "0")
        self.koftelerEntry.place(x=150,y=180)
        
        self.fasulye = Label(self.pencere,text="Fasulye",fg="#EEEEEE",bg="grey10")
        self.fasulye.place(x=50,y=210)
        self.fasulyeEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.fasulyeEntry.insert(0, "0")
        self.fasulyeEntry.place(x=150,y=210)
        
        self.manti = Label(self.pencere,text="Mantı",fg="#EEEEEE",bg="grey10")
        self.manti.place(x=50,y=240)
        self.mantiEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.mantiEntry.insert(0, "0")
        self.mantiEntry.place(x=150,y=240)
        
        self.salata = Label(self.pencere,text="Salata",fg="#EEEEEE",bg="grey10")
        self.salata.place(x=50,y=270)
        self.salataEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.salataEntry.insert(0, "0")
        self.salataEntry.place(x=150,y=270)
        
        self.borek = Label(self.pencere,text="Börek",fg="#EEEEEE",bg="grey10")
        self.borek.place(x=50,y=300)
        self.borekEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.borekEntry.insert(0, "0")
        self.borekEntry.place(x=150,y=300)
        
        self.karniyarik = Label(self.pencere,text="Karnıyarık",fg="#EEEEEE",bg="grey10")
        self.karniyarik.place(x=50,y=330)
        self.karniyarikEntry = Entry(self.pencere,bg="lavender", bd=5, relief=RAISED)
        self.karniyarikEntry.insert(0, "0")
        self.karniyarikEntry.place(x=150,y=330)
        
# İçecekleri bu bölümde tanımlıyorum.
    def icecekler(self):
        self.baslik = Label(self.pencere,text="İçecekler",font=("Arial",20,"bold","underline"),bg="grey10",fg="#EEEEEE")
        self.baslik.place(x=90,y=380)
        
        self.kola = Label(self.pencere,text="Kola",fg="#EEEEEE",bg="grey10")
        self.kola.place(x=50,y=430)
        self.kolaEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.kolaEntry.insert(0, "0")
        self.kolaEntry.place(x=150,y=430)
        
        self.fanta = Label(self.pencere,text="Fanta",fg="#EEEEEE",bg="grey10")
        self.fanta.place(x=50,y=460)
        self.fantaEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.fantaEntry.insert(0, "0")
        self.fantaEntry.place(x=150,y=460)
        
        self.ayran = Label(self.pencere,text="Ayran",fg="#EEEEEE",bg="grey10")
        self.ayran.place(x=50,y=490)
        self.ayranEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.ayranEntry.insert(0, "0")
        self.ayranEntry.place(x=150,y=490)
        
        self.su = Label(self.pencere,text="Su",fg="#EEEEEE",bg="grey10")
        self.su.place(x=50,y=520)
        self.suEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.suEntry.insert(0, "0")
        self.suEntry.place(x=150,y=520)
        
        self.madensuyu = Label(self.pencere,text="Madensuyu",fg="#EEEEEE",bg="grey10")
        self.madensuyu.place(x=50,y=550)
        self.madensuyuEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.madensuyuEntry.insert(0, "0")
        self.madensuyuEntry.place(x=150,y=550)
        
# Mezeleri bu bölümde tanımlıyorum.
    def mezeler(self):
        self.baslik = Label(self.pencere,text="Mezeler",font=("Arial",20,"bold","underline"),bg="grey10",fg="#EEEEEE")
        self.baslik.place(x=500,y=40)
        
        self.humus = Label(self.pencere,text="Humus",fg="#EEEEEE",bg="grey10")
        self.humus.place(x=450,y=90)
        self.humusEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.humusEntry.insert(0, "0")
        self.humusEntry.place(x=550,y=90)
        
        self.cacik = Label(self.pencere,text="Cacık",fg="#EEEEEE",bg="grey10")
        self.cacik.place(x=450,y=120)
        self.cacikEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.cacikEntry.insert(0, "0")
        self.cacikEntry.place(x=550,y=120)
        
        self.kisir = Label(self.pencere,text="Kısır",fg="#EEEEEE",bg="grey10")
        self.kisir.place(x=450,y=150)
        self.kisirEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.kisirEntry.insert(0, "0")
        self.kisirEntry.place(x=550,y=150)
        
        self.dolma = Label(self.pencere,text="Dolma",fg="#EEEEEE",bg="grey10")
        self.dolma.place(x=450,y=180)
        self.dolmaEntry = Entry(self.pencere,bg="lavender",bd=5, relief=RAISED)
        self.dolmaEntry.insert(0, "0")
        self.dolmaEntry.place(x=550,y=180)
        
        
# Alınan ürünleri adetine göre hesaplama işlemlerini yapıyorum.
    def hesapla(self):                
        self.hesap=0
        
        self.hesap+=int(self.pilavEntry.get())*10
        self.hesap+=int(self.makarnaEntry.get())*10
        self.hesap+=int(self.koftelerEntry.get())*15
        self.hesap+=int(self.tavukEntry.get())*15
        self.hesap+=int(self.fasulyeEntry.get())*12
        self.hesap+=int(self.mantiEntry.get())*8
        self.hesap+=int(self.salataEntry.get())*5
        self.hesap+=int(self.borekEntry.get())*7
        self.hesap+=int(self.karniyarikEntry.get())*10
        self.hesap+=int(self.kolaEntry.get())*5
        self.hesap+=int(self.fantaEntry.get())*5
        self.hesap+=int(self.ayranEntry.get())*3
        self.hesap+=int(self.suEntry.get())*2
        self.hesap+=int(self.madensuyuEntry.get())*3
        self.hesap+=int(self.humusEntry.get())*10
        self.hesap+=int(self.cacikEntry.get())*8
        self.hesap+=int(self.kisirEntry.get())*7
        self.hesap+=int(self.dolmaEntry.get())*10
        
        self.buton = Button(self.pencere,text="Hesapla",command=self.hesapla,width=28,height=1,font=1, bd=2, relief=RAISED,fg="grey10",bg="#EEEEEE")
        self.buton.place(x=450,y=500)
        self.toplamhepsi = Label(self.pencere,text="Toplam Hesap:"+str(self.hesap)+"TL",font=("Arial",20,"bold","underline"),fg="#EEEEEE",bg="grey10")
        self.toplamhepsi.place(x=450,y=450)
    
# Hesaplanan ürünleri fiş olarak kaydediyorum.
    def fis(self):
        with open("fis.txt","w") as file:
            file.write (str(self.toplamhepsi.cget("text")))
                
        self.fis = Button(self.pencere,text="Fiş",command=self.fis,width=28,height=1,font=1, bd=2, relief=RAISED,fg="grey10",bg="#EEEEEE")
        self.fis.place(x=450,y=550)
    

Restoran = Odev()
Restoran.pencere.mainloop()
