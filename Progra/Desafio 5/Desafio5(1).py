def maximodiasfuncion(dias):
    maximo = -9999
    for dia in dias:
        if(dia > maximo):
            maximo = dia
    return maximo
def rangoaños(años):
    rangos = [0,0,0,0,0,0,0,0,0,0,0]
    for año in años:
        if(año>=1 and año < 10):
            rangos[0] += 1
        elif(año>=10 and año < 20):
            rangos[1] += 1
        elif(año>=20 and año < 30):
            rangos[2] += 1
        elif(año>=30 and año < 40):
            rangos[3] += 1
        elif(año>=40 and año < 50):
            rangos[4] += 1
        elif(año>=50 and año < 60):
            rangos[5] += 1
        elif(año>=60 and año < 70):
            rangos[6] += 1
        elif(año>=70 and año < 80):
            rangos[7] += 1
        elif(año>=80 and año < 90):
            rangos[8] += 1
        elif(año>=90 and año < 100):
            rangos[9] += 1
        elif(año>=100):
            rangos[10] += 1
    maximo = -9999
    indicemax = -9999
    for rango in range(0,11):
        if(rangos[rango] > maximo):
            maximo = rangos[rango]
            indicemax = rango
    if(indicemax == 0):
        return '1 a 10 años'
    elif(indicemax == 1):
        return '10 a 20 años'
    elif(indicemax == 2):
        return '20 a 30 años'
    elif(indicemax == 3):
        return '30 a 40 años'
    elif(indicemax == 4):
        return '40 a 50 años'
    elif(indicemax == 5):
        return '50 a 60 años'
    elif(indicemax == 6):
        return '60 a 70 años'
    elif(indicemax == 7):
        return '70 a 80 años'
    elif(indicemax == 8):
        return '80 a 90 años'
    elif(indicemax == 9):
        return '90 a 100 años'
    elif(indicemax == 10):
        return 'mas de 100 años'

def rangoañostodos(años):
    rangos = [0,0,0,0,0,0,0,0,0,0,0]
    for año in años:
        if(año>=1 and año < 10):
            rangos[0] += 1
        elif(año>=10 and año < 20):
            rangos[1] += 1
        elif(año>=20 and año < 30):
            rangos[2] += 1
        elif(año>=30 and año < 40):
            rangos[3] += 1
        elif(año>=40 and año < 50):
            rangos[4] += 1
        elif(año>=50 and año < 60):
            rangos[5] += 1
        elif(año>=60 and año < 70):
            rangos[6] += 1
        elif(año>=70 and año < 80):
            rangos[7] += 1
        elif(año>=80 and año < 90):
            rangos[8] += 1
        elif(año>=90 and año < 100):
            rangos[9] += 1
        elif(año>=100):
            rangos[10] += 1
    for i in range(0,11):
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
        elif(i == 10):
            print( 'mas de 100 años:',rangos[i],'pacientes')
    return

paises2 = []
contagiadospais = []
matrizedadpaises = []
dias2 = []
contagiadosdias = []
chinagenero = [0,0]

idpacs = []
dias = []
paises = []
generos = []
edades = []
arch = open('COVID19_data.txt','r')
linea = arch.readline().strip()
while(linea!=''):
    linea2 = linea.split(';')
    dia = int(linea2[1])
    pais = linea2[2]
    genero = linea2[3]
    edad = int(linea2[4])

    idpacs.append(int(linea2[0]))
    dias.append(dia)
    paises.append(pais)
    generos.append(genero)
    edades.append(edad)

    if(pais not in paises2):
        paises2.append(pais)
    if(dia not in dias2):
        dias2.append(dia)
    indicepais = paises2.index(pais)
    indicedia = dias2.index(dia)
    try:
        contagiadospais[indicepais] += 1
    except:
        contagiadospais.append(1)
    try:
        contagiadosdias[indicedia] += 1
    except:
        contagiadosdias.append(1)
    try:
        matrizedadpaises[indicepais].append(edad)
    except:
        matrizedadpaises.append([])
        matrizedadpaises[indicepais].append(edad)
    if(pais == 'China'):
        if(genero == 'masculino'):
            chinagenero[0] += 1
        else:
            chinagenero[1] += 1
    linea = arch.readline().strip()
diamax = maximodiasfuncion(dias) + 1
if(diamax not in dias2):
    dias2.append(diamax)
print('¿Desea agregar un nuevo paciente [Si para continuar]?')
continuar = input()
continuar = continuar.lower()
if(continuar == 'sí'):
    continuar = 'si'
while(continuar=='si'):
    try:
        print('Ingresa el identificador del paciente')
        idpac = int(input())
        print('Ingresa la edad del paciente')
        edad = int(input())
    except:
        print('Ingresa un numero valido porfavor')
        continue
    print('Ingresa el pais del paciente')
    pais = input()
    pais = pais.capitalize()
    print('Ingresa el genero del paciente')
    genero = input()
    genero = genero.lower()
    if(genero != 'masculino' and genero != 'femenino'):
        print('Ingresa una opcion valida')
        continue
    idpacs.append(idpac)
    dias.append(diamax)
    paises.append(pais)
    generos.append(genero)
    edades.append(edad)
    if(pais not in paises2):
        paises2.append(pais)
    indicepais = paises2.index(pais)
    indicedia = dias2.index(diamax)
    try:
        contagiadospais[indicepais] += 1
    except:
        contagiadospais.append(1)
    try:
        contagiadosdias[indicedia] += 1
    except:
        contagiadosdias.append(1)
    try:
        matrizedadpaises[indicepais].append(edad)
    except:
        matrizedadpaises.append([])
        matrizedadpaises[indicepais].append(edad)
    if(pais == 'China'):
        if(genero == 'masculino'):
            chinagenero[0] += 1
        else:
            chinagenero[1] += 1
    print('Paciente agregado al sistema')
    print('¿Desea agregar un nuevo paciente [Si para continuar]?')
    continuar = input()
    continuar = continuar.lower()
    if(continuar == 'sí'):
        continuar = 'si'
indicemax = -9999
maximo = -9999
for i in range(0,len(contagiadospais)):
    if(contagiadospais[i] > maximo):
        maximo = contagiadospais[i]
        indicemax = i
indicemaxpais = indicemax
print('El pais con mas contagiados es',paises2[indicemax], 'con',maximo,'casos')
print('China tiene',chinagenero[0],'hombres contagiados y',chinagenero[1],'mujeres contagiadas')
indicemax = -9999
maximo = -9999
for i in range(0,len(contagiadosdias)):
    if(contagiadosdias[i] > maximo):
        maximo = contagiadosdias[i]
        indicemax = i
print('El dia con mas contagios fue el',dias2[indicemax], 'con',maximo,'casos')
rangomax = rangoaños(edades)
print('El rango etario con mas contagiados es de',rangomax)
print('El rango etario de contagiados en el pais de mas contagiados')
rangoañostodos(matrizedadpaises[indicemaxpais])
print('¿Desea ver el rango etario de contagiados de algun pais? [Si para continuar]')
continuar = input()
continuar = continuar.lower()
if(continuar == 'sí'):
    continuar = 'si'
while(continuar=='si'):
    print('Ingresa el nombre del pais')
    pais = input()
    pais = pais.capitalize()
    if(pais not in paises2):
        print('Ese pais no esta en los registros intenta nuevamente')
        continue
    indicepais = paises2.index(pais)
    rangomax = rangoaños(matrizedadpaises[indicepais])
    print('El rango etario de contagiados en',pais)
    rangoañostodos(matrizedadpaises[indicepais])
    print('¿Desea ver el rango etario de contagiados de algun pais? [Si/No]')
    continuar = input()
    continuar = continuar.lower()
    if(continuar == 'sí'):
        continuar = 'si'