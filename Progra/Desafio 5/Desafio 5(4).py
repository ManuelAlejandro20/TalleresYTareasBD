# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:03:27 2020

@author: Samsung
"""
import numpy as np        
###IMPORTANDO LA LIBRERIA NUMPY PARA LAS MATRICES###

def funcionencontrarmayor(lista):
    mayor = -9999
    indicemayor = -9999
    for i in range(0,len(lista)):
        if(lista[i] > mayor):
            mayor = lista[i]
            indicemayor = i
    return mayor, indicemayor

def rangoetarios(edades):
    rangos = [0,0,0,0,0,0,0,0,0,0]
    for edad in edades:
        if(edad>=1 and edad < 10):
            rangos[0] += 1
        elif(edad>=10 and edad < 20):
            rangos[1] += 1
        elif(edad>=20 and edad < 30):
            rangos[2] += 1
        elif(edad>=30 and edad < 40):
            rangos[3] += 1
        elif(edad>=40 and edad < 50):
            rangos[4] += 1
        elif(edad>=50 and edad < 60):
            rangos[5] += 1
        elif(edad>=60 and edad < 70):
            rangos[6] += 1
        elif(edad>=70 and edad < 80):
            rangos[7] += 1
        elif(edad>=80 and edad < 90):
            rangos[8] += 1
        elif(edad>=90 and edad < 100):
            rangos[9] += 1
    return rangos

def rangoetariomayor(edades):
    listarangos = rangoetarios(edades)
    cantmayor, indicerangomayor = funcionencontrarmayor(listarangos)
    if(indicerangomayor == 0):
        return "1 a 10 años con " + str(cantmayor) + " casos"
    elif(indicerangomayor == 1):
        return "10 a 20 años con " + str(cantmayor) + " casos"
    elif(indicerangomayor == 2):
        return "20 a 30 años con " + str(cantmayor) + " casos"
    elif(indicerangomayor == 3):
        return "30 a 40 años con " + str(cantmayor) + " casos"
    elif(indicerangomayor == 4):
        return "40 a 50 años con " + str(cantmayor) + " casos"
    elif(indicerangomayor == 5):
        return "50 a 60 años con " + str(cantmayor) + " casos"
    elif(indicerangomayor == 6):
        return "60 a 70 años con " + str(cantmayor) + " casos"
    elif(indicerangomayor == 7):
        return "70 a 80 años con " + str(cantmayor) + " casos"
    elif(indicerangomayor == 8):
        return "80 a 90 años con " + str(cantmayor) + " casos"
    elif(indicerangomayor == 9):
        return "90 a 100 años con " + str(cantmayor) + " casos"

def mostrarangosetarios(edades):
    rangos = rangoetarios(edades)
    for i in range(0,len(rangos)):
        if(i == 0):
            print('1 a 10 años:',rangos[i],'pacientes')
        elif(i == 1):
            print( '10 a 20 años:',rangos[i],'pacientes')
        elif(i == 2):
            print( '20 a 30 años:',rangos[i],'pacientes')
        elif(i == 3):
            print( '30 a 40 años:',rangos[i],'pacientes')
        elif(i == 4):
            print( '40 a 50 años:',rangos[i],'pacientes')
        elif(i == 5):
            print( '50 a 60 años:',rangos[i],'pacientes')
        elif(i == 6):
            print( '60 a 70 años:',rangos[i],'pacientes')
        elif(i == 7):
            print( '70 a 80 años:',rangos[i],'pacientes')
        elif(i == 8):
            print( '80 a 90 años:',rangos[i],'pacientes')
        elif(i == 9):
            print( '90 a 100 años:',rangos[i],'pacientes')
###PROGRAMA PRINCIPAL###

archivo = open("COVID19_data.txt", "r")
linea= archivo.readline().strip()
dias= []
edades = []
paises = []
matriz_edades_paises = np.zeros((1000,1000))
matriz_contagiados_paises = np.zeros((1000,1))
matriz_contagiados_dias = np.zeros((1000,1))
masculinoChinaManual= 0
femeninoChinaManual= 0
while linea != "":
    partes = linea.split(";")
    diaContagio= int(partes[1])
    pais = partes[2]
    genero = partes[3]
    edad = int(partes[4])
    edades.append(edad)
    if diaContagio not in dias:
        dias.append(diaContagio)
    if pais not in paises:
        paises.append(pais)
    indicepais = paises.index(pais)
    indicedia = dias.index(diaContagio)
    matriz_contagiados_dias[indicedia][0] += 1
    matriz_contagiados_paises[indicepais][0] += 1
    for i in range(0, 1000):
        if(matriz_edades_paises[indicepais][i] == 0.0):
            matriz_edades_paises[indicepais][i] = edad
            break
    if pais == "China" or pais == "Hong Kong" and genero == 'masculino':
        masculinoChinaManual += 1
    elif pais == "China" or pais == "Hong Kong" and genero == 'femenino':
        femeninoChinaManual += 1
    linea= archivo.readline().strip()
listadiamayor = funcionencontrarmayor(dias)
diamayor = listadiamayor[0] + 1
if diamayor not in dias:
    dias.append(diamayor)

seguir= input("¿Desea añadir datos de pacientes?(Si/No): ")
seguir = seguir.lower()
if(seguir == "sí"):
    seguir = "si"
while seguir == "si":
    try:
        identificadorManual= int(input("Digame su numero identificador: "))
    except:
        print("Error, no se detectaron numeros XX")
        continue
    paisManual= input("Digame de que pais es usted: ")
    paisManual = paisManual.capitalize()
    sexoManual= input("Digame su sexo: ")
    if(sexoManual != "masculino" and sexoManual != "femenino"):
        print("Error, opcion no valida XX")
        continue
    try:
        edadManual= int(input("Digame la edad que usted tiene: "))
    except:
        print("Error, no se detectaron numeros XX")
        continue
    edades.append(edadManual)
    if pais not in paises:
        paises.append(pais)
    indicepais = paises.index(paisManual)
    indicedia = dias.index(diamayor)
    matriz_contagiados_dias[indicedia][0] += 1
    matriz_contagiados_paises[indicepais][0] += 1
    for i in range(0, 1000):
        if(matriz_edades_paises[indicepais][i] == 0.0):
            matriz_edades_paises[indicepais][i] = edadManual
            break
    if paisManual == "China" or pais == "Hong Kong" and sexoManual == 'masculino':
        masculinoChinaManual += 1
    elif paisManual == "China" or pais == "Hong Kong" and sexoManual == 'femenino':
        femeninoChinaManual += 1
    seguir= input("¿Desea añadir a alguien más?: ")
    seguir = seguir.lower()
    if(seguir == "sí"):
        seguir = "si"
indicemaximo = -999999
maxpacientes = -999999
for i in range(0,1000):
    if(matriz_contagiados_paises[i][0] > maxpacientes):
        maxpacientes = matriz_contagiados_paises[i][0]
        indicemaximo = i
print("El pais mas contagiado es",paises[indicemaximo],"con",int(maxpacientes),"casos")
indicemaximodias = -999999
maxpacientesdias = -999999
for i in range(0,1000):
    if(matriz_contagiados_dias[i][0] > maxpacientesdias):
        maxpacientesdias = matriz_contagiados_dias[i][0]
        indicemaximodias = i
print("China tiene:",masculinoChinaManual,"hombres contagiados y",femeninoChinaManual,"mujeres contagiadas")
print("El dia con mas contagiado es",dias[indicemaximodias],"con",int(maxpacientesdias),"casos")
print("Este es el rango etario con mayor cantidad de contagiados")
print(rangoetariomayor(edades))
print("Rangos etarios para el pais con mas contagiados")
mostrarangosetarios(matriz_edades_paises[indicemaximo])
continuar= input("¿Desea saber el rango etario de un pais?(Si/No): ")
continuar = continuar.lower()
if(continuar == "sí"):
    continuar = "si"
while continuar == "si":
    pais = input("Ingresa el pais:")
    pais = pais.capitalize()
    if pais not in paises:
        print("ERROR pais no encontrado XX")
        continue
    indicepais = paises.index(pais)
    print('El rango etario de',pais)
    mostrarangosetarios(matriz_edades_paises[indicepais])
    continuar= input("¿Desea saber el rango etario de un pais?(Si/No): ")
    continuar = continuar.lower()
    if(continuar == "sí"):
        continuar = "si"