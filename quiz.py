# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a=input("dijite el valor de a: ")
a= int(a)
b=input("dijite el valor de b: ")
b= int(b)
c=input("dijite el valor de c: ")
c=int(c)
# processing
if (a+b)>c:
    r="si forma triangulo"
else:
    (a+b)<c
    r="no forma un triangulo" 
    if (b+c)>c:
        r="si forma un triangulo"
    else:
        (b+c)<c
    r="no forma un triangulo"
    if (a+c)<c:
        r="si forman un triangulo"
    else:
        (a+b)<c
        r="no forman un triangulo"

# output
print("  respuesta: " + str(r))