# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:03:27 2020

@author: Samsung
"""
import numpy as np        
###IMPORTANDO LA LIBRERIA NUMPY PARA LAS MATRICES###

def buscarAgregar(lista,elemento):
    ###FUNCION PARA IR AGREGANDO FILAS Y COLUMNAS A LA MATRIZ###
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

def mayorDia(pacientes):
    ###FUNCION PARA OBTENER EL MAYOR DIA DEL ARCHIVO###
    archivo= open(pacientes,"r")
    diaMayor= 0
    dias= []
    linea= archivo.readline().strip()
    while linea != "":
        partes= linea.split(";")
        diaContagio= int(partes[1])
        if diaContagio >= 0:
            dias.append(diaContagio)
        for i in range(len(dias)):
            if dias[i] > diaMayor:
                diaMayor= dias[i]
        linea= archivo.readline().strip()
    return diaMayor        
            
def chinos(pacientes):
    ###FUNCION PARA OBTENER LA CANTIDAD DE CHINOS HOMBRES Y MUJERES###
    masculinoChina= 0
    femeninoChina= 0
    masculinoHK= 0
    femeninoHK= 0
    archivo= open(pacientes, "r")
    linea= archivo.readline().strip()
    while linea != "":
        partes= linea.split(";")
        pais= partes[2]
        genero= partes[3]
          
        if genero == "masculino" and pais == "China":
            masculinoChina += 1
        if genero == "femenino" and pais == "China":
            femeninoChina += 1
        if genero == "masculino" and pais == "Hong Kong":
            masculinoHK += 1
        if genero == "femenino" and pais == "Hong Kong":
            femeninoHK += 1
        linea= archivo.readline().strip()
    ###OBTENIENDO LA CANTIDAD DE CONTAGIADOS POR GENERO EN CHINA###
    return masculinoChina,femeninoChina,masculinoHK,femeninoHK


def rangoEtario(pacientes):
    ###OBTENIENDO EL RANGO ETARIO CON UNA FUNCIÓN###
    archivo2= open(pacientes, "r")
    linea2= archivo2.readline().strip()
    rango1= 0      #entre 1 y 10 años#
    rango2= 0      #entre 11 y 20 años#
    rango3= 0      #entre 21 y 30 años#
    rango4= 0      #entre 31 y 40 años#
    rango5= 0      #entre 41 y 50 años#
    rango6= 0      #entre 51 y 60 años#
    rango7= 0      #entre 61 y 70 años#
    rango8= 0      #entre 71 y 80 años#
    rango9= 0      #entre 81 y 90 años#
    rango10= 0     #entre 91 y 100 años#
    rangoMayorNumero= 0
    rangoMayor= ""
    rangosTotal= ["rango1", "rango2", "rango3", "rango4", "rango5", "rango6", "rango7", "rango8", "rango9", "rango10"]
    while linea2 != "":
        partes2= linea2.split(";")
        edad2= int(partes2[4])
        
        if edad2 >= 1 and edad2 <= 10:
            rango1 += 1
        if edad2 > 10 and edad2 <= 20:
            rango2 += 1
        if edad2 > 20 and edad2 <= 30:
            rango3 += 1
        if edad2 > 30 and edad2 <= 40:
            rango4 += 1
        if edad2 > 40 and edad2 <= 50:
            rango5 += 1
        if edad2 > 50 and edad2 <= 60:
            rango6 += 1
        if edad2 > 60 and edad2 <= 70:
            rango7 += 1
        if edad2 > 70 and edad2 <= 80:
            rango8 += 1
        if edad2 > 80 and edad2 <= 90:
            rango9 += 1
        if edad2 > 90 and edad2 <= 100:
            rango10 += 1
            
        rangos= []
        ###LISTA PARA LOS RANGOS ETARIOS###
        rango1Total= rango1 + rango1Manual
        rango2Total= rango2 + rango2Manual
        rango3Total= rango3 + rango3Manual
        rango4Total= rango4 + rango4Manual
        rango5Total= rango5 + rango5Manual
        rango6Total= rango6 + rango6Manual
        rango7Total= rango7 + rango7Manual
        rango8Total= rango8 + rango8Manual
        rango9Total= rango9 + rango9Manual
        rango10Total= rango10 + rango10Manual
        rangos.append(rango1Total)
        rangos.append(rango2Total)
        rangos.append(rango3Total)
        rangos.append(rango4Total)
        rangos.append(rango5Total)
        rangos.append(rango6Total)
        rangos.append(rango7Total)
        rangos.append(rango8Total)
        rangos.append(rango9Total)
        rangos.append(rango10Total)
        
        for i in range(len(rangos)):
            ###OBTENIENDO EL RANGO ETARIO CON MAYOR CONTAGIADOS###
            if rangos[i] > rangoMayorNumero:
                rangoMayorNumero = rangos[i]
                rangoMayor = rangosTotal[i]
        linea2= archivo2.readline().strip()       
    return print("El rango etario con más contagiados es: ", rangoMayor, "con: ", rangoMayorNumero, "personas")


def contagiosDiaMayor(pacientes):
    ###FUNCION PARA OBTENER EL DIA DONDE HAY MAS CONTAGIADOS###
    archivo= open(pacientes, "r")
    linea= archivo.readline().strip()
    dias= []
    paises= []
    matriz= np.zeros([200,200])
    mayor= 0
    mayorDia= ""
    while linea != "":
        partes= linea.split(";")
        diaContagio= int(partes[1])
        pais= partes[2]
        columna= buscarAgregar(dias,diaContagio)
        fila= buscarAgregar(paises,pais)
        matriz[fila][columna] = matriz[fila][columna] + 1
        linea= archivo.readline().strip()
    
    cantidadDias= len(dias)
    cantidadPaises= len(paises)
    totalPorPais= []
    diaNumeros= ["Dia21","Dia22","Dia23","Dia24","Dia25","Dia26","Dia27","Dia28","Dia29","Dia0","Dia2","Dia4","Dia7","Dia8","Dia9","Dia10","Dia11","Dia12","Dia13","Dia14","Dia15","Dia16","Dia17","Dia18","Dia30","Dia31","Dia32","Dia33","Dia34","Dia35","Dia36","Dia37","Dia38","Dia39","Dia40","Dia41","Dia42","Dia43","Dia44","Dia45"]
    ###CONVIRTIENDO LA MATRIZ EN LISTAS###
    for i in range(cantidadDias):
        sumaVisitasEnEstePais = 0

        for j in range(cantidadPaises):
            sumaVisitasEnEstePais += matriz[j][i]
        totalPorPais.append(sumaVisitasEnEstePais)
    ###ORDENANDO LAS LISTAS###
    for a in range(len(totalPorPais) -1):
        for b in range(a+1, len(totalPorPais)):
            if totalPorPais[a] > totalPorPais[b]:
                aux= totalPorPais[a]
                totalPorPais[a]= totalPorPais[b]
                totalPorPais[b]= aux
                           
                aux= diaNumeros[a]
                diaNumeros[a]= diaNumeros[b]
                diaNumeros[b]= aux
     ###OBTENIENDO EL DIA EN EL QUE SE ENFERMARON MAS PERSONAS###           
    for i in range(cantidadDias):
        if totalPorPais[i] > mayor:
            mayor = totalPorPais[i]
            mayorDia= diaNumeros[i]
    return print("El dia donde se produjeron más contagiados fue el dia: ", mayorDia, "con: ", mayor, "personas contagiadas")
    
def rangoEtarioPorPais(pacientes):
    ###OBTENIENDO EL RANGO ETARIO POR CADA PAIS EN UNA FUNCIÓN###
    archivo= open(pacientes, "r")
    matriz0= np.zeros([1100,1100])
    matriz1= np.zeros([1100,1100])
    matriz2= np.zeros([1100,1100])
    matriz3= np.zeros([1100,1100])
    matriz4= np.zeros([1100,1100])
    matriz5= np.zeros([1100,1100])
    matriz6= np.zeros([1100,1100])
    matriz7= np.zeros([1100,1100])
    matriz8= np.zeros([1100,1100])
    matriz9= np.zeros([1100,1100])
    matriz10= np.zeros([1100,1100])
    ###CONSTRUYENDO LAS MATRICES CON CEROS###
    linea= archivo.readline().strip()
    paises= []
    edades= []
    totalPais= []
    mayor= 0
    indiceMayor= -1
    rango1= 0      
    rango2= 0      
    rango3= 0
    rango4= 0
    rango5= 0      
    rango6= 0      ###CONTADORES###
    rango7= 0      
    rango8= 0      
    rango9= 0      
    rango10= 0
    continuar= "Si"
    while linea != "":
        partes= linea.split(";")
        pais= partes[2]
        edad= int(partes[4])
        columna0= buscarAgregar(paises,pais)
        fila0= buscarAgregar(edades,edad)
        matriz0[fila0][columna0] = matriz0[fila0][columna0] + 1
        if edad >= 1 and edad <= 10:
            ###MATRIZ NUMERO 1###
            rango1 += 1
            rango1Total= rango1 + rango1Manual
            rangos1= []
            columna1= buscarAgregar(paises,pais)
            fila1= buscarAgregar(rangos1,rango1Total)
            matriz1[fila1][columna1] = matriz1[fila1][columna1] + 1
        if edad > 10 and edad <= 20:
            ###MATRIZ NUMERO 2###
            rango2 += 1
            rango2Total= rango2 + rango2Manual
            rangos2= []
            columna2= buscarAgregar(paises,pais)
            fila2= buscarAgregar(rangos2,rango2Total)
            matriz2[fila2][columna2] = matriz2[fila2][columna2] + 1
        if edad > 20 and edad <= 30:
            ###MATRIZ NUMERO 3###
            rango3 += 1
            rango3Total= rango3 + rango3Manual
            rangos3= []
            columna3= buscarAgregar(paises,pais)
            fila3= buscarAgregar(rangos3,rango3Total)
            matriz3[fila3][columna3] = matriz3[fila3][columna3] + 1
        if edad > 30 and edad <= 40:
            ###MATRIZ NUMERO 4###
            rango4 += 1
            rango4Total= rango4 + rango4Manual
            rangos4= []
            columna4= buscarAgregar(paises,pais)
            fila4= buscarAgregar(rangos4,rango4Total)
            matriz4[fila4][columna4] = matriz4[fila4][columna4] + 1
        if edad > 40 and edad <= 50:
            ###MATRIZ NUMERO 5###
            rango5 += 1
            rango5Total= rango5 + rango5Manual
            rangos5= []
            columna5= buscarAgregar(paises,pais)
            fila5= buscarAgregar(rangos5,rango5Total)
            matriz5[fila5][columna5] = matriz5[fila5][columna5] + 1
        if edad > 50 and edad <= 60:
            #MATRIZ NUMERO 6###
            rango6 += 1
            rango6Total= rango6 + rango6Manual
            rangos6= []
            columna6= buscarAgregar(paises,pais)
            fila6= buscarAgregar(rangos6,rango6Total)
            matriz6[fila6][columna6] = matriz6[fila6][columna6] + 1
        if edad > 60 and edad <= 70:
            ###MATRIZ NUMERO 7###
            rango7 += 1
            rango7Total= rango7 + rango7Manual
            rangos7= []
            columna7= buscarAgregar(paises,pais)
            fila7= buscarAgregar(rangos7,rango7Total)
            matriz7[fila7][columna7] = matriz7[fila7][columna7] + 1
        if edad > 70 and edad <= 80:
            ###MATRIZ NUMERO 8###
            rango8 += 1
            rango8Total= rango8 + rango8Manual
            rangos8= []
            columna8= buscarAgregar(paises,pais)
            fila8= buscarAgregar(rangos8,rango8Total)
            matriz8[fila8][columna8] = matriz8[fila8][columna8] + 1
        if edad > 80 and edad <= 90:
            ###MATRIZ NUMERO 9###
            rango9 += 1
            rango9Total= rango9 + rango9Manual
            rangos9= []
            columna9= buscarAgregar(paises,pais)
            fila9= buscarAgregar(rangos9,rango9Total)
            matriz9[fila9][columna9] = matriz9[fila9][columna9] + 1
        if edad > 90 and edad <= 100:
            ###MATRIZ NUMERO10###
            rango10 += 1
            rango10Total= rango10 + rango10Manual
            rangos10= []
            columna10= buscarAgregar(paises,pais)
            fila10= buscarAgregar(rangos10,rango10Total)
            matriz10[fila10][columna10] = matriz10[fila10][columna10] + 1
        linea= archivo.readline().strip()
    ###OBTENIENDO EL PAIS CON MÁS CONTAGIADOS Y SUS RANGOS ETARIOS###
    for i in range(len(paises)):
        visitasPais = 0
        
        for j in range(len(edades)):
            visitasPais += matriz0[j][i]
        totalPais.append(visitasPais)
            
    for i in range(len(paises)):
        if totalPais[i] > mayor:
            mayor= totalPais[i]
            indiceMayor = i
    
    if paises[indiceMayor] == "China":
        print("El pais con más contagiados es: ", paises[indiceMayor], "con: ", int(mayor), "personas. Y sus rangos etarios son: ","Rango1:",int(matriz1[0][0]),"Rango2:", int(matriz2[0][0]),"Rango3:", int(matriz3[0][0]),"Rango4:", int(matriz4[0][0]),"Rango5:", int(matriz5[0][0]),"Rango6:", int(matriz6[0][0]),"Rango7:", int(matriz7[0][0]),"Rango8:", int(matriz8[0][0]),"Rango9:", int(matriz9[0][0]),"Rango10:", int(matriz10[0][0]))

        

    while continuar == "Si":
        continuar= input("¿Desea saber el rango etario de un pais?(Si/No): ")
        if continuar == "Si":
            continuar= input("¿De que pais quiere saber el rango etario?(China, Francia, Japon, Malasia, Nepal, Singapur, CoreaSur, Taiwan, Tailandia, USA, Vietnam, Australia, Canada, Cambodia, SriLanka, Alemania, UAE, HongKong, UK, India, Filipinas, Finlandia, España, Suecia, Belgica, Egipto, Iran, Israel, Lebanon, Kuwait, Bahrain, Austria, Afganistan, Argelia, Croacia, Suiza): ")
            if continuar == "China":
                return print("Rango1:",int(matriz1[0][0]),"Rango2:", int(matriz2[0][0]),"Rango3:", int(matriz3[0][0]),"Rango4:", int(matriz4[0][0]),"Rango5:", int(matriz5[0][0]),"Rango6:", int(matriz6[0][0]),"Rango7:", int(matriz7[0][0]),"Rango8:", int(matriz8[0][0]),"Rango9:", int(matriz9[0][0]),"Rango10:", int(matriz10[0][0]))
            if continuar == "Francia":
                return print("Rango1:",int(matriz1[0][1]),"Rango2:", int(matriz2[0][1]),"Rango3:", int(matriz3[0][1]),"Rango4:", int(matriz4[0][1]),"Rango5:", int(matriz5[0][1]),"Rango6:", int(matriz6[0][1]),"Rango7:", int(matriz7[0][1]),"Rango8:", int(matriz8[0][1]),"Rango9:", int(matriz9[0][1]),"Rango10:", int(matriz10[0][1]))
            if continuar == "Japon":
                return print("Rango1:",int(matriz1[0][2]),"Rango2:", int(matriz2[0][2]),"Rango3:", int(matriz3[0][2]),"Rango4:", int(matriz4[0][2]),"Rango5:", int(matriz5[0][2]),"Rango6:", int(matriz6[0][2]),"Rango7:", int(matriz7[0][2]),"Rango8:", int(matriz8[0][2]),"Rango9:", int(matriz9[0][2]),"Rango10:", int(matriz10[0][2]))
            if continuar == "Malasia":
                return print("Rango1:",int(matriz1[0][3]),"Rango2:", int(matriz2[0][3]),"Rango3:", int(matriz3[0][3]),"Rango4:", int(matriz4[0][3]),"Rango5:", int(matriz5[0][3]),"Rango6:", int(matriz6[0][3]),"Rango7:", int(matriz7[0][3]),"Rango8:", int(matriz8[0][3]),"Rango9:", int(matriz9[0][3]),"Rango10:", int(matriz10[0][3]))
            if continuar == "Nepal":
                return print("Rango1:",int(matriz1[0][4]),"Rango2:", int(matriz2[0][4]),"Rango3:", int(matriz3[0][4]),"Rango4:", int(matriz4[0][4]),"Rango5:", int(matriz5[0][4]),"Rango6:", int(matriz6[0][4]),"Rango7:", int(matriz7[0][4]),"Rango8:", int(matriz8[0][4]),"Rango9:", int(matriz9[0][4]),"Rango10:", int(matriz10[0][4]))
            if continuar == "Singapur":
                return print("Rango1:",int(matriz1[0][5]),"Rango2:", int(matriz2[0][5]),"Rango3:", int(matriz3[0][5]),"Rango4:", int(matriz4[0][5]),"Rango5:", int(matriz5[0][5]),"Rango6:", int(matriz6[0][5]),"Rango7:", int(matriz7[0][5]),"Rango8:", int(matriz8[0][5]),"Rango9:", int(matriz9[0][5]),"Rango10:", int(matriz10[0][5]))
            if continuar == "CoreaSur":
                return print("Rango1:",int(matriz1[0][6]),"Rango2:", int(matriz2[0][6]),"Rango3:", int(matriz3[0][6]),"Rango4:", int(matriz4[0][6]),"Rango5:", int(matriz5[0][6]),"Rango6:", int(matriz6[0][6]),"Rango7:", int(matriz7[0][6]),"Rango8:", int(matriz8[0][6]),"Rango9:", int(matriz9[0][6]),"Rango10:", int(matriz10[0][6]))
            if continuar == "Taiwan":
                return print("Rango1:",int(matriz1[0][7]),"Rango2:", int(matriz2[0][7]),"Rango3:", int(matriz3[0][7]),"Rango4:", int(matriz4[0][7]),"Rango5:", int(matriz5[0][7]),"Rango6:", int(matriz6[0][7]),"Rango7:", int(matriz7[0][7]),"Rango8:", int(matriz8[0][7]),"Rango9:", int(matriz9[0][7]),"Rango10:", int(matriz10[0][7]))
            if continuar == "Tailandia":
                return print("Rango1:",int(matriz1[0][8]),"Rango2:", int(matriz2[0][8]),"Rango3:", int(matriz3[0][8]),"Rango4:", int(matriz4[0][8]),"Rango5:", int(matriz5[0][8]),"Rango6:", int(matriz6[0][8]),"Rango7:", int(matriz7[0][8]),"Rango8:", int(matriz8[0][8]),"Rango9:", int(matriz9[0][8]),"Rango10:", int(matriz10[0][8]))
            if continuar == "USA":
                return print("Rango1:",int(matriz1[0][9]),"Rango2:", int(matriz2[0][9]),"Rango3:", int(matriz3[0][9]),"Rango4:", int(matriz4[0][9]),"Rango5:", int(matriz5[0][9]),"Rango6:", int(matriz6[0][9]),"Rango7:", int(matriz7[0][9]),"Rango8:", int(matriz8[0][9]),"Rango9:", int(matriz9[0][9]),"Rango10:", int(matriz10[0][9]))
            if continuar == "Vietnam":
                return print("Rango1:",int(matriz1[0][10]),"Rango2:", int(matriz2[0][10]),"Rango3:", int(matriz3[0][10]),"Rango4:", int(matriz4[0][10]),"Rango5:", int(matriz5[0][10]),"Rango6:", int(matriz6[0][10]),"Rango7:", int(matriz7[0][10]),"Rango8:", int(matriz8[0][10]),"Rango9:", int(matriz9[0][10]),"Rango10:", int(matriz10[0][10]))
            if continuar == "Australia":
                return print("Rango1:",int(matriz1[0][11]),"Rango2:", int(matriz2[0][11]),"Rango3:", int(matriz3[0][11]),"Rango4:", int(matriz4[0][11]),"Rango5:", int(matriz5[0][11]),"Rango6:", int(matriz6[0][11]),"Rango7:", int(matriz7[0][11]),"Rango8:", int(matriz8[0][11]),"Rango9:", int(matriz9[0][11]),"Rango10:", int(matriz10[0][11]))
            if continuar == "Canada":
                return print("Rango1:",int(matriz1[0][12]),"Rango2:", int(matriz2[0][12]),"Rango3:", int(matriz3[0][12]),"Rango4:", int(matriz4[0][12]),"Rango5:", int(matriz5[0][12]),"Rango6:", int(matriz6[0][12]),"Rango7:", int(matriz7[0][12]),"Rango8:", int(matriz8[0][12]),"Rango9:", int(matriz9[0][12]),"Rango10:", int(matriz10[0][12]))
            if continuar == "Cambodia":
                return print("Rango1:",int(matriz1[0][13]),"Rango2:", int(matriz2[0][13]),"Rango3:", int(matriz3[0][13]),"Rango4:", int(matriz4[0][13]),"Rango5:", int(matriz5[0][13]),"Rango6:", int(matriz6[0][13]),"Rango7:", int(matriz7[0][13]),"Rango8:", int(matriz8[0][13]),"Rango9:", int(matriz9[0][13]),"Rango10:", int(matriz10[0][13]))
            if continuar == "SriLanka":
                return print("Rango1:",int(matriz1[0][14]),"Rango2:", int(matriz2[0][14]),"Rango3:", int(matriz3[0][14]),"Rango4:", int(matriz4[0][14]),"Rango5:", int(matriz5[0][14]),"Rango6:", int(matriz6[0][14]),"Rango7:", int(matriz7[0][14]),"Rango8:", int(matriz8[0][14]),"Rango9:", int(matriz9[0][14]),"Rango10:", int(matriz10[0][14]))
            if continuar == "Alemania":
                return print("Rango1:",int(matriz1[0][15]),"Rango2:", int(matriz2[0][15]),"Rango3:", int(matriz3[0][15]),"Rango4:", int(matriz4[0][15]),"Rango5:", int(matriz5[0][15]),"Rango6:", int(matriz6[0][15]),"Rango7:", int(matriz7[0][15]),"Rango8:", int(matriz8[0][15]),"Rango9:", int(matriz9[0][15]),"Rango10:", int(matriz10[0][15]))
            if continuar == "UAE":
                return print("Rango1:",int(matriz1[0][16]),"Rango2:", int(matriz2[0][16]),"Rango3:", int(matriz3[0][16]),"Rango4:", int(matriz4[0][16]),"Rango5:", int(matriz5[0][16]),"Rango6:", int(matriz6[0][16]),"Rango7:", int(matriz7[0][16]),"Rango8:", int(matriz8[0][16]),"Rango9:", int(matriz9[0][16]),"Rango10:", int(matriz10[0][16]))
            if continuar == "HongKong":
                return print("Rango1:",int(matriz1[0][17]),"Rango2:", int(matriz2[0][17]),"Rango3:", int(matriz3[0][17]),"Rango4:", int(matriz4[0][17]),"Rango5:", int(matriz5[0][17]),"Rango6:", int(matriz6[0][17]),"Rango7:", int(matriz7[0][17]),"Rango8:", int(matriz8[0][17]),"Rango9:", int(matriz9[0][17]),"Rango10:", int(matriz10[0][17]))
            if continuar == "UK":
                return print("Rango1:",int(matriz1[0][18]),"Rango2:", int(matriz2[0][18]),"Rango3:", int(matriz3[0][18]),"Rango4:", int(matriz4[0][18]),"Rango5:", int(matriz5[0][18]),"Rango6:", int(matriz6[0][18]),"Rango7:", int(matriz7[0][18]),"Rango8:", int(matriz8[0][18]),"Rango9:", int(matriz9[0][18]),"Rango10:", int(matriz10[0][18]))
            if continuar == "India":
                return print("Rango1:",int(matriz1[0][19]),"Rango2:", int(matriz2[0][19]),"Rango3:", int(matriz3[0][19]),"Rango4:", int(matriz4[0][19]),"Rango5:", int(matriz5[0][19]),"Rango6:", int(matriz6[0][19]),"Rango7:", int(matriz7[0][19]),"Rango8:", int(matriz8[0][19]),"Rango9:", int(matriz9[0][19]),"Rango10:", int(matriz10[0][19]))
            if continuar == "Filipinas":
                return print("Rango1:",int(matriz1[0][20]),"Rango2:", int(matriz2[0][20]),"Rango3:", int(matriz3[0][20]),"Rango4:", int(matriz4[0][20]),"Rango5:", int(matriz5[0][20]),"Rango6:", int(matriz6[0][20]),"Rango7:", int(matriz7[0][20]),"Rango8:", int(matriz8[0][20]),"Rango9:", int(matriz9[0][20]),"Rango10:", int(matriz10[0][20]))
            if continuar == "Finlandia":
                return print("Rango1:",int(matriz1[0][21]),"Rango2:", int(matriz2[0][21]),"Rango3:", int(matriz3[0][21]),"Rango4:", int(matriz4[0][21]),"Rango5:", int(matriz5[0][21]),"Rango6:", int(matriz6[0][21]),"Rango7:", int(matriz7[0][21]),"Rango8:", int(matriz8[0][21]),"Rango9:", int(matriz9[0][21]),"Rango10:", int(matriz10[0][21]))
            if continuar == "España":
                return print("Rango1:",int(matriz1[0][22]),"Rango2:", int(matriz2[0][22]),"Rango3:", int(matriz3[0][22]),"Rango4:", int(matriz4[0][22]),"Rango5:", int(matriz5[0][22]),"Rango6:", int(matriz6[0][22]),"Rango7:", int(matriz7[0][22]),"Rango8:", int(matriz8[0][22]),"Rango9:", int(matriz9[0][22]),"Rango10:", int(matriz10[0][22]))
            if continuar == "Suecia":
                return print("Rango1:",int(matriz1[0][23]),"Rango2:", int(matriz2[0][23]),"Rango3:", int(matriz3[0][23]),"Rango4:", int(matriz4[0][23]),"Rango5:", int(matriz5[0][23]),"Rango6:", int(matriz6[0][23]),"Rango7:", int(matriz7[0][23]),"Rango8:", int(matriz8[0][23]),"Rango9:", int(matriz9[0][23]),"Rango10:", int(matriz10[0][23]))
            if continuar == "Belgica":
                return print("Rango1:",int(matriz1[0][24]),"Rango2:", int(matriz2[0][24]),"Rango3:", int(matriz3[0][24]),"Rango4:", int(matriz4[0][24]),"Rango5:", int(matriz5[0][24]),"Rango6:", int(matriz6[0][24]),"Rango7:", int(matriz7[0][24]),"Rango8:", int(matriz8[0][24]),"Rango9:", int(matriz9[0][24]),"Rango10:", int(matriz10[0][24]))
            if continuar == "Egipto":
                return print("Rango1:",int(matriz1[0][25]),"Rango2:", int(matriz2[0][25]),"Rango3:", int(matriz3[0][25]),"Rango4:", int(matriz4[0][25]),"Rango5:", int(matriz5[0][25]),"Rango6:", int(matriz6[0][25]),"Rango7:", int(matriz7[0][25]),"Rango8:", int(matriz8[0][25]),"Rango9:", int(matriz9[0][25]),"Rango10:", int(matriz10[0][25]))
            if continuar == "Iran":
                return print("Rango1:",int(matriz1[0][26]),"Rango2:", int(matriz2[0][26]),"Rango3:", int(matriz3[0][26]),"Rango4:", int(matriz4[0][26]),"Rango5:", int(matriz5[0][26]),"Rango6:", int(matriz6[0][26]),"Rango7:", int(matriz7[0][26]),"Rango8:", int(matriz8[0][26]),"Rango9:", int(matriz9[0][26]),"Rango10:", int(matriz10[0][26]))
            if continuar == "Israel":
                return print("Rango1:",int(matriz1[0][27]),"Rango2:", int(matriz2[0][27]),"Rango3:", int(matriz3[0][27]),"Rango4:", int(matriz4[0][27]),"Rango5:", int(matriz5[0][27]),"Rango6:", int(matriz6[0][27]),"Rango7:", int(matriz7[0][27]),"Rango8:", int(matriz8[0][27]),"Rango9:", int(matriz9[0][27]),"Rango10:", int(matriz10[0][27]))
            if continuar == "Lebanon":
                return print("Rango1:",int(matriz1[0][28]),"Rango2:", int(matriz2[0][28]),"Rango3:", int(matriz3[0][28]),"Rango4:", int(matriz4[0][28]),"Rango5:", int(matriz5[0][28]),"Rango6:", int(matriz6[0][28]),"Rango7:", int(matriz7[0][28]),"Rango8:", int(matriz8[0][28]),"Rango9:", int(matriz9[0][28]),"Rango10:", int(matriz10[0][28]))
            if continuar == "Kuwait":
                return print("Rango1:",int(matriz1[0][29]),"Rango2:", int(matriz2[0][29]),"Rango3:", int(matriz3[0][29]),"Rango4:", int(matriz4[0][29]),"Rango5:", int(matriz5[0][29]),"Rango6:", int(matriz6[0][29]),"Rango7:", int(matriz7[0][29]),"Rango8:", int(matriz8[0][29]),"Rango9:", int(matriz9[0][29]),"Rango10:", int(matriz10[0][29]))
            if continuar == "Bahrain":
                return print("Rango1:",int(matriz1[0][30]),"Rango2:", int(matriz2[0][30]),"Rango3:", int(matriz3[0][30]),"Rango4:", int(matriz4[0][30]),"Rango5:", int(matriz5[0][30]),"Rango6:", int(matriz6[0][30]),"Rango7:", int(matriz7[0][30]),"Rango8:", int(matriz8[0][30]),"Rango9:", int(matriz9[0][30]),"Rango10:", int(matriz10[0][30]))
            if continuar == "Austria":
                return print("Rango1:",int(matriz1[0][31]),"Rango2:", int(matriz2[0][31]),"Rango3:", int(matriz3[0][31]),"Rango4:", int(matriz4[0][31]),"Rango5:", int(matriz5[0][31]),"Rango6:", int(matriz6[0][31]),"Rango7:", int(matriz7[0][31]),"Rango8:", int(matriz8[0][31]),"Rango9:", int(matriz9[0][31]),"Rango10:", int(matriz10[0][31]))
            if continuar == "Afganistan":
                return print("Rango1:",int(matriz1[0][32]),"Rango2:", int(matriz2[0][32]),"Rango3:", int(matriz3[0][32]),"Rango4:", int(matriz4[0][32]),"Rango5:", int(matriz5[0][32]),"Rango6:", int(matriz6[0][32]),"Rango7:", int(matriz7[0][32]),"Rango8:", int(matriz8[0][32]),"Rango9:", int(matriz9[0][32]),"Rango10:", int(matriz10[0][32]))
            if continuar == "Argelia":
                return print("Rango1:",int(matriz1[0][33]),"Rango2:", int(matriz2[0][33]),"Rango3:", int(matriz3[0][33]),"Rango4:", int(matriz4[0][33]),"Rango5:", int(matriz5[0][33]),"Rango6:", int(matriz6[0][33]),"Rango7:", int(matriz7[0][33]),"Rango8:", int(matriz8[0][33]),"Rango9:", int(matriz9[0][33]),"Rango10:", int(matriz10[0][33]))
            if continuar == "Croacia":
                return print("Rango1:",int(matriz1[0][34]),"Rango2:", int(matriz2[0][34]),"Rango3:", int(matriz3[0][34]),"Rango4:", int(matriz4[0][34]),"Rango5:", int(matriz5[0][34]),"Rango6:", int(matriz6[0][34]),"Rango7:", int(matriz7[0][34]),"Rango8:", int(matriz8[0][34]),"Rango9:", int(matriz9[0][34]),"Rango10:", int(matriz10[0][34]))
            if continuar == "Suiza":
                return print("Rango1:",int(matriz1[0][35]),"Rango2:", int(matriz2[0][35]),"Rango3:", int(matriz3[0][35]),"Rango4:", int(matriz4[0][35]),"Rango5:", int(matriz5[0][35]),"Rango6:", int(matriz6[0][35]),"Rango7:", int(matriz7[0][35]),"Rango8:", int(matriz8[0][35]),"Rango9:", int(matriz9[0][35]),"Rango10:", int(matriz10[0][35]))
            ###SI COMBINAMOS LAS MATRICES OBTENEMOS LAS COLUMNAS CON LOS RANGOS ETARIOS POR PAIS###

            
###PROGRAMA PRINCIPAL###

diaContagioManual= mayorDia("COVID19_data.txt")
masculinoChinaManual= 0
femeninoChinaManual= 0
masculinoHKManual= 0
femeninoHKManual= 0
rango1Manual= 0
rango2Manual= 0
rango3Manual= 0
rango4Manual= 0
rango5Manual= 0
rango6Manual= 0
rango7Manual= 0
rango8Manual= 0
rango9Manual= 0
rango10Manual= 0
masculinoChina,femeninoChina,masculinoHK,femeninoHK= chinos("COVID19_data.txt")
seguir= input("¿Desea añadir datos de pacientes?(Si/No): ")
while seguir == "Si":
    identificadorManual= int(input("Digame su numero identificador: "))
    paisManual= input("Digame de que pais es usted: ")
    sexoManual= input("Digame su sexo: ")
    edadManual= int(input("Digame la edad que usted tiene: "))
    diaContagioManualFinal= diaContagioManual+1 
    if paisManual == "China" and sexoManual == "masculino":
        masculinoChinaManual += 1
    if paisManual == "China" and sexoManual == "femenino":
        femeninoChinaManual += 1
    if paisManual == "Hong Kong" and sexoManual == "masculino":
        masculinoHKManual += 1
    if paisManual == "Hong Kong" and sexoManual == "femenino":
        femeninoHKManual += 1
    if edadManual >= 1 and edadManual <= 10:
        rango1Manual += 1
    if edadManual > 10 and edadManual <= 20:
        rango2Manual += 1
    if edadManual > 20 and edadManual <= 30:
        rango3Manual += 1
    if edadManual > 30 and edadManual <= 40:
        rango4Manual += 1
    if edadManual > 40 and edadManual <= 50:
        rango5Manual += 1
    if edadManual > 50 and edadManual <= 60:
        rango6Manual += 1
    if edadManual > 60 and edadManual <= 70:
        rango7Manual += 1
    if edadManual > 70 and edadManual <= 80:
        rango8Manual += 1
    if edadManual > 80 and edadManual <= 90:
        rango9Manual += 1
    if edadManual > 90 and edadManual <= 100:
        rango10Manual += 1
    seguir= input("¿Desea añadir a alguien más?: ")

masculinosChinosTotal= masculinoChina + masculinoChinaManual
femeninosChinosTotal= femeninoChina + femeninoChinaManual
masculinosHKTotal= masculinoHK + masculinoHKManual
femeninosHKTotal= femeninoHK + femeninoHKManual

totalMasculinos= masculinosChinosTotal + masculinosHKTotal
totalFemenino= femeninosChinosTotal + femeninosHKTotal
 

rangoEtarioPorPais("COVID19_data.txt")
print(rangoEtario("COVID19_data.txt"))
contagiosDiaMayor("COVID19_data.txt")
print("China tiene a: ", masculinosChinosTotal, "personas masculinas contagiadas y ", femeninosChinosTotal, "personas femeninas contagiadas. Si considarmos a Hong Kong, entonces hay personas hay: ",totalMasculinos, "personas masculinas contagiadas y a: ",totalFemenino, "personas femeninas contagiadas en total")
