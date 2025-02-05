# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import wfdb # Libreria para que lea los archivos .hea y .dat
import matplotlib.pyplot as plt # Libreria para graficar
import numpy as np #Libreria para sacar las operaciones estadisticas
import random #Libreria para sacar valores aleatorios
import math # Libreria de operaciones matematicas

archivo_hea = 'C:\\Users\\HP RY5\\Downloads\\a01.hea' #Direecion de el archivo .hea
archivo_dat = 'C:\\Users\\HP RY5\\Downloads\\a01.dat' #Direccion del archivo .dat

recorte = wfdb.rdrecord('C:\\Users\\HP RY5\\Downloads\\a01' ) #lee los registros de la señal 
conversion = recorte.p_signal [:,0] #selecciona las filas de los datos pero solo la primera columna
frecuencia=recorte.fs #Devuelve la frecuencia de muestreo en Hz, indica cuantas muestras por segundo se tomaron 

muestras=conversion.shape[0] #Asigna a la variable muestras el numero total de elementos
Tiempo=[i/frecuencia for i in range (muestras)] #el ciclo for recorre todos los valores que tome i generados por el range que seria de 0 a muestras, y para cada valor ue tome i se divide por la frecuencia para que quede almacenado en la variable tiempo  

#Graficar la señal
Fraccion=int (10*frecuencia) #se almacena en la variable el numero de muestras correspondientes a 10 segundos por la multiplicacion de 10 por la frecuencia de muestreo y este debe ser un numero entero 
plt.figure(figsize=(10, 5))# se crea la imagen y Da el tamaño, el alto y el ancho 
plt.plot(Tiempo[:Fraccion], conversion[:Fraccion], label='Primeros 10 segundos')#dibuja el diagrama con las muestras correspondientes a los primeros 10 segundos, en el eje x el tiempo en s y en el eje y los valores que correnponden a cada tiempo en mv 
plt.title("Señal Fisiológica") # coloca el titulo del grafico
plt.xlabel("Tiempo (s)") #da el nombre del eje x 
plt.ylabel("Amplitud (mv)")# da el nombre del eje y 
plt.legend()# muestras el label de los primeros 10 segundos 
plt.grid() #muestra la cuadricula en el grafico 
plt.show() #muestra el grafico 

# Media de la señal 
total=0 # se inicializa la variable con 0 
for r in conversion : #se utiliza un ciclo for para hacer la suma total de los datos que estan en la variable conversion 
   total += r # se almacena en la variable total el numero de datos que se van sumando 
media=total/len(conversion) #se halla la media con el total de datos dividio el numero de datos que hay 
media2=np.mean(conversion) #se halla la media pero mediante la libreria enteriormente mencionada 
 
#Desviacion estandar de la señal 
suma_cuadrados=0 #se inicializa la varible en cero 
for x in conversion:# se utiliza un ciclo for para que x valla tomando cada valor de conversion 
    diferencia=x-media # en este ciclo se halla la diferencia de cada valor tomado por x menos la media 
    potencia=diferencia**2 #dentro del ciclo se eleva al cuadrado la cada valor que valla tomando diferencia
    suma_cuadrados += potencia #se va sumando cada potencia 
    
varianza= suma_cuadrados/len (conversion) #se halla la varinaza con la suma de las potencias dividido entre el numero de datos 
varianza2=np.var(conversion[:Fraccion])#Se halla la varianza de los datos de los 10 primeros segundos
desviacion_estandar= varianza**0.5# se halla la desviacion estandar al calculale la raiz cuadrada a la varianza 
desviacion2=np.std(conversion) #se halla la desviacion utilizando la libreria 
coeficiente_variacion=(desviacion_estandar/media)*100 #se calcula el coeficiente de variacion con la formula que es desviacion estandar sobre la media por cien 

#Histograma 
plt.figure(figsize=(10, 5)) #crea un grafico y se le da unas medidas a la imagen 
plt.hist(conversion, bins=60, color='purple', alpha=0.7) #dibuja el histograma el cual contiene la variable conversion el cual contiene los valores de la señal, el numero de columnas que se quieren en el histograma, el color y ajusta la opacidad de las barras
plt.title("Histograma de la Señal Fisiológica") #Da el nombre al grafico 
plt.xlabel("Amplitud (mV)") #nombre del eje x 
plt.ylabel("Frecuencia (Hz)") #nombre del eje y
plt.grid(True) #muestra la cuadricula 
plt.show() #muestra el grafico 

ordenar_datos=np.sort(conversion) #se ordenan los datos de la señal lamcenados en conversion de menor a mayor 
numero_datos = len(ordenar_datos) #numero_datos almacena la cantidad de datos ordenados que hay en ordenar datos
funcion_probabilidad = [] #se crea un array vacio
for i in range(numero_datos): #se crea un ciclo for 
    funcion_probabilidad.append((i + 1) / numero_datos ) #funcion que itera los datos y crea la probabilidad en funcion de la imagen
plt.figure(figsize=(10, 5))
plt.plot(ordenar_datos, funcion_probabilidad, marker='.', linestyle='none', color='green')
plt.title("Función de Probabilidad de la Señal Fisiológica calculada")
plt.xlabel("Amplitud (mV)")
plt.ylabel("Probabilidad Acumulada")
plt.grid(True)
plt.show()

ordenar_datos=np.sort(conversion)#se ordenan los datos de la señal lamcenados en conversion de menor a mayor 
funcion=np.arange(1,len(ordenar_datos)+1)/len (ordenar_datos) #se genera un arreglo con numeros desde el 1 al total de datos y se divide entre el numero de datos, esto indica la fracion del total de datos que son menores o iguales a cada valor en el arreglo ordenado 
plt.figure(figsize=(10, 5)) #crea la figura y le da un ancho y un alto 
plt.plot(ordenar_datos, funcion, marker='.', linestyle='none', color='green')#dibuja el digarma el cual tiene los datos ordenados, los datos de la variable funcion, se utiliza un punto para marcar cada valor y se establece un color a la grafica  
plt.title("Función de Probabilidad de la Señal Fisiológica con la libreria") #se le asigna un titulo al grafico 
plt.xlabel("Amplitud (mV)") #se le da nombre al eje x 
plt.ylabel("Probabilidad Acumulada") #se le nombre al eje y 
plt.grid(True) #muestra la cuadricula en la grafica 
plt.show()# muestra el grafico 

print ("la media es:", media, "mv") #muestra la media anteriormente calculada
print ("la media es:", media2, "mv")#muestra la media anteriormente calculada por medio de la libreria 
print ("la varianza es:", varianza2) #muestra la varianza anteriormente calculada
print ("la desviacion estandar es:", desviacion_estandar)#muestra la desviacion estandar anteriormente calculada
print ("la desviacion estandar es:", desviacion2) #muestra la desviacion estandar anteriormente calculada por medio de la libreria 
print ("el coeficiente de variacion es:", coeficiente_variacion, "%") #muestra el coeficiente de variacion

# Relacion señal Ruido: es una medida que compara el nivel de la señal útil con el nivel del ruido no deseado en un sistema. Se expresa en decibeles (dB), se calcula como la potencia de la señal sobre la potencia del ruido 
ruido_gaussiano=conversion.copy() #crea una copia de los datos almacenados en coversion
for j in range(Fraccion): # se hace un ciclo for para ir tomando cada valor desde 0 hasta fraccion
    ruido=random.gauss(0,0.01) #genera un numero aleatorio con la distribucion gaussina con una media de cero y una desviacion estandar de 0.1 para que tenga una pequeña variabilidad y el ruido no se desplace hacia arriba o hacia abajo para tener bajo ruido 
    ruido_gaussiano[j] += ruido #A la variable ruido_gaussiano se le suma cada valor que tome ruido en el indice j 

ruido_gaussiano2 = conversion.copy() #crea una copia de los datos almacenados en coversion
desviacion_alto = np.sqrt(varianza2 / 100)#obtenemos la desviacion estandar del ruido, la varianza de la señal original la dividimos entre 100 para reducir la magnitud del ruido 
for n in range(Fraccion): # se hace un ciclo for para ir tomando cada valor desde 0 hasta fraccion que son los 10 primeros segundos 
    ruido2 = random.gauss(desviacion_alto) #Se da una mayor desviacion estandar para dar mas ruido a la señal 
    ruido_gaussiano2[n] += ruido2 #A la variable ruido_gaussiano2 se le suma cada valor que tome ruido en el indice n
    
ruidogaus=0 #se inicializa la variable en cero 
for k in ruido_gaussiano:#se utiliza un ciclo for para que valla sumando cada valor que toma ruido_gaussiano
    ruidogaus += k #variable que suma cada valor que va tomando k
    mediagaus= ruidogaus/muestras #se calcula la media con la suma de todos los datos dividio entre el numero de muestras  

des=0 #se inicaliza una variable en cero
for l in ruido_gaussiano: #se utiliza un ciclo for para que valla tomando cada valor almacenado en ruido_gaussiano
    diferencia2=l-mediagaus #A cada valor que toma l se le resta la media anteriormente calculada
    potencia2=diferencia2**2#a cada diferencia se eleva al cuadrado 
    des += potencia2 #a la variable inicializada en cero se le suma cada valor que tome la potencia2
    varianzagaus=des/muestras #la varianza es igual a la suma de todos los datos almacenados en des dividido entre el numero total de muestras
    
SNR=varianza2/varianzagaus #la relacion señal ruido se calcula con la varianza de la señal original durante los 10 primeros segundos dividido entre la varianza obtenida de la agrgacion del ruido Gauss 
SNR_dB = 10 * math.log10(SNR) #se para el SNR en dB mediante la formula utilizando la libreria math
ruidogaus2=0 #se inicializa la variable en cero 
for m in ruido_gaussiano2:#se utiliza un ciclo for para que valla sumando cada valor que toma ruido_gaussiano
    ruidogaus2 += m #variable que suma cada valor que va tomando k
    mediagaus2= ruidogaus2/muestras #se calcula la media con la suma de todos los datos dividio entre el numero de muestras  

des2=0 #se inicaliza una variable en cero
for l in ruido_gaussiano2: #se utiliza un ciclo for para que valla tomando cada valor almacenado en ruido_gaussiano
    diferencia2=l-mediagaus2 #A cada valor que toma l se le resta la media anteriormente calculada
    potencia2=diferencia2**2#a cada diferencia se eleva al cuadrado 
    des2 += potencia2 #a la variable inicializada en cero se le suma cada valor que tome la potencia2
    varianzagaus2=des2/muestras #la varianza es igual a la suma de todos los datos almacenados en des dividido entre el numero total de muestras
    
SNR2=varianza2/varianzagaus2 #la relacion señal ruido se calcula con la varianza de la señal original durante los 10 primeros segundos dividido entre la varianza obtenida de la agrgacion del ruido Gauss 
SNR_dB2 = 10 * math.log10(SNR2) #se para el SNR en dB mediante la formula utilizando la libreria math
plt.figure(figsize=(10, 5))#crea un grafico y se le da unas medidas a la imagen 
plt.plot(Tiempo[:Fraccion], ruido_gaussiano[:Fraccion], label='Señal con ruido gaussiano', color='red') #dibuja el digrama con las muestras correspondientes a los 10 primeros segundos y con la agregacion del ruido en los 10 primeros segundos  
plt.title("Señal Fisiológica con Ruido Gaussiano (Primeros 10s)") #se le agrega un titulo al diagrama
plt.xlabel("Tiempo (s)")#se le da un nombre al eje x 
plt.ylabel("Amplitud (mv)")#se le da un nombre al eje y
plt.legend()# muestra en label 
plt.grid()#muestra la cuadricula en el grafico 
plt.show()#muestra el grafico 

ruido_impulso=[] #se crea una lista vacia 
for a in conversion[:Fraccion]: #se hace un ciclo for para que valla tomando cada valor almacenado desde 0 hasta la fraccion 10 segundos 
    if random.random()<0.1: #si se genera un numero entre 0 y 1 y si este numero es menor a 0.1 se ejecuta la siguiente accion   
       ruidoim=random.uniform(-1,1)# si se cumple lo anterior se genera un numero aleatorio entre -1 y 1 que genera el ruido impulsivo, se escoge este rango para alterar la señal y no distorcionarla tanto
       sumaimpul=ruidoim+a #se suma el valor de ruido impulsivo al valor que valla tomando a 
       ruido_impulso.append(sumaimpul) #se agrega el nuevo valor de ruido a la lista 
    else:#si no se cumple lo anterior ejecute lo siguiente 
        ruido_impulso.append(a) #si no se cumple lo anterior se guarda el valor original de la señal modificada 
ruido_impulso2=[] #se crea una lista vacia para menos ruido
for o in conversion[:Fraccion]: #se hace un ciclo for para que valla tomando cada valor almacenado desde 0 hasta la fraccion 10 segundos
    if random.random()<0.01:#si se genera un numero entre 0 y 0.01 para menor probabilidad de ruido, se ejecuta la siguiente accion 
       ruidoim2=random.uniform(-0.1,0.1) # si se cumple lo anterior se genera un numero aleatorio entre -0.1 y 0.1 que genera el ruido impulsivo, se escoge este rango para tener menor rango de ruido 
       sumaimpul2=ruidoim+a#se suma el valor de ruido impulsivo al valor que valla tomando a
       ruido_impulso2.append(sumaimpul2) #se agrega el nuevo valor de ruido a la lista 
    else: #si no se cumple lo anterior ejecute lo siguiente 
        ruido_impulso2.append(o) #si no se cumple lo anterior se guarda el valor original de la señal modificada
ruidoimpulso=0 #se inicializa la variable en 0
for b in ruido_impulso:#se crea un ciclo for para que se valla lellendo cada dato de ruido_impulso y con cada valor ejecutar lo siguente: 
    ruidoimpulso += b #se va sumando cada valor para hallar el total 
    mediaimpul= ruidoimpulso/muestras #se calcula la media mediente el valor total anterior dividido el numero total de muestras 
    
vari=0 #se inicializa la variable en 0
for z in ruido_impulso: #se crea un ciclo for para que se vaya leyendo cada dato de ruido_impulso y con cada valor ejecutar lo siguente:
    diferenciaim=z-mediaimpul #se halla la diferencia entre cada valor que vaya tomando z y se le resta la media 
    potenciaimpul=diferenciaim**2 #se eleva al cuadrado la diferencia anterior calculada de cada numero 
    vari += potenciaimpul #se suma cada potencia para tener la suma total 
    varianzaimpulso=vari/muestras #para hallar la varianza divido el total entre el numero total de muestras 
    
SNRim=varianza2/varianzaimpulso #se halla el SNR entre la varianza de la señal dividido la varianza del ruido impulso para un mayor ruido 
SNRim_dB = 10 * math.log10(SNRim)#se pasa el SNR en dB mediante la libreria math 
ruidoimpulso2=0 #se inicializa la variable en 0
for q in ruido_impulso2: #se crea un ciclo for para que se vaya leyendo cada dato de ruido_impulso y con cada valor ejecutar lo siguente:
    ruidoimpulso2 += q #se va sumando cada valor para hallar el total 
    mediaimpul2= ruidoimpulso2/len(ruido_impulso2) #se calcula la media mediente el valor total anterior dividido el numero total del ruido 
    
vari2=0  #se inicializa la variable en 0
for t in ruido_impulso2: #se crea un ciclo for para que se vaya leyendo cada dato de ruido_impulso y con cada valor ejecutar lo siguente:
    diferenciaim2=t-mediaimpul2 #se halla la diferencia entre cada valor que vaya tomando z y se le resta la media
    potenciaimpul2=diferenciaim2**2 #se eleva al cuadrado la diferencia anterior calculada de cada numero
    vari2 += potenciaimpul2 #se suma cada potencia para tener la suma total 
    varianzaimpulso2=vari2/len(ruido_impulso2) #para hallar la varianza divido el total entre el numero total del ruido 
    
SNRim2=varianza2/varianzaimpulso2 #se halla el SNR entre la varianza de la señal dividido la varianza del ruido impulso para un menor ruido 
SNRim2_dB = 10 * math.log10(SNRim2) #se pasa el SNR en dB mediante la libreria math 
ruido_artefacto=[] #se crea una lista vacia para menor ruido 
for c, g in enumerate(conversion[:Fraccion]): #se crea un ciclo for para leer cada valor de la fraccion de los primeros 10 segundos, enumerate crea un indice c que se refiere al contador y un indice g valor de la señal en la posicion para generar la siguiente accion dentro del ciclo
    ruidoar=0.05* (c% 50==0) #se crea para que cada 50 muestras un verdadero representado con el 1 y un falso en los demas representado con 0 para que el ruido tenga 0.05 cada 50 muestras 
    sumaart=ruidoar+g # se suma el ruido a la señal g en esa posicion 
    ruido_artefacto.append(sumaart)#guarda el valor modificado 
ruido_artefacto2=[] #se crea una lista vacia para mayor ruido 
for h, ñ in enumerate(conversion[:Fraccion]): #se crea un ciclo for para leer cada valor de la fraccion de los primeros 10 segundos, enumerate crea un indice h que se refiere al contador y un indice ñ valor de la señal en la posicion para generar la siguiente accion dentro del ciclo
    ruidoar2=0.2* (h% 50==0) #se crea para que cada 50 muestras un verdadero representado con el 1 y un falso en los demas representado con 0 para que el ruido tenga 0.05 cada 50 muestras
    sumaart2=ruidoar2+ñ # se suma el ruido a la señal g en esa posicion 
    ruido_artefacto2.append(sumaart) #guarda el valor modificado 
ruidoartefacto=0 #inicializo una variable en 0
for v in ruido_artefacto: #se crea un ciclo for para llamar a cada valor del ruido artefacto y cumplir lo siguiente con cada uno:
    ruidoartefacto+= v #se va sumando cada valor para tener un valor total 
    mediaart=ruidoartefacto/len(ruido_artefacto) #el valor total obtenido se divide entre la cantidad de datos que hay en el ruido artefacto

artefacto=0 #Inicializa la variable artefacto, que se usará para calcular la varianza del ruido artefacto.
for p in ruido_artefacto : #se crea un ciclo for para representar la amplitud de la señal en cada muestra después de haber añadido el ruido artefacto.
    diferenciaart=p-mediaart # Esta diferencia mide cuánto se desvía cada punto de la media.
    potenciaart=diferenciaart**2 #Esto es parte de la fórmula de la varianza:
    artefacto += potenciaart #Para acumular todas las diferencias al cuadrado.

    varianza_artefacto=artefacto/len(ruido_artefacto) #Dividiendo la suma de las diferencias al cuadrado por el número total de muestras.
    
SNRart=varianza2/varianza_artefacto # Es la varianza de la señal original y el ruido artefacto que se agrego
SNRart_dB = 10 * math.log10(SNRart) #Convierte esta relación a decibeles (dB) usando la fórmula 
ruidoartefacto2=0 #Inicializa la variable artefacto, que se usará para calcular la varianza del ruido artefacto.
for s in ruido_artefacto2: #se crea un ciclo for para representar la amplitud de la señal en cada muestra después de haber añadido el ruido artefacto.
    ruidoartefacto2+= s #se va sumando cada valor para tener un valor total 
    mediaart2=ruidoartefacto2/muestras #el valor total obtenido se divide entre la cantidad de muestras  total

artefacto2=0 #Inicializa la variable artefacto, que se usará para calcular la varianza del ruido artefacto.
for w in ruido_artefacto2 : #se crea un ciclo for para representar la amplitud de la señal en cada muestra después de haber añadido el ruido artefacto.
    diferenciaart2=w-mediaart2 # Esta diferencia mide cuánto se desvía cada punto de la media.
    potenciaart2=diferenciaart2**2 #Esto es parte de la fórmula de la varianza:
    artefacto2 += potenciaart2#Para acumular todas las diferencias al cuadrado.
    varianza_artefacto2=artefacto2/muestras  #se divide la suma de las diferencias al cuadrado por el número total de muestras
    
SNRart2=varianza2/varianza_artefacto2 # Es la varianza de la señal original y el ruido artefacto que se agrego
SNRart2_dB = 10 * math.log10(SNRart2) #Convierte esta relación a decibeles (dB) usando la fórmula
    
print ("el SNR de contaminar la señal con ruido gaussiano menor a 10 dB es:", SNR_dB,  "dB") #muestra el SNR del ruido Gaussiano 
print ("el SNR de contaminar la señal con ruido gaussiano mayor a 10 dB es:", SNR_dB2,  "dB")   
print ("el SNR de contaminar la señal con ruido impulso mayor a 10 dB es:", SNRim2_dB, "dB")
print ("el SNR de contaminar la señal con ruido impulso menor a 10 dB es:", SNRim_dB, "dB")
print ("el SNR de contaminar la señal con ruido artfacto mayor a 10 dB es:", SNRart_dB, "dB") 
print ("el SNR de contaminar la señal con ruido artfacto menor a 10 dB es::", SNRart2_dB, "dB") 


 





