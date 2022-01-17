"""
                                        Ejercicio 5
Enunciado: Convierte un Excel a CSV
Objetivo:
    - Aprender a trabajar con ficheros
    - Usar la librería pandas de Python

Recursos:
# Leer un fichero xlsx en Python (si hay mas de una hoja se puede especificar con sheet_name='example')
# Por defecto se utiliza la primera linea como cabecera de nombre para columnas, si no fuera asi se puede evitar con
# la propiedad header=None.
# Si queremos ignorar una o mas filas lo podemos hacer con skiprows = (numero entero de la fila). Ej: skiprows = 1
# Con sheet_name=None lo que hacemos es mostrar todo el documento, independientemente de las hojas que tenga
# Hay que instalar openpyxl usando  en la terminal-->  pip install openpyxl
"""

import pandas

# rutaExcel = "C:/excelPython.xlsx"
rutaExcel = input("Introduce la ruta y nombre del archivo: \n")

leerExcel = pandas.read_excel(io=rutaExcel+'.xlsx', sheet_name=None)
print("\tMostramos el contenido del fichero Excel: ")
print(leerExcel)

print("Segundo paso")

# Guardamos el archivo de tipo diccionario para posteriormente guardarlo como csv
csvTemporal=()
for i in leerExcel.items():
    # concatenamos tuplas vacias con las tuplas que devuelve el archivo excel
    csvTemporal = csvTemporal + i

print("**************************************************************************\nDiccionario temporal leido del xlsx")
print(csvTemporal)

guardarCSV = pandas.DataFrame(csvTemporal)
guardarCSV.to_csv('PruebaCsv.csv', sep=';')



leerCSV = pandas.read_csv('PruebaCsv.csv')
print("*************************************************************************\nMostramos el archivo csv: ")
print(leerCSV)
