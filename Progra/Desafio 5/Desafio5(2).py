import numpy as np
def funciondiafinal(listadias):
    diafinal = -999999
    for dia in listadias:
        if(dia > diafinal):
            diafinal = dia
    return diafinal
def funcionrangoetario(edades):
    matriz = np.zeros([10,1])
    for edad in edades:
        if(edad == 0.0):
            break
        edadint = int(edad)
        edadstr = str(edadint)
        if(len(edadstr) == 1):
            matriz[0][0] += 1
        else:
            matriz[int(edadstr[0])][0] += 1
    maximo = -9999
    indicemaximo = -9999
    for i in range(0,10):
        if(matriz[i][0] > maximo):
            maximo = matriz[i][0]
            indicemaximo = i
    if(indicemaximo == 0):
        print('De 1 año a 10 años')
    elif(indicemaximo == 9):
        print('De 90 años a 100 años')
    edadmenor = str(indicemaximo) + '0'
    edadmayor = str(indicemaximo + 1) + '0'
    return print('De',edadmenor , 'años a',edadmayor,'años')

def funcionmostrarrangoetario(edades):
    matriz = np.zeros([10,1])
    for edad in edades:
        if(edad == 0.0):
            break
        edadint = int(edad)
        edadstr = str(edadint)
        if(len(edadstr) == 1):
            matriz[0][0] += 1
        else:
            matriz[int(edadstr[0])][0] += 1
    for i in range(0,11):
        if(i == 0):
            print('De 1 año a 10 años:',int(matriz[i][0]),'pacientes')
        elif(i == 1):
            print( 'De 10 años a 20 años:',int(matriz[i][0]),'pacientes')
        elif(i == 2):
            print( 'De 20 años a 30 años:',int(matriz[i][0]),'pacientes')
        elif(i == 3):
            print( 'De 30 años a 40 años:',int(matriz[i][0]),'pacientes')
        elif(i == 4):
            print( 'De 40 años a 50 años:',int(matriz[i][0]),'pacientes')
        elif(i == 5):
            print( 'De 50 años a 60 años:',int(matriz[i][0]),'pacientes')
        elif(i == 6):
            print( 'De 60 años a 70 años:',int(matriz[i][0]),'pacientes')
        elif(i == 7):
            print( 'De 70 años a 80 años:',int(matriz[i][0]),'pacientes')
        elif(i == 8):
            print( 'De 80 años a 90 años:',int(matriz[i][0]),'pacientes')
        elif(i == 9):
            print( 'De 90 años a 100 años:',int(matriz[i][0]),'pacientes')



listapaises = []
listadias = []
edades = []
matrizcontagiadospais = np.zeros((100,1))
matrizcontagiadosdias = np.zeros((100,1))
matrizpaisesyedades = np.zeros((1000,1000))
mas = 0
fem = 0
archivo = open('COVID19_data.txt','r')
linealeida = archivo.readline().strip()
while(linealeida!=''):
    lineasplit = linealeida.split(';')
    dia = int(lineasplit[1])
    pais = lineasplit[2]
    genero = lineasplit[3]
    edad = int(lineasplit[4])
    edades.append(edad)
    if(pais not in listapaises):
        listapaises.append(pais)
    if(dia not in listadias):
        listadias.append(dia)
    matrizcontagiadospais[listapaises.index(pais)] += 1
    matrizcontagiadosdias[listadias.index(dia)] += 1
    for i in range(0,1000):
        if(matrizpaisesyedades[listapaises.index(pais)][i] == 0.0):
            matrizpaisesyedades[listapaises.index(pais)][i] = edad
            break
    if(pais == 'China' and genero == 'masculino'):
        mas += 1
    elif(pais == 'China' and genero == 'femenino'):
        fem += 1
    linealeida = archivo.readline().strip()
diafinal = funciondiafinal(listadias) + 1
if(diafinal not in listadias):
    listadias.append(diafinal)
while(1):
    print('¿Deseas agregar un paciente nuevo al sistema?')
    resp = input()
    resp = resp.lower()
    if(resp == 'si' or resp == 'sí'):
        try:
            print('Id del paciente')
            idpac = int(input())
        except ValueError:
            print('ERROR DE ID')
            continue
        print('Pais del paciente')
        pais = input()
        pais = pais.capitalize()
        print('Genero del paciente')
        genero = input()
        if(genero not in ['masculino', 'femenino']):
            print('ERROR OPCION NO VALIDA')
            continue
        try:
            print('Edad del paciente')
            edad = int(input())
        except ValueError:
            print('ERROR DE EDAD')
            continue
        edades.append(edad)
        if(pais not in listapaises):
            listapaises.append(pais)
        if(dia not in listadias):
            listadias.append(dia)
        matrizcontagiadospais[listapaises.index(pais)] += 1
        matrizcontagiadosdias[listadias.index(dia)] += 1
        for i in range(0,1000):
            if(matrizpaisesyedades[listapaises.index(pais)][i] == 0.0):
                matrizpaisesyedades[listapaises.index(pais)][i] = edad
                break
        if(pais == 'China' and genero == 'masculino'):
            mas += 1
        elif(pais == 'China' and genero == 'femenino'):
            fem += 1
        print('Paciente agregado al sistema')
    elif(resp == 'no'):
        break
indicemaximo = -999999
maximopacientes = -999999
for i in range(0,100):
    if(matrizcontagiadospais[i][0] > maximopacientes):
        maximopacientes = matrizcontagiadospais[i][0]
        indicemaximo = i
print(listapaises[indicemaximo], 'es el pais con mas contagiados (',int(maximopacientes),')')
print('China tiene:')
print(mas,'hombres contagiados')
print(fem,'mujeres contagiados')
print('En el pais de mas contagiados el rango etario mayor es:')
funcionmostrarrangoetario(matrizpaisesyedades[indicemaximo])
print('El rango etario mayor entre el total de paises es:')
funcionrangoetario(edades)

indicemaximo = -9999
maximo = -9999
for i in range(0,100):
    if(matrizcontagiadosdias[i][0] > maximo):
        maximo = matrizcontagiadosdias[i][0]
        indicemaximo = i
print('Dia con mas contagios:', listadias[indicemaximo])
while(1):
    print('¿Deseas saber el rango etario de otro pais?')
    res = input()
    if(res == 'si' or res == 'sí'):
        print('Ingresa el pais')
        pais = input()
        pais = pais.capitalize()
        if(pais not in listapaises):
            print('Este pais no existe')
            continue
        indicepais = listapaises.index(pais)
        print('En',pais,'el rango etario de contagiados es:')
        funcionmostrarrangoetario(matrizpaisesyedades[indicepais])
    elif(res == 'no'):
        break

