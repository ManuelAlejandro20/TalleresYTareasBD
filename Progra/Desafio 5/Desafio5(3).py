import numpy as np
def etariofuncion(edades):
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    cont9 = 0
    cont10 = 0
    for edad in edades:
        edadint = int(edad)
        if(edadint>=1 and edadint < 10):
            cont1 += 1
        elif(edadint>=10 and edadint < 20):
            cont2 += 1
        elif(edadint>=20 and edadint < 30):
            cont3 += 1
        elif(edadint>=30 and edadint < 40):
            cont4 += 1
        elif(edadint>=40 and edadint < 50):
            cont5 += 1
        elif(edadint>=50 and edadint < 60):
            cont6 += 1
        elif(edadint>=60 and edadint < 70):
            cont7 += 1
        elif(edadint>=70 and edadint < 80):
            cont8 += 1
        elif(edadint>=80 and edadint < 90):
            cont9 += 1
        elif(edadint>=90 and edadint < 100):
            cont10 += 1
    maximo = -9999
    if(cont1 > maximo):
        maximo = cont1
        rango = 'De 1 año a 10 años'
    if(cont2 > maximo):
        maximo = cont2
        rango = 'De 10 años a 20 años'
    if(cont3 > maximo):
        maximo = cont3
        rango = 'De 20 años a 30 años'
    if(cont4 > maximo):
        maximo = cont4
        rango = 'De 30 años a 40 años'
    if(cont5 > maximo):
        maximo = cont5
        rango = 'De 40 años a 50 años'
    if(cont6 > maximo):
        maximo = cont6
        rango = 'De 50 años a 60 años'
    if(cont7 > maximo):
        maximo = cont7
        rango = 'De 60 años a 70 años'
    if(cont8 > maximo):
        maximo = cont8
        rango = 'De 70 años a 80 años'
    if(cont9 > maximo):
        maximo = cont9
        rango = 'De 80 años a 90 años'
    if(cont10 > maximo):
        maximo = cont10
        rango = 'De 90 años a 100 años'
    return rango

def mostraretariofuncion(edades):
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    cont9 = 0
    cont10 = 0
    for edad in edades:
        edadint = int(edad)
        if(edadint>=1 and edadint < 10):
            cont1 += 1
        elif(edadint>=10 and edadint < 20):
            cont2 += 1
        elif(edadint>=20 and edadint < 30):
            cont3 += 1
        elif(edadint>=30 and edadint < 40):
            cont4 += 1
        elif(edadint>=40 and edadint < 50):
            cont5 += 1
        elif(edadint>=50 and edadint < 60):
            cont6 += 1
        elif(edadint>=60 and edadint < 70):
            cont7 += 1
        elif(edadint>=70 and edadint < 80):
            cont8 += 1
        elif(edadint>=80 and edadint < 90):
            cont9 += 1
        elif(edadint>=90 and edadint < 100):
            cont10 += 1
    for i in range(0,10):
        if(i == 0):
            print('1 a 10 años:',cont1,'contagiados')
        elif(i == 1):
            print( '10 a 20 años:',cont2,'contagiados')
        elif(i == 2):
            print( '20 a 30 años:',cont3,'contagiados')
        elif(i == 3):
            print( '30 a 40 años:',cont4,'contagiados')
        elif(i == 4):
            print( '40 a 50 años:',cont5,'contagiados')
        elif(i == 5):
            print( '50 a 60 años:',cont6,'contagiados')
        elif(i == 6):
            print( '60 a 70 años:',cont7,'contagiados')
        elif(i == 7):
            print( '70 a 80 años:',cont8,'contagiados')
        elif(i == 8):
            print( '80 a 90 años:',cont9,'contagiados')
        elif(i == 9):
            print( '90 a 100 años:',cont10,'contagiados')
    return




def encontrardiamaximo(dias):
    diamaximo = -99999
    for i in range(0,len(dias)):
        if(dias[i] > diamaximo):
            diamaximo = dias[i]
    return diamaximo + 1

paisesdif = []
diasdif = []
edadesnodif = []
edades_paises = np.zeros((500,500))
edades_dias = np.zeros((500,500))
masculinochina = 0
femeninochina = 0
a = open('COVID19_data.txt','r')
l = a.readline().strip()
while l!='':
    l2 = l.split(';')
    dia = int(l2[1])
    pais = l2[2]
    genero = l2[3]
    edad = int(l2[4])
    edadesnodif.append(edad)
    if pais not in paisesdif :
        paisesdif.append(pais)
    if dia not in diasdif:
        diasdif.append(dia)
    indicedelpais = paisesdif.index(pais)
    indicedeldia = diasdif.index(dia)
    for i in range(0,500):
        if(edades_paises[indicedelpais][i] == 0.0):
            edades_paises[indicedelpais][i] = edad
            break
    for i in range(0,500):
        if(edades_dias[indicedeldia][i] == 0.0):
            edades_dias[indicedeldia][i] = edad
            break
    if(pais == 'China' and genero == 'masculino'):
        masculinochina += 1
    elif(pais == 'China' and genero == 'femenino'):
        femeninochina += 1
    l = a.readline().strip()
diamaximo = encontrardiamaximo(diasdif)
if diamaximo not in diasdif:
    diasdif.append(diamaximo)
continuar = 'si'
while(continuar == 'si'):
    print('¿Quieres agregar un paciente nuevo?')
    continuar = input()
    continuar = continuar.lower()
    if(continuar == 'si' or continuar == 'sí'):
        try:
            print('Ingresa id nuevo')
            idpaciente = int(input())
        except:
            print('Error, ingresaste letras')
            continue
        try:
            print('Ingresa edad nueva')
            edad = int(input())
        except:
            print('Error, ingresaste letras')
            continue
        print('Ingresa pais nuevo')
        pais = input()
        pais = pais.capitalize()
        print('Ingresa genero')
        genero = input()
        if(genero != 'femenino' and genero != 'masculino'):
            print('Error, opcion no valida')
            continue
        edadesnodif.append(edad)
        if pais not in paisesdif :
            paisesdif.append(pais)
        if dia not in diasdif:
            diasdif.append(dia)
        indicedelpais = paisesdif.index(pais)
        indicedeldia = diasdif.index(dia)
        for i in range(0,500):
            if(edades_paises[indicedelpais][i] == 0.0):
                edades_paises[indicedelpais][i] = edad
                break
        for i in range(0,500):
            if(edades_dias[indicedeldia][i] == 0.0):
                edades_dias[indicedeldia][i] = edad
                break
        if(pais == 'China' and genero == 'masculino'):
            masculinochina += 1
        elif(pais == 'China' and genero == 'femenino'):
            femeninochina += 1
        print('¡Se agrego al paciente con exito!')
paismaximo = ''
maximopais = -99999
indicemaximo = -1
cont = 0
for i in range(0,len(paisesdif)):
    for j in range(0,500):
        if(edades_paises[i][j] != 0.0):
            cont += 1 
    if(cont > maximopais):
        paismaximo = paisesdif[i]
        indicemaximo = i
        maximopais = cont
    cont = 0
diamaximo = 0
maximodia = -99999
cont = 0
for i in range(0,len(diasdif)):
    for j in range(0,500):
        if(edades_dias[i][j] != 0.0):
            cont += 1 
    if(cont > maximodia):
        diamaximo = diasdif[i]
        maximodia = cont
    cont = 0
print('El pais mas contagiado es', paismaximo)
print('El dia con mas contagios es', diamaximo)
print('Rango etario mayor')
print(etariofuncion(edadesnodif))
print('Rango etario para el pais de mas contagios')
mostraretariofuncion(edades_paises[indicemaximo])
continuar = 'si'
while(continuar=='si'):
    print('¿Quieres ver el rango etario de un pais?')
    continuar = input()
    continuar = continuar.lower()
    if(continuar == 'si' or continuar == 'sí'):
        print('Ingresa el nombre del pais')
        pais = input()
        pais = pais.capitalize()
        if(pais not in paisesdif):
            print('Error, paises no existe')
            continue
        indicepais = paisesdif.index(pais)
        print('El rango etario de contagiados de', pais)
        mostraretariofuncion(edades_paises[indicepais])