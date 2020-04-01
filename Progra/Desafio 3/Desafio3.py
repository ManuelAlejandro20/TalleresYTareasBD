clinica1 = []
clinica2 = []
clinica3 = []

edades1 = []
edades2 = []
edades3 = []

pregunta = ''
cont = 0
for i in range(1,4):

        print('¿Quieres registrar una nueva persona en la clinica ' , i , '? (Sí/No): ')
        pregunta = input()
        pregunta = pregunta.lower()
        if(pregunta == 'sí'):
            pregunta = 'si'

        if(pregunta != 'si' and pregunta != 'no'):
            print('\n>> Ingresa una de las opciones validas porfavor <<\n')
            pregunta = ''

        while(pregunta != 'no'):
                if(pregunta == 'si'):
                    persona = input('\nIngresa el nombre de la persona que quieres agregar porfavor: ')
                    persona = persona.capitalize()

                    try:
                        print('Ingresa la edad de ' , persona , ' porfavor: ')
                        edad = int(input())
                    except:
                        print('\n>> Ingresa una de las opciones validas porfavor <<\n')
                        pregunta = ''
                        continue


                    if(edad < 10 and i != 2):
                        if(persona not in clinica2):
                            clinica2.append(persona)
                            edades2.append(edad)
                            print('\n>> Persona agregada, fue derivada a la clinica 2! <<\n')
                            cont += 1
                        else:
                            print('\n>> Esta persona ya esta inscrita, intenta nuevamente <<\n')
                        pregunta = ''
                        continue
                    
                    if(i == 1):
                        if(persona not in clinica1):
                            clinica1.append(persona)
                            edades1.append(edad)
                            print('\n>> Persona agregada! <<\n')
                            cont += 1
                        else:
                            print('\n>> Esta persona ya esta inscrita, intenta nuevamente <<\n')

                    elif(i == 2):
                        if(persona not in clinica2):
                            clinica2.append(persona)
                            edades2.append(edad)
                            print('\n>> Persona agregada! <<\n')
                            cont += 1
                        else:
                            print('\n>> Esta persona ya esta inscrita, intenta nuevamente <<\n')
                    
                    elif(i == 3):
                        if(persona not in clinica3):
                            clinica3.append(persona)
                            edades3.append(edad)
                            print('\n>> Persona agregada! <<\n')
                            cont += 1
                        else:
                            print('\n>> Esta persona ya esta inscrita, intenta nuevamente <<\n')
                    
                print('¿Quieres registrar una nueva persona en la clinica? ' , i , ' (Sí/No): ')    
                pregunta = input()
                pregunta.lower()
                if(pregunta == 'sí'):
                    pregunta = 'si'
                if(pregunta != 'si' and pregunta != 'no'):
                    print('\n>> Ingresa una de las opciones validas porfavor <<\n')


        pregunta = ''

archivo1 = open('1.txt', 'r')
archivo2 = open('1.txt', 'r')
archivo3 = open('1.txt', 'r')

linea = archivo1.readline().strip()
while(linea != ""):
    lineaSplit = linea.split(',')
    if(int(lineaSplit[1]) < 10):
        clinica2.append(lineaSplit[0])
        edades2.append(int(lineaSplit[1]))
    else:
        clinica1.append(lineaSplit[0])
        edades1.append(int(lineaSplit[1]))
    linea = archivo1.readline().strip()
    
linea = archivo2.readline().strip()
while(linea != ""):
    lineaSplit = linea.split(',')
    clinica2.append(lineaSplit[0])
    edades2.append(int(lineaSplit[1]))
    linea = archivo2.readline().strip()

linea = archivo3.readline().strip()
while(linea != ""):
    lineaSplit = linea.split(',')
    if(int(lineaSplit[1]) < 10):
        clinica2.append(lineaSplit[0])
        edades2.append(int(lineaSplit[1]))
    else:
        clinica3.append(lineaSplit[0])
        edades3.append(int(lineaSplit[1]))
    linea = archivo3.readline().strip()

max = -9999
clinicamax = ''

print('\n>>> La clinica con mas pacientes es: ')
if(len(clinica1) > max):
    max = len(clinica1)
    clinicamax = 'clinica 1'
if(len(clinica2) > max):
    max = len(clinica2)
    clinicamax = 'clinica 2'
if(len(clinica3) > max):
    max = len(clinica2)
    clinicamax = 'clinica 3'
print(clinicamax , ' con ' , max , ' pacientes')

edades = 0
for i in edades3:
    edades += i
prom = round(edades/len(clinica3), 2)
print('\n>>>El promedio de edades de la clinica 3 es ' , prom , ' años')

listaTotal = []

for i in range (0, len(clinica1)):
    if(clinica1[i] not in listaTotal and edades1[i] >= 18 and edades1[i] <= 50):
        listaTotal.append(clinica1[i])

for i in range (0, len(clinica2)):
    if(clinica2[i] not in listaTotal and edades2[i] >= 18 and edades2[i] <= 50):
        listaTotal.append(clinica1[i])

for i in range (0, len(clinica3)):
    if(clinica3[i] not in listaTotal and edades3[i] >= 18 and edades3[i] <= 50):
        listaTotal.append(clinica1[i])

print('\n>>> Todos los pacientes entre 18 y 50 años ordenados alfabeticamente')
listaTotal = sorted(listaTotal)
for i in listaTotal:
    print('     ' + i)

porc = round((cont*100)/(len(clinica1) + len(clinica2) + len(clinica3)), 2)
print('\n>>>Porcentaje de personas agregadas manualmente: ' , porc , '%')











