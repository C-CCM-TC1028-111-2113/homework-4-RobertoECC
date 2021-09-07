def main():
    #escribe tu código abajo de esta línea
    pass

n = int(input())
a = 0

while a < n:
    a = a + 1
    if (a % 2 ) != 0:
        print(str(a) + "-" + "#")
    elif (a % 2) == 0:
        print(str(a) + "-" + "%")

if __name__=='__main__':   
    main()
