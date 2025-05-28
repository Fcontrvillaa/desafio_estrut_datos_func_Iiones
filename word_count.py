import sys

archivo = sys.argv[1]


#leer archivo
with open(archivo, "r", encoding="utf-8") as f:
    #print(f.read())
    texto = f.read()

#print (texto)

total_letras = len(texto)




total_palabras = texto.split
print(total_letras)
#print(f" {total_palabras}")