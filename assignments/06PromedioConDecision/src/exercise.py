def main():
    #escribe tu código abajo de esta línea
    pass

num = float(input())
a = 1

while (num > 0):
    a = a + 1
    c = float(input())
    num = num + c 
    if (c < 0):
        num = num - c
        a = a - 1 
        prom = (num / a)
        print (prom)
        break 

if __name__=='__main__':
    main()
