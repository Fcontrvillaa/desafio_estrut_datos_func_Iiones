import sys

archivo = sys.argv[1]

#leer archivo
with open(archivo, "r", encoding="utf-8") as f:
    #print(f.read())
    texto = f.read()
#print (texto)

# cuenta caracteres distintos
distintas_letras = set(texto)
print (len(distintas_letras))

# cuenta palabras distintas
total_palabras = texto.split()
distintas_palabras = set(total_palabras)
print (len(distintas_palabras))





