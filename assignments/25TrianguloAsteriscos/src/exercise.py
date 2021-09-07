
def main():
    height = int(input("Enter triangle height: "))
    
    #Escribe tu código debajo de esta línea
    pass

    for i in range(height, -1, -1):
        for a in range (i):
            print(" ", end="")
        for b in range(i, height):
            print("*", end= "")
        print("")

if __name__=='__main__':
    main()
