# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:28:11 2019

@author: HOLGADOS
"""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from math import *

monit_path = 'd:/monitorizadas.txt'
nomonit_path = 'd:/no_monitorizadas.txt'
rutas_bas = 'd:/rutas_bas_2.txt'

class Centrales:
    def __init__(self):
        self.nom = []
        self.abr = []
        self.tecnica = []
        self.cnt = 0
        
        with open(monit_path,'r') as fp:  
            line = fp.readline()
            self.cnt = 1
            while line:
                self.abr.append(line[0:line.find(",")])
                self.nom.append(line[len(self.abr[self.cnt-1])+1:line.find(",",len(self.abr[self.cnt-1])+1)])
                self.tecnica.append(line[len(self.abr[self.cnt-1])+len(self.nom[self.cnt-1])+2:line.find(",",len(self.abr[self.cnt-1])+len(self.nom[self.cnt-1])+2)])
                line = fp.readline()
                self.cnt+=1
        
    def es_nodo(self,cual):
        print("entro en es_nodo, consultando:" + cual)

    def es_SBC(self,cual):
        if self.abr[int(cual)]=="SBC":
            return True
        else:
            return False
        print("entro en es_SBC, consultando:" + cual)

    def buscar_abr(self,cual):
        for i in range(self.cnt):
            if self.nom[i]==cual:
                return self.abr[i]
    
    def que_ABR(self,cual):
        return self.abr[int(cual)]

    def cantidad(self):
        return self.cnt-1
    
    def es_AS(self):
        for i in range(40):
            print (self)


class Centrales_NoMonit:
    def __init__(self):
        self.nom = []
        self.abr = []
        self.clave = []
        self.cnt = 0
        
        with open(nomonit_path,'r') as fp:  
            line = fp.readline()
            self.cnt = 1
            while line:
                self.clave.append(line[0:line.find(",")])
                self.abr.append(line[len(self.clave[self.cnt-1])+1:line.find(",",len(self.clave[self.cnt-1])+1)])
                self.nom.append(line[len(self.clave[self.cnt-1])+len(self.abr[self.cnt-1])+2:line.find(",",len(self.clave[self.cnt-1])+len(self.abr[self.cnt-1])+2)])
                line = fp.readline()
                self.cnt+=1
    def buscar_abr(self,cual):
        for i in range(self.cnt):
            if self.nom[i]==cual:
                return self.clave[i]

class Rutas_Bas:
    def __init__(self):
        self.nom = []
        self.abr = []
        self.clave = []
        
        self.cnt = 0
        
        self.Central_Extremo = []
        self.Clave_extremo = []
        self.Tipo_Ruta = []
        self.Tipo_Ruta_I = []
        self.Algoritmo_ruta_basica_asignado = []
        self.Algoritmo_ruta_basica_defecto = []
        self.Id_entrada_numerico = []
        self.Id_entrada_textual = []
        self.Id_salida_numerico = []
        self.Id_salida_textual = []

        
        with open(rutas_bas,'r') as fp:  
            line = fp.readline()
            self.cnt = 0
            while line:
                pos1=0
                pos2=line.find(";")
                self.Central_Extremo.append(line[pos1:pos2])
                print(self.Central_Extremo[self.cnt] + str(pos1) + "*" + str(pos2))
                pos1+=len(self.Central_Extremo[self.cnt])+1
                pos2=line.find(";",pos1)
                self.Clave_extremo.append(line[pos1:pos2])
                print(self.Clave_extremo[self.cnt] + str(pos1) + "*" + str(pos2))
                pos1+=len(self.Clave_extremo[self.cnt])+1
                pos2=line.find(";",pos1)
                self.Tipo_Ruta.append(line[pos1:pos2])
                print(self.Tipo_Ruta[self.cnt] + str(pos1) + "*" + str(pos2))
                pos1+=len(self.Tipo_Ruta[self.cnt])+1
                pos2=line.find(";",pos1)
                self.Tipo_Ruta_I.append(line[pos1:pos2])
                print(self.Tipo_Ruta_I[self.cnt] + str(pos1) + "*" + str(pos2))
                pos1+=len(self.Tipo_Ruta_I[self.cnt])+1
                pos2=line.find(";",pos1)
                self.Algoritmo_ruta_basica_asignado.append(line[pos1:pos2])
                print(self.Algoritmo_ruta_basica_asignado[self.cnt] + str(pos1) + "*" + str(pos2))
                pos1+=len(self.Algoritmo_ruta_basica_asignado[self.cnt])+1
                pos2=line.find(";",pos1)
                self.Algoritmo_ruta_basica_defecto.append(line[pos1:pos2])
                print(self.Algoritmo_ruta_basica_defecto[self.cnt] + str(pos1) + "*" + str(pos2))
                pos1+=len(self.Algoritmo_ruta_basica_defecto[self.cnt])+1
                pos2=line.find(";",pos1)
                self.Id_entrada_numerico.append(line[pos1:pos2])
                print(self.Id_entrada_numerico[self.cnt] + str(pos1) + "*" + str(pos2))
                pos1+=len(self.Id_entrada_numerico[self.cnt])+1
                pos2=line.find(";",pos1)
                self.Id_entrada_textual.append(line[pos1:pos2])
                print(self.Id_entrada_textual[self.cnt] + str(pos1) + "*" + str(pos2))
                pos1+=len(self.Id_entrada_textual[self.cnt])+1
                pos2=line.find(";",pos1)
                self.Id_salida_numerico.append(line[pos1:pos2])
                print(self.Id_salida_numerico[self.cnt] + str(pos1) + "*" + str(pos2))
                pos1+=len(self.Id_salida_numerico[self.cnt])+1
                pos2=line.find(";",pos1)
                self.Id_salida_textual.append(line[pos1:pos2])
                print(self.Id_salida_textual[self.cnt] + str(pos1) + "*" + str(pos2))
                
                #print (self.Central_Extremo[self.cnt] + "-" + self.Clave_extremo[self.cnt] +"-" + self.Tipo_Ruta[self.cnt] +"\n")
                line = fp.readline()
                self.cnt+=1
    


class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        
        self.raiz.geometry('1000x500')
        
        self.raiz.resizable(width=True,height=True)
        self.raiz.title('Netmas Controller')
        self.raiz.bind("<Configure>",self.resizeEvent)
        
        #crea menus
        
        menubar = Menu(self.raiz)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Central No_Monit", command=self.hello)
        filemenu.add_command(label="Ruta SGT", command=self.alta_sgt)
        filemenu.add_command(label="Ruta BAS", command=self.alta_bas)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.raiz.destroy)
        menubar.add_cascade(label="Alta", menu=filemenu)

        # create more pulldown menus
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Central No_Monit", command=self.baja_cent_no_monit)
        editmenu.add_command(label="Ruta SGT", command=self.hello)
        editmenu.add_command(label="Ruta BAS", command=self.hello)
        menubar.add_cascade(label="Baja", menu=editmenu)

# create more pulldown menus
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Central No_Monit", command=self.hello)
        editmenu.add_command(label="Ruta SGT", command=self.hello)
        editmenu.add_command(label="Ruta BAS", command=self.hello)
        menubar.add_cascade(label="Modificacion", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Manual", command=self.hello)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)


        self.raiz.config(menu=menubar)
        #fin crea menus
        
        self.centrales=Centrales()
        self.centrales_nomonit=Centrales_NoMonit()
        self.rutas_basicas=Rutas_Bas()
        
        #Ûself.binfo.pack(side=LEFT)
        
        #print (self.raiz.winfo_height())
        
        self.bsalir = ttk.Button(self.raiz, text='Salir', command=self.raiz.destroy)
        self.bsalir.place(x=1000*.91,y=500*.95)                                 
        
        
        
        self.raiz.mainloop()
    
    def resizeEvent(self,event):
        print("cambio de tamaño" + str(self.raiz.winfo_height()))
    
    def alta_sgt(self):
        self.tipo=0
        self.lab1 = Label(self.raiz,text="Seleccione Extremo Origen")
        self.lab1.place(x=10,y=20)
        self.cb = ttk.Combobox(self.raiz,state='readonly')
        self.cb['values']=self.centrales.nom
        self.cb.current(0)
        self.cb.place(x=10,y=40,width=220)
        self.cb.bind("<<ComboboxSelected>>",self.cambio)
        self.lab2 = Label(self.raiz,text="Seleccione Extremo Destino")
        self.lab2.place(x=10,y=60)
        self.cb2 = ttk.Combobox(self.raiz,state='readonly')
        self.cb2['values']=self.centrales_nomonit.nom
        self.cb2.current(0)
        self.cb2.place(x=10,y=80,width=220)
        self.tb = Text(self.raiz,height=20,width=80)
        self.tb.place(x=240,y=20,height=400)
        self.binfo = ttk.Button(self.raiz, text='Generar texto', command=self.verinfo)
        self.binfo.place(x=10,y=500*.95)
        self.binfo.focus_set()
        
    def alta_bas(self):
        self.area = Canvas(self.raiz,width=1000, height=620,background="#AAAAAA")
        self.area.pack(side=TOP)
        self.area.lab1 = Label(self.raiz,text="Seleccione Extremo Origen")
        self.area.lab1.place(x=10,y=20)
        self.area.cb = ttk.Combobox(self.raiz,state='readonly')
        self.area.cb['values']=self.centrales.nom
        self.area.cb.current(0)
        self.area.cb.place(x=10,y=40,width=220)
        self.area.cb.bind("<<ComboboxSelected>>",self.cambio)



    
    def cambio(self,event):
        if self.tipo!=0:
            self.lab3.destroy()
            self.entrada1.destroy()
            
            if self.tipo==3:
                self.lab4.destroy()
                self.entrada2.destroy()
                self.lab5.destroy()
                self.entrada3.destroy()
                self.lab6.destroy()
                self.entrada4.destroy()
            if self.tipo==4:
                self.lab4.destroy()
                self.entrada2.destroy()
        
        if self.centrales.tecnica[self.cb.current()]=="EWSD":
            self.tipo=1
            self.lab3 = Label(self.raiz,text="Ingrese Nombre de Ruta")
            self.lab3.place(x=10,y=100)
            self.entrada1 = Entry(self.raiz)
            self.entrada1.place(x=10,y=120)
            #RUTA_BAS 'B-UMG89-WLD' BIDIREC >> 'BUMWLD'
        elif self.centrales.tecnica[self.cb.current()]=="NEAX61E":
            self.tipo=2
            self.lab3 = Label(self.raiz,text="Ingrese Nombre de Ruta")
            self.lab3.place(x=10,y=100)
            self.entrada1 = Entry(self.raiz)
            self.entrada1.place(x=10,y=120)
            #RUTA_BAS 'BCF-VISA' BIDIREC >> 'BPMP'  << 'BPMP'
        elif self.centrales.tecnica[self.cb.current()]=="AXE":
            self.tipo=3
            self.lab3 = Label(self.raiz,text="Ingrese Ruta Saliente")
            self.lab3.place(x=10,y=100)
            self.lab4 = Label(self.raiz,text="RNO")
            self.lab4.place(x=140,y=100)
            self.entrada1 = Entry(self.raiz)
            self.entrada1.place(x=10,y=120)
            self.entrada2 = Entry(self.raiz)
            self.entrada2.place(x=140,y=120,width=50)
            self.lab5 = Label(self.raiz,text="Ingrese Ruta Entrante")
            self.lab5.place(x=10,y=140)
            self.lab6 = Label(self.raiz,text="RNO")
            self.lab6.place(x=140,y=140)
            self.entrada3 = Entry(self.raiz)
            self.entrada3.place(x=10,y=160)
            self.entrada4 = Entry(self.raiz)
            self.entrada4.place(x=140,y=160,width=50)
            #RUTA_BAS 'BS9-SALT-PRG' BIDIREC >> 'OSCELJ' (2456) << 'ISCELJ' (2457)
        elif self.centrales.tecnica[self.cb.current()]=="S12":
            self.tipo=4
            self.lab3 = Label(self.raiz,text="Ingrese Ruta")
            self.lab3.place(x=10,y=100)
            self.lab4 = Label(self.raiz,text="TKG")
            self.lab4.place(x=140,y=100)
            self.entrada1 = Entry(self.raiz)
            self.entrada1.place(x=10,y=120)
            self.entrada2 = Entry(self.raiz)
            self.entrada2.place(x=140,y=120,width=50)
            #RUTA_BAS 'B-UMG89-MRM' BIDIREC >> 'BUMMRM' (00035)
        elif self.centrales.tecnica[self.cb.current()]=="HUAWEI":
            self.tipo=5

    
    def verinfo(self):
        
        #self.tinfo.delete("1.0", END)
        #self.area.delete("all")
        self.tb.delete(1.0, END)
        texto=""
        central=self.centrales.buscar_abr(self.cb.get())
        central2=self.centrales_nomonit.buscar_abr(self.cb2.get())
        texto += "ALTA RUTA_SGT '" + central + "_" + central2 + "'\nEXTREMO '" + central2 + "'\nEXTREMO '" + central
        tiporuta= central2[-3:]
        texto += "'\nRUTA_BAS 'B-UMG89-" + tiporuta + "' BIDIREC "
        if self.tipo==1:
            texto += ">> '" + self.entrada1.get() + "'"
        elif self.tipo==2:
            texto += ">> '" + self.entrada1.get() + "' << '" + self.entrada1.get() + "'"
        elif self.tipo==3:
            texto += ">> '" + self.entrada1.get() + "' (" + self.entrada2.get() + ") << '" + self.entrada3.get() + "' (" + self.entrada4.get() + ")"
        elif self.tipo==4:
            texto += ">> '" + self.entrada1.get() + "' (" + self.entrada2.get() +")"
        texto += "\nALGORITMO POR DEFECTO 'alg2_NGN'"
        self.tb.insert(END,texto)
        self.binfo.place(x=10,y=self.raiz.winfo_height()*.95)
        #print (self.raiz.winfo_height())
        
    def baja_cent_no_monit(self):
        self.lab2 = Label(self.raiz,text="Seleccione Extremo Destino")
        self.lab2.place(x=10,y=60)
        self.cb2 = ttk.Combobox(self.raiz,state='readonly')
        self.cb2['values']=self.centrales_nomonit.nom
        self.cb2.current(0)
        self.cb2.place(x=10,y=80,width=220)
        self.tb = Text(self.raiz,height=20,width=80)
        self.tb.place(x=240,y=20,height=400)
        
    def hello(self):
        print ("hello!")


   
def main():

    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()