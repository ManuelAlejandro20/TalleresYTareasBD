def funcionsistolica(presionlinealeida):
    listapresion = presionlinealeida.split("/") 
    presionsis = listapresion[0]
    presionsis = int(presionsis) 
    return presionsis

def funcionestado(presion, pulso, temperatura, respiratoria):
    estadopaciente = ""
    if(presion < 40 or presion > 180 or pulso < 30 or pulso > 150 or temperatura >= 42):
        estadopaciente = 'pacientecritico'
    elif(presion < 60 or presion > 150 or pulso < 50 or pulso > 120 or temperatura >= 40.5 or respiratoria < 15 or respiratoria > 20):
        estadopaciente = 'pacientegrave'
    elif(presion < 90 or presion > 120 or pulso < 60 or pulso > 90 or temperatura >= 37.3):
        estadopaciente = 'pacienteleve'
    elif(presion >= 90 and presion <= 120 or pulso >= 60 and pulso <= 90 or temperatura >= 36.6 and temperatura <= 37.2 or respiratoria >= 15 and respiratoria <= 20):
        estadopaciente = 'pacienteestable'
    return estadopaciente

def funcionrangohoras(horasleidas):
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0
    contador6 = 0
    contador7 = 0
    contador8 = 0
    contador9 = 0
    contador10 = 0
    contador11 = 0
    contador12 = 0
    
    for hora in horasleidas:
        if(hora >= 0 and hora < 2):
            contador1 += 1
        elif(hora >= 2 and hora < 4):
            contador2 += 1
        elif(hora >= 4 and hora < 6):
            contador3 += 1
        elif(hora >= 6 and hora < 8):
            contador4 += 1
        elif(hora >= 8 and hora < 10):
            contador5 += 1
        elif(hora >= 10 and hora < 12):
            contador6 += 1
        elif(hora >= 12 and hora < 14):
            contador7 += 1
        elif(hora >= 14 and hora < 16):
            contador8 += 1
        elif(hora >= 16 and hora < 18):
            contador9 += 1
        elif(hora >= 18 and hora < 20):
            contador10 += 1
        elif(hora >= 20 and hora < 22):
            contador11 += 1
        elif(hora >= 22 and hora < 24):
            contador12 += 1

    rango = ''
    maximo = -9999
    if(contador1 > maximo):
        maximo = contador1
        rango = '00:00am - 02:00am'
    if(contador2 > maximo):
        maximo = contador2
        rango = '02:00am - 04:00am'
    if(contador3 > maximo):
        maximo = contador3
        rango = '04:00am - 06:00am'
    if(contador4 > maximo):
        maximo = contador4
        rango = '06:00am - 08:00am'
    if(contador5 > maximo):
        maximo = contador5
        rango = '08:00am - 10:00am'
    if(contador6 > maximo):
        maximo = contador6
        rango = '10:00am - 12:00pm'
    if(contador7 > maximo):
        maximo = contador7
        rango = '12:00pm - 14:00apm'
    if(contador8 > maximo):
        maximo = contador8
        rango = '14:00pm - 16:00pm'
    if(contador9 > maximo):
        maximo = contador9
        rango = '16:00pm - 18:00pm'
    if(contador10 > maximo):
        maximo = contador10
        rango = '18:00pm - 20:00pm'
    if(contador11 > maximo):
        maximo = contador11
        rango = '20:00pm - 22:00pm'
    if(contador12 > maximo):
        maximo = contador12
        rango = '22:00pm - 00:00am'    

    resultado = [maximo, rango] 
    return resultado

estadocritico = []
estadograve = []
estadoleve = []
estadoestable = []
horaspacientes = []
horaspacientesanormales = []
contadorhorainhabil = 0
contadorhorariopunta = 0
pacientes = open('pacientes2.txt', 'r')
linealeida = pacientes.readline().strip()
while(linealeida != ""):
    lineasplit = linealeida.split(";")
    if(lineasplit[0] != "hora"):
        presionsis = funcionsistolica(lineasplit[3])
        pulso = int(lineasplit[2])
        temperatura = lineasplit[4].replace(',','.')
        temperatura = float(temperatura)
        respiratoria = int(lineasplit[5])
        estado = funcionestado(presionsis, pulso , temperatura, respiratoria)
        if(estado == 'pacientecritico'):
            estadocritico.append(lineasplit[1])
        elif(estado == 'pacientegrave'):
            estadograve.append(lineasplit[1])
        elif(estado == 'pacienteleve'):
            estadoleve.append(lineasplit[1])
        elif(estado == 'pacienteestable'):
            estadoestable.append(lineasplit[1])
        horaleida = lineasplit[0].replace(',','.')
        horaleida = float(horaleida)
        horaspacientes.append(horaleida)
        if(horaleida >= 20.0 or horaleida <= 8.0):
            contadorhorainhabil += 1
        if(estado == 'pacienteestable' and horaleida >= 18.0 and horaleida <= 21.0):
            contadorhorariopunta += 1
        if(pulso < 50 or pulso > 120):
             horaspacientesanormales.append(horaleida)
        linealeida = pacientes.readline().strip()
    else:
        linealeida = pacientes.readline().strip()
print(contadorhorainhabil, 'personas fueron en horario inhabil')
porcentajecriticos = (len(estadocritico) * 100)/(len(estadocritico) + len(estadoestable) + len(estadograve) + len(estadoleve))
porcentajegraves = (len(estadograve) * 100)/(len(estadocritico) + len(estadoestable) + len(estadograve) + len(estadoleve))
print('Hay', porcentajecriticos, '% pacientes criticos del total')
print('Hay', porcentajegraves, '% pacientes graves del total')
print('Hay', contadorhorariopunta, 'personas estables y que llegaron en horario punta')
listarangomayor = funcionrangohoras(horaspacientes)
numeromayor = listarangomayor[0]
horariomayor = listarangomayor[1]
print('El rango de horario con mas pacientes fue entre', horariomayor, 'hubieron', numeromayor,)
listarangoanormales = funcionrangohoras(horaspacientesanormales)
numeromayoranormales = listarangoanormales[0]
horariomayoranormales = listarangoanormales[1]
print('El rango de horario con mas pacientes con pulso anormal fue entre', horariomayoranormales, 'hubieron', numeromayoranormales,)
# maximo, contMax = rango(horas)

# print('El rango mas concurrido fue el', maximo, 'con un total de', contMax, 'pacientes\n')

# maximoAn, contAn = rango(horasAn)

# print('El rango mas concurrido con pacientes de pulso anormal (critico y grave) fue el', maximoAn, 'con un total de', contAn, 'pacientes')