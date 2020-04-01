#desafio 4: valentina corday y felipe urra 

def sacarpresionsistiolica(presion):
  presionsd = presion.split("/")
  ps = presionsd[0]
  return int(ps)

def catalogar(pulso,ps,temperatura,fr,critico,grave,leve,estable,hora,establepunta):
    if pulso < 30 or pulso > 150 or ps < 40 or ps > 180 or temperatura >= 42:
        critico += 1
    elif pulso < 50 or pulso > 120 or ps < 60 or ps > 150 or temperatura >= 40.5 or fr < 15 or fr > 20:
        grave += 1
    elif pulso < 60 or pulso > 90 or ps < 90 or ps > 120 or temperatura >= 37.3:
        leve += 1
    elif pulso >= 60 and pulso <= 90 or ps >= 90 and ps <= 120 or temperatura > 36.6 and temperatura <= 37.2 or fr >= 15 and fr <= 20:
        estable += 1
        print(hora)
        if hora > 18 and hora < 21:
            establepunta += 1
            print(establepunta)
    return

def rangos(horas):
  rango1 = 0 # de 00:00 a 01:59
  rango2 = 0 # de 02:00 a 03.59
  rango3 = 0 # de 04:00 a 05.59
  rango4 = 0 # de 06:00 a 07:59
  rango5 = 0 # de 08:00 a 09:59
  rango6 = 0 # de 10:00 a 11:59
  rango7 = 0 # de 12:00 a 13:59
  rango8 = 0 # de 14:00 a 15:59
  rango9 = 0 # de 16:00 a 17:59
  rango10 = 0 # de 18:00 a 19.59
  rango11 = 0 # de 20:00 a 21:59
  rango12 = 0 # de 22:00 a 23:59

  for h in horas: 
    if h >= 0 and h < 1.9:
      rango1 += 1
    elif h >= 2 and h < 3.9:
      rango2 += 1
    elif h >= 4 and h < 5.9:
      rango3 += 1
    elif h >= 6 and h < 7.9:
      rango4 += 1
    elif h >= 8 and h < 9.9:
      rango5 += 1
    elif h >= 10 and h < 11.9:
      rango6 += 1
    elif h >= 12 and h < 13.9:
      rango7 += 1
    elif h >= 14 and h < 15.9:
      rango8 += 1
    elif h >= 16 and h < 17.9:
      rango9 += 1
    elif h >= 18 and h < 19.9:
      rango10 += 1
    elif h >= 20 and h < 21.9:
      rango11 += 1
    elif h >= 22 and h < 23.9:
      rango12 += 1

  maximo = -9999999
  if rango1 > maximo:
    maximo = rango1
  if rango2 > maximo:
    maximo = rango2
  if rango3 > maximo:
    maximo = rango3
  if rango4 > maximo:
    maximo = rango4
  if rango5 > maximo:
    maximo = rango5
  if rango6 > maximo:
    maximo = rango6
  if rango7 > maximo:
    maximo = rango7
  if rango8 > maximo:
    maximo = rango8
  if rango9 > maximo:
    maximo = rango9
  if rango10 > maximo:
    maximo = rango10
  if rango11 > maximo:
    maximo = rango11
  if rango12 > maximo:
    maximo = rango12

  return maximo
    

pacientes = 0

inhabil = 0
establepunta = 0

critico = 0
grave = 0
leve = 0 
estable = 0

listahoras = []

#archivo
archivo = open("pacientes2.txt","r")
linea = archivo.readline().strip()
while linea != "":
  partes = linea.split(";")

  h = partes[0]
  h = h.replace(",",".")
  h = float(h)
  listahoras.append(h)

  nombre = str(partes[1])

  pulso = int(partes[2])

  presion = partes[3]
  presionsist = sacarpresionsistiolica(presion)

  temperatura = partes[4]
  temperatura = temperatura.replace(",",".")
  temperatura = float(temperatura)

  fr = int(partes[5])

  catalogar(pulso,presionsist,temperatura,fr,critico,grave,leve,estable,h,establepunta)

  #hora
  if h > 20 or h < 8:
    inhabil += 1 

  pacientes += 1
  
  linea = archivo.readline().strip()

rangomaximo = rangos(listahoras)

#preguntas
#1. Cantidad de pacientes llegados en horario inhábil. (Se considera horario inhábil entre las 20:00 hrs y 08:00 hrs).
print("llegaron", inhabil, "pacientes en horario inhabil")

#2. % de pacientes graves y % de pacientes críticos respecto del total. 
pgraves = ((grave/pacientes)*100)
pcriticos = ((critico/pacientes)*100)
print(pgraves,"% de pacientes graves y ", pcriticos,"% de pacientes criticos, con respecto al total")

#3. Número de pacientes estables llegados en horario punta. Considere el horario punta entre las 18:00 y 21:00 hrs. 
print("llegaron", establepunta, "pacientes en hora punta")

#4. Rango horario en el que llegaron más pacientes. Asuma que cada rango es de 2 horas (08:00 a 09:59, 10:00 a 11:59, 12:00 a 13:59, etc).

#5. Rango horario en el que hubo más pacientes con pulso anormal. 