def rangomaximopacientesfuncion(horastotales):
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    cont9 = 0
    cont10 = 0
    cont11 = 0
    cont12 = 0
    cont13 = 0
    cont14 = 0
    
    for horaleida in horastotales:
        if(horaleida >= 0 and horaleida < 2):
            cont3 += 1
        elif(horaleida >= 2 and horaleida < 4):
            cont4 += 1
        elif(horaleida >= 4 and horaleida < 6):
            cont5 += 1
        elif(horaleida >= 6 and horaleida < 8):
            cont6 += 1
        elif(horaleida >= 8 and horaleida < 10):
            cont7 += 1
        elif(horaleida >= 10 and horaleida < 12):
            cont8 += 1
        elif(horaleida >= 12 and horaleida < 14):
            cont9 += 1
        elif(horaleida >= 14 and horaleida < 16):
            cont10 += 1
        elif(horaleida >= 16 and horaleida < 18):
            cont11 += 1
        elif(horaleida >= 18 and horaleida < 20):
            cont12 += 1
        elif(horaleida >= 20 and horaleida < 22):
            cont13 += 1
        elif(horaleida >= 22 and horaleida < 24):
            cont14 += 1

    rangomaximo = ''
    maximopac = -999999
    if(cont3 > maximopac):
        rangomaximo = '0am a 2am'
        maximopac = cont3
    if(cont4 > maximopac):
        rangomaximo = '2am a 4am'
        maximopac = cont4
    if(cont5 > maximopac):
        rangomaximo = '4am a 6am'
        maximopac = cont5
    if(cont6 > maximopac):
        rangomaximo = '6am a 8am'
        maximopac = cont6
    if(cont7 > maximopac):
        rangomaximo = '8am a 10am'
        maximopac = cont7
    if(cont8 > maximopac):
        rangomaximo = '10am a 12pm'
        maximopac = cont8
    if(cont9 > maximopac):
        rangomaximo = '12pm a 14pm'
        maximopac = cont9
    if(cont10 > maximopac):
        rangomaximo = '14pm a 16pm'
        maximopac = cont10
    if(cont11 > maximopac):
        rangomaximo = '16pm a 18pm'
        maximopac = cont11
    if(cont12 > maximopac):
        rangomaximo = '18pm a 20pm'
        maximopac = cont12
    if(cont13 > maximopac):
        rangomaximo = '20pm a 22pm'
        maximopac = cont13
    if(cont12 > maximopac):
        rangomaximo = '22pm a 0am'
        maximopac = cont12    
 
    return rangomaximo

def llenarestadosfuncion(crit, gra, leve, estab, estado, nombre):
    if(estado == 'critico'):
        crit.append(nombre)
    elif(estado == 'grave'):
        gra.append(nombre)
    elif(estado == 'leve'):
        leve.append(nombre)
    elif(estado == 'estable'):
        estab.append(nombre)

def presionsistolicafuncion(presion):
    presiones = presion.split("/") 
    presionsistolica = presiones[0]
    return int(presionsistolica)

def estadopacientefuncion(presion, pulso, temperatura, respiratoria):
    estado = ""
    if(presion >= 90 and presion <= 120 or pulso >= 60 and pulso <= 90 or temperatura >= 36.6 and temperatura <= 37.2 or respiratoria >= 15 and respiratoria <= 20):
        estado = 'estable'
    if(presion < 90 or presion > 120 or pulso < 60 or pulso > 90 or temperatura >= 37.3):
        estado = 'leve'
    if(presion < 60 or presion > 150 or pulso < 50 or pulso > 120 or temperatura >= 40.5 or respiratoria < 15 or respiratoria > 20):
        estado = 'grave'
    if(presion < 40 or presion > 180 or pulso < 30 or pulso > 150 or temperatura >= 42):
        estado = 'critico'
    return estado

crit = []
gra = []
leve = []
estab = []

horastotales = []
horastotalespacientesan = []

cont1 = 0
cont2 = 0
contadorhorariopunta = 0
pacientesarchivo = open('pacientes2.txt', 'r')
linea = pacientesarchivo.readline().strip()
while(linea != ""):
    lineas = linea.split(";")
    if(lineas[0] == "hora"):
        linea = pacientesarchivo.readline().strip()
    else:
        hora = lineas[0]
        hora2 = hora.replace(',','.')
        hora2 = float(hora2)
        horastotales.append(hora2)

        nombre = lineas[1]

        presion = lineas[3]
        presionsistolica = presionsistolicafuncion(presion)

        pulso = int(lineas[2])
        if(pulso < 60 or pulso > 90):
             horastotalespacientesan.append(hora2)
       
        temperatura = lineas[4]
        temperatura = temperatura.replace(',','.')
        temperatura2 = float(temperatura)

        resp = int(lineas[5])
    
        estadopaciente = estadopacientefuncion(presionsistolica, pulso , temperatura2, resp)
        llenarestadosfuncion(crit,gra,leve,estab,estadopaciente,nombre)

        if(hora2 >= 18 and hora2 <= 21 and estadopaciente == 'estable'):
            cont1 += 1        
        if(hora2 <= 8 or hora2 >= 20):
            cont2 += 1        
        linea = pacientesarchivo.readline().strip()
print("Pregunta 1:")
print(cont2, 'paccientesconcurrieron en horario inhabil')
pacientestotales = len(crit) + len(estab) + len(gra) + len(leve)
porc1 = (len(crit) * 100)/pacientestotales
porc2 = (len(gra) * 100)/pacientestotales
print("Pregunta 2:")
print('Del total de pacientes hay', porc1, '% de pacientes criticos ')
print('Del total de pacientes hay', porc2, '% de pacientes graves ')
print("Pregunta 3:")
print(cont1, 'pacientes llegaron en horario punta y que ademas su estado es estable')
print("Pregunta 4:")
print("Rango de horario con mayor cantidad de pacientes")
rangomaximopacientes = rangomaximopacientesfuncion(horastotales)
print(rangomaximopacientes)
print("Pregunta 5:")
print("Rango de horario con mayor cantidad de pacientes que tienen un pulso no estable")
rangomaximopacientesanormales = rangomaximopacientesfuncion(horastotalespacientesan)
print(rangomaximopacientesanormales)