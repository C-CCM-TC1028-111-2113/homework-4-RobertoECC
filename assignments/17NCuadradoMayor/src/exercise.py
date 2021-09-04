

def main():
    num = int(input("Escribe un numero: "))
    #Escribe tu código debajo de esta línea
    pass
a = 1 

while a < num:
    if (a ** 2) < num:
        a = a + 1 
    elif (a ** 2) > num:
        print(a)
        break

if __name__=='__main__':
    main()
