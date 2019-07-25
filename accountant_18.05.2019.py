#!/usr/bin/env python
# -*-coding:utf8-*-
from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter import StringVar
from tkinter.ttk import Entry, Label
from tkinter import ttk
import tkinter.font
import time


global ekle1
global ekle2
global ekle3
global ekle4
global ekle5
global ekle6
global ekle7

pencere = Tk()

pencere.title("MUHASEBE PROGRAMI BULENT V.1")
pencere.config(background="red")
pencere.resizable(0,0)

#frame = ttk.Frame(pencere)
#frame.pack()
#frame.config(height = 10, width = 10)
#frame.grid(row = 0 , column = 0)
#photo = PhotoImage(file="Ets_Logo.png")
#etiket = Label(pencere, image=photo)
#etiket.grid()
#frame = Tk.Frame(pencere)
#frame.grid()
#frame.config(height =200, width = 500)
#frame.config(relief = RIDGE)
#ttk.Button(frame, text = 'Click Me').pack()
#frame.config(padding = (100, 50))
#ttk.LabelFrame(pencere, height = 2000, width = 200, text = 'My Frame').grid()


Musteri_unvani = Label(pencere)  # company namep
etiket1 = Label(text="Lütfen Müşteri Ünvanını Giriniz!", background="Navy Blue", foreground="yellow")
etiket1.grid(row=1, column=0)
Musteri_unvani = Entry()
Musteri_unvani.grid(row=1, column=1)

Vergi_no = Label(pencere)  # VAT Number
etiket8 = Label(text="Lütfen Vergi Numarasını Giriniz!", background="Navy Blue", foreground="yellow")
etiket8.grid(row=2, column=0)
Vergi_no = Entry()
Vergi_no.grid(row=2, column=1)

Fatura_no = Label(pencere)  # Invoice number
etiket2 = Label(text="Lütfen Fatura Numarasını Giriniz!", background="Navy Blue", foreground="yellow")
etiket2.grid(row=3, column=0)
Fatura_no = Entry()
Fatura_no.grid(row=3, column=1)

Fatura_tarihi = Label(pencere)  # Invoice date
etiket3 = Label(text="Lütfen Fatura Tarihini Giriniz!", background="Navy Blue", foreground="yellow")
etiket3.grid(row=4, column=0)
Fatura_tarihi = Entry()
Fatura_tarihi.grid(row=4, column=1)

category = {'ALIM': [1, 8, 18], 'SATIM': [1, 8, 18], 'ALIM İADE': [1, 8, 18], 'SATIM İADE': [1, 8, 18],
            'TEVKİFAT KDV': [9 / 10]}


# ========================
# search fucntion to search value inside search box
def search():
    value = search_f.get()

    #     db op's
    baglanti = sqlite3.connect('accounting.db')
    veritabani_sec = baglanti.cursor()

    veritabani_sec.execute("SELECT musteri_unvani , fatura_no   FROM  accountant WHERE musteri_unvani=?", (value,))

    for row in veritabani_sec.fetchall():
        listbox.insert(END, row[0], row[1])


# ==========================
def kdv_total():
    value = search_f1.get()
    baglanti = sqlite3.connect('accounting.db')
    veritabani_sec = baglanti.cursor()
    veritabani_sec.execute("SELECT Fatura_Turu as FATURA_TURU, SUM(Kdv_tutari) as KDV_TUTARI FROM  accountant GROUP BY Fatura_Turu")

    for row in veritabani_sec.fetchall():
        listbox1.insert(END, row)


def getUpdate(event):
    box2['values'] = category[(box1.get())]


Fatura_turu = Label(pencere)
etiket4 = Label(text="Lütfen Fatura Türünü Seçiniz!", background="Navy Blue", foreground="yellow")
etiket4.grid(row=5, column=0)
value = StringVar()
box1 = Combobox(pencere, textvariable=value, width=17, state='readonly')
box1['values'] = list(category.keys())
box1.bind('<<ComboboxSelected>>', getUpdate)
box1.current(0)
box1.grid(row=5, column=1)

Tutar = Label(pencere)
etiket5 = Label(text="Lütfen Tutarı Giriniz!", background="Navy Blue", foreground="yellow")
etiket5.grid(row=6, column=0)
Tutar = Entry()
Tutar.grid(row=6, column=1)

Kdv_orani = Label(pencere)
etiket6 = Label(text="Lütfen KDV oranını Seçiniz!", background="Navy Blue", foreground="yellow")  # type: Label
etiket6.grid(row=7, column=0)
box2 = Combobox(pencere,width=17)
box2.grid(row=7, column=1)

Kdv_tutari = Label(pencere)
etiket9 = Label(text="Lütfen KDV tutarını Giriniz!", background="Navy Blue", foreground="yellow")
etiket9.grid(row=8, column=0)
Kdv_tutari = Entry()
Kdv_tutari.grid(row=8, column=1)

Toplam = Label(pencere)
etiket7 = Label(text="Lütfen Fatura Toplamını Giriniz!", background="Navy Blue", foreground="yellow")
etiket7.grid(row=9, column=0)
Toplam = Entry()
Toplam.grid(row=9, column=1)

Odeme_vadesi = Label(pencere)
etiket10 = Label(text="Lütfen Ödeme Vadesini  Giriniz!", background="Navy Blue", foreground="yellow")
etiket10.grid(row=10, column=0)
Odeme_vadesi = Entry()
Odeme_vadesi.grid(row=10, column=1)



# ==========================
# search label
search_label = Label(text="Müşteri Arama!", background="Navy Blue", foreground="yellow")
search_label.grid(row=21, column=0)

# ==========================
# search label
search_label2 = Label(text="KDV Toplamı!", background="Navy Blue", foreground="yellow")
search_label2.grid(row=22, column=1)

# ==========================
# search label
search_label2 = Label(text="Ödeme Vadesi!", background="Navy Blue", foreground="yellow")
search_label2.grid(row=22, column=2)





# =======================
# Search box to search something
search_f = Entry(pencere)
#search_f.place(x=0, y=0)
search_f.grid(row=21, column=0)
# Search button to run search function
search_button = Button(pencere, text="Müşteri Ara", command=search)
search_button.grid(row=22, column=0)

# Search button to run search function
# Search box to search something
search_f1 = Entry(pencere)
#search_f.place(x=0, y=0)
search_f1.grid(row=21, column=1)
# Search button to run search function
search_button = Button(pencere, text="Kdv Total", command=kdv_total)
search_button.grid(row=22, column=1)

search_f2 = Entry(pencere)
#search_f.place(x=0, y=0)
search_f2.grid(row=21, column=2)
# Search button to run search function
search_button = Button(pencere, text="Ödeme Vadesi", command=Odeme_vadesi)
search_button.grid(row=22, column=2)

# ========================


def database():
    # calculate the value of Kdv_Tutari here
    Kdv_tutari.delete(0, 'end')
    kdv_tutari = 0
    tutar = float(Tutar.get())
    kdv_orani = float(box2.get())
    kdv_tutari = (tutar * (kdv_orani / 100))
    Kdv_tutari.insert(0, str(kdv_tutari))

    # calculate the value of toplam here
    Toplam.delete(0, 'end')
    toplam = 0
    tutar = float(Tutar.get())
    kdv_orani = float(box2.get())
    toplam = tutar + (tutar * (kdv_orani / 100))
    Toplam.insert(0, str(toplam))

    baglanti = sqlite3.connect('accounting.db')
    if (baglanti):
        print('Baglanti Basarili!')
    else:
        print('Baglanti Basarisiz!')

    veritabani_sec = baglanti.cursor()

    ekle1 = Musteri_unvani.get()
    ekle2 = Fatura_no.get()
    ekle3 = Fatura_tarihi.get()
    ekle4 = box1.get()
    ekle5 = float(Tutar.get())
    ekle6 = float(box2.get())
    ekle7 = float(Toplam.get())
    ekle8 = Vergi_no.get()
    ekle9 = Kdv_tutari.get()
    ekle10 = Odeme_vadesi.get()

    # seçili veritabanına veri ekliyoruz.
    veritabani_sec.execute(
        """INSERT INTO accountant VALUES ('""" + str(ekle1) + """','""" + str(ekle2) + """','""" + str(
            ekle8) + """','""" + str(ekle3) + """','""" + str(ekle4) + """','""" + str(ekle5) + """','""" + str(
            ekle6) + """','""" + str(ekle7) + """','""" + str(ekle9) + """' ,'""" + str(ekle10) + """')""")
    baglanti.commit()
    baglanti.close()


listbox = 0
#listbox = Listbox(background="Grey", width=50, height=25)
listbox= Listbox(background="Grey")
#listbox.place(relx=0.095, rely=0.001)
listbox.grid(row=20, column=0)

# scrollbar = Scrollbar(orient="vertical",command=listbox.yview)
# scrollbar.pack(side="right", fill="y")

# listbox.config(yscrollcommand=scrollbar.set)

listbox1 = 0
listbox1 = Listbox(background="Grey")
#listbox1.place(relx=0.240, rely=0.001)
listbox1.grid(row=20, column=1)

listbox3 = 0
listbox3 = Listbox(background="Grey")
#listbox1.place(relx=0.240, rely=0.001)
listbox3.grid(row=20, column=2)

# scrollbar = Scrollbar(orient="vertical",command=listbox.yview)
# scrollbar.pack(side="right", fill="y")

# listbox1.config(yscrollcommand=scrollbar.set)


def View():
    baglanti = sqlite3.connect('accounting.db')
    veritabani_sec = baglanti.cursor()
    veritabani_sec.execute("SELECT * FROM  accountant")
    for row in veritabani_sec.fetchall():
        listbox.insert(END, row[0], row[2])


def Kdv_View():
    baglanti = sqlite3.connect('accounting.db')
    veritabani_sec = baglanti.cursor()
    veritabani_sec.execute("SELECT Fatura_Turu, SUM(Kdv_tutari) FROM  accountant GROUP BY ROLLUP")
    for row in veritabani_sec.fetchall():
        listbox1.insert(END, row[4], row[7])

def Odeme_View():
    value=search_f2.get()
    baglanti = sqlite3.connect('accounting.db')
    veritabani_sec = baglanti.cursor()
    veritabani_sec.execute("SELECT * FROM  accountant Where (Odeme_vadesi date >='2015-01-01' AND date<='2019-07-01')")
    for row in veritabani_sec.fetchall():
        listbox3.insert(END, row[10])



dugme1 = Button(pencere)
dugme1.config(text="Kaydet")
dugme1.config(command=database)
dugme1.grid(row = 18,column = 1)


pencere.mainloop()
