import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
datos ={"ID":[1,2,3,4,5,6,7,8,9,10],
        "Nombre":["Ana","Juan","Luis","Marta","Pedro","Sofía","Carlos","Elena","Miguel","Paula"],
        "Edad":[25,30,28,22,35,27,29,24,31,26],
        "Ingresos":[2500,3200,2800,2200,4100,2900,3100,2700,3300,2600],
        "Género":["Femenino","Masculino","Masculino","Femenino","Masculino","Femenino","Masculino","Femenino","Masculino","Femenino"],
        "Cuidad":["Lima","Bogotá","Lima","Quito","Santiago","Lima","Buenos_Aires","Quito","Santiago","Buenos_Aires"]}
df=pd.DataFrame(datos)
print(f"\n",df)

# 1. Definir Variables (2 puntos)
# ● Identificar el tipo de variable (categórica, cuantitativa discreta o continua) de cada columna 
# en el conjunto de datos.
# ID: Cuantitativa discreta / Categórica nominal
# Nombre: Categórica nominal
# Edad: Cuantitativa discreta
# Ingresos: Cuantitativa 
# Genero: Categórica nominal
# Ciudad: Categorico nominal

# 2. Construcción de una Tabla de Frecuencia (2 puntos)
# ● Generar una tabla de frecuencia para una variable categórica y otra para una variable 
# cuantitativa discreta

# Tabla Frecuencia Variable Cuantitativa "Ingresos"
tabla_frecuencia = df['Ingresos'].value_counts().sort_index().to_frame('Frecuencia Absoluta')
tabla_frecuencia["Frecuencia Relativa"] = tabla_frecuencia["Frecuencia Absoluta"] / tabla_frecuencia["Frecuencia Absoluta"].sum()
tabla_frecuencia["Frecuencia Acumulada"] = tabla_frecuencia["Frecuencia Absoluta"].cumsum()
tabla_frecuencia["Frecuencia Relativa Acumulada"] = tabla_frecuencia["Frecuencia Relativa"].cumsum()
print(f"\n",tabla_frecuencia)
# Tabla Frecuencia Variable Categórica "Género"
frecuencia_genero = df["Género"].value_counts().sort_index().to_frame('Frecuencia Absoluta')
frecuencia_genero["Frecuencia Relativa"] = frecuencia_genero["Frecuencia Absoluta"] / frecuencia_genero["Frecuencia Absoluta"].sum()
frecuencia_genero["Frecuencia Acumulada"] = frecuencia_genero["Frecuencia Absoluta"].cumsum()
frecuencia_genero["Frecuencia Relativa Acumulada"] = frecuencia_genero["Frecuencia Relativa"].cumsum()
print(f"\n",frecuencia_genero)
# 3. Cálculo de Medidas de Tendencia Central (2 puntos)
# ● Calcular la media, mediana y moda de una variable cuantitativa
media_edad = df["Edad"].mean()
mediana_edad = df["Edad"].median()
moda_edad = df["Edad"].mode()[0]
print(f"\nLa media de la edad es:",media_edad)
print(f"\nLa mediana de la edad es:",mediana_edad)
print(f"\nLa moda de la edad es:",moda_edad)

# 4. Cálculo de Medidas de Dispersión (2 puntos) 
# ● Calcular el rango, varianza y desviación estándar de la misma variable utilizada en el punto anterior. 
datos = df["Edad"]
minimo_edad = min(datos)
maximo_edad = max(datos)
print(f"\nLa edad minima es de:",minimo_edad,"años")
print(f"\nLa edad maxima es de:",maximo_edad,"años")
rango = max(datos)-min(datos)
print(f"\nEl rango de variación de la Edad es de:",rango,"años")
varianza_poblacional = np.var(datos)
varianza_muestral = np.var(datos, ddof=1)
print(f"\nLa varianza poblacional es de:",varianza_poblacional,"años")
print(f"\nLa varianza muestral es de:",varianza_muestral,"años")
desviacion_poblacional = np.std(datos)
desviacion_muestral = np.std(datos, ddof=1)
print(f"\nLa desviación estandar de la edad es de:",desviacion_poblacional,"años")
print(f"\nLa desviación muestral de la edad es de:",desviacion_muestral,"años")

# 5. Visualización de Datos (2 puntos) 
# Crear un histograma para una variable cuantitativa y un boxplot para otra variable del dataset. 
plt.hist(df["Ingresos"], bins=5, edgecolor="black")
plt.xlabel("Frecuencia")
plt.ylabel("Ingresos")
plt.title("Histograma de Datos de los Ingresos")
plt.show()

sns.boxplot(x=df["Edad"])
plt.title("Boxplot de Datos de Edad")
plt.show()