def calcula_grado(grado):
    if grado < 0.0 or grado > 1.0:
        return "score incorrecto"
    elif grado > 0.9:
        return "A"
    elif grado > 0.8:
        return "B"
    elif grado > 0.7:
        return "C"
    elif grado > 0.6:
        return "D"
    else: 
        return "F"
   


def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: " ))
    y = calcula_grado(x) 
    print(y)

if __name__=='__main__':
    print("Hello World!")    
    main()

