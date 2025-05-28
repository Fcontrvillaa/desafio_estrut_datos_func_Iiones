import sys

archivo = sys.argv[1]


#leer archivo
with open(archivo, "r", encoding="utf-8") as f:
    #print(f.read())
    texto = f.read()
#print (texto)

# cuenta palabras
total_palabras = texto.split()
print (len(total_palabras))


# cuenta letras
total_letras = texto.replace(" ","")
total_letras = texto.replace(".","")
#total_letras = texto.lower
print (len(total_letras))
#total_letras = len(texto)

#print(dir(texto))




#total_palabras = texto.split
#print(total_letras)
#print(f" {total_palabras}")