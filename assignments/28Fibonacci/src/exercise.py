
def main():
    num = int(input("Enter a number: "))
   
    #escribe tu código abajo de esta línea
    pass

    a = 0
    b = 1

    if num == 0:
        print("0")
    elif num == 1:
      print ("1")
    else:
        for i in range(1, num):
           c =  a + b
           a = b
           b = c
      print (b)

if __name__=='__main__':
    main()
