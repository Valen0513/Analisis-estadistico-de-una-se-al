# Analisis-estadistico-de-una-se-al
# -*- coding: utf-8 -*-



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

ordenar_datos=np.sort(conversion)#se ordenan los datos de la señal lamcenados en conversion de menor a mayor 
funcion=np.arange(1,len(ordenar_datos)+1)/len (ordenar_datos) #se genera un arreglo con numeros desde el 1 al total de datos y se divide entre el numero de datos, esto indica la fracion del total de datos que son menores o iguales a cada valor en el arreglo ordenado 
plt.figure(figsize=(10, 5)) #crea la figura y le da un ancho y un alto 
plt.plot(ordenar_datos, funcion, marker='.', linestyle='none', color='green')#dibuja el digarma el cual tiene los datos ordenados, los datos de la variable funcion, se utiliza un punto para marcar cada valor y se establece un color a la grafica  
plt.title("Función de Probabilidad de la Señal Fisiológica") #se le asigna un titulo al grafico 
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

ruido_gaussiano=conversion.copy() #crea una copia de los datos almacenados en coversion
for j in range(Fraccion): # se hace un ciclo for para ir tomando cada valor desde 0 hasta fraccion
    ruido=random.gauss(0,0.1) #genera un numero aleatorio con la distribucion gaussina con una media de cero y una desviacion estandar de 0.1 para que tenga una pequeña variabilidad y el ruido no se desplace hacia arriba o hacia abajo 
    ruido_gaussiano[j] += ruido #A la variable ruido_gaussiano se le suma cada valor que tome ruido en el indice j 

ruidogaus=0 #se inicializa la variable en cero 
for k in ruido_gaussiano:#se utiliza un ciclo for para que valla sumando cada valor que toma ruido_gaussiano
    ruidogaus += k #variable que suma cada valor que va tomando k
    mediagaus= ruidogaus/muestras #se calcula la media con la suma de todos los doatos dividio entre el numero de datos 

des=0 #se inicaliza una variable en cero
for l in ruido_gaussiano: #se utiliza un ciclo for para que valla tomando cada valor almacenado en ruido_gaussiano
    diferencia2=l-mediagaus #A cada valor que toma l se le resta la media anteriormente calculada
    potencia2=diferencia2**2#a cada diferencia se eleva al cuadrado 
    des += potencia2 #a la variable inicializada en cero se le suma cada valor que tome la potencia2
    varianzagaus=des/muestras #la varianza es igual a la suma de todos los datos almacenados en des dividido entre el numero total de muestras
    
SNR=varianza2/varianzagaus #la relacion señal ruido se calcula con la varianza de la señal original durante los 10 primeros segundos dividido entre la varianza obtenida de la agrgacion del ruido Gauss 
SNR_dB = 10 * math.log10(SNR) #se para el SNR en dB mediante la formula utilizando la libreria math

plt.figure(figsize=(10, 5))#crea un grafico y se le da unas medidas a la imagen 
plt.plot(Tiempo[:Fraccion], ruido_gaussiano[:Fraccion], label='Señal con ruido gaussiano', color='red') #dibuja el digrama con las muestras correspondientes a los 10 primeros segundos y con la agregacion del ruido en los 10 primeros segundos  
plt.title("Señal Fisiológica con Ruido Gaussiano (Primeros 10s)") #se le agrega un titulo al diagrama
plt.xlabel("Tiempo (s)")#se le da un nombre al eje x 
plt.ylabel("Amplitud (mv)")#se le da un nombre al eje y
plt.legend()# muestra en label 
plt.grid()#muestra la cuadricula en el grafico 
plt.show()#muestra el grafico 
