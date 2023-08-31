def starletter(i):
    N = 5
    print("")
    #letter A
    def letterA():
        for i in range(1,N+1):
            if(i == 1):
                left_spaces = " "*(N-i)
                print(left_spaces+"* ")
            elif(i == 3):
                left_spaces = " "*(N-i)
                print(left_spaces+"* "*i)
            else:
                left_spaces = " "*(N-i)
                hollow = "  "*(i-2)
                print(left_spaces+"* "+hollow+"* ")
        print("")

#letter B
    def letterB():
        for i in range(1,N+1):
            if(i % 2 != 0):
                print("* "*4)
            else:
                hollow = "  " * 3
                print("* "+hollow +"* ")
        print("")
#letter C
    def letterC():
        for i in range(1,N+1):
            if(i == 1 or i == N):
                print("  "+"* "*(N-1))
            else:
                print("* ")
        print("")
#letter D
    def letterD():
        for i in range(1,N+1):
            if(i == 1 or i == N):
                print("* "*(N-1))
            elif(i == 3):
                print("*"+"  "*4+"* ")
            else:
                hollow = "  "*3
                print("* "+hollow+"* ")
        print("")
#letter E
    def letterE():
        for i in range(1,N+1):
            if(i % 2 == 0):
                print("* ")
            elif(i == 3):
                print("* "*(N-1))
            else:
                print("* "*N)
        print("")
#letter F
    def letterF():
        for i in range(1,N+1):
            if(i % 2 == 0):
                print("* ")
            elif(i == 3):
                print("* "*(N-1))
            else:
                print("* "*N)
        print("")
#letter G
    def letterG():
        for i in range(1,N+1):
            if(i == 1 or i == N):
                print("  "+"* "*(N-1))
            elif(i == 3):
                print("* "+"  "+"* "*3)
            elif(i % 2 == 0):
                if(i == 4):
                    print("* "+"  "*3+"* ")
                else:
                    print("* ")
        print("")
#letter H
    def letterH():
        for i in range(1,N+1):
            if(i== 3):
                print("* "*N)
            else:
                hollow = "  "*(N-2)
                print("* "+hollow +"* ")
        print("")
#letter I
    def letterI():
        for i in range(1,N+1):
            if(i == 1 or i == N):
                print("* "*N)
            else:
                left_space = "  "*2
                print(left_space+"* ")
        print("")
#letter J
    def letterJ():
        for i in range(1,N+1):
            if(i == 1):
                print("* "*N)
            elif(i == N):
                print("* "*3)
            elif(i == 4):
                print("* "+"  "+"* ")
            else:
                print("  "*2+"* ")
        print("")                           
#letter K
    def letterK():
        for i in range(1,N+1):
            if(i == 1 or i == N):
                print("* "+"  "*2+"* ")
            elif(i == 2 or i == 4):
                print("* "+"  "+"* ")
            else:
                print("* "*2)
        print("")
#letter L
    def letterL():
        for i in range(1,N+1):
            if(i==N):
                print("* "*N)
            else:
                print("* ")
        print("")
#letter M
    def letterM():
        for i in range(1,N+1):
            if(i == 2):
                print("* "*2+"  "+"* "*2)
            elif(i == 3):
                print("* "+"  "+"* "+"  "+"* ")
            else:
                print("* "+"  "*3+"* ")
        print("")
#letter N
    def letterN():
        for i in range(1,N+1):
            if(i == 1 or i == N):
                print("* "+"  "*3+"* ")
            else:
                s1 = "  "*(i - 2)
                s2 = "  "*(N-i-1)
                print("* "+s1+"* "+s2+"* ")
        print("")
#letter O
    def letterO():
        for i in range(1,N+1):
            if(i == 1 or i ==N):
                print("  "+"* "* 3)
            else:
                print("* "+"  "*3+"* ")
        print("")
#letter P
    def letterP():
        for i in range(1,N+1):
            if(i == 1 or i == 3):
                print("* "*N)
            elif(i == 2):
                print("* "+"  "*3+"* ")
            else:
                print("* ")
        print("")
#letter R
    def letterR():
        for i in range(1,N+1):
            if(i == 1 or i == 3):
                print("* "*N)
            elif(i == 2):
                print("* "+"  "*3+"* ")
            else:
                print("* "+"  "*(i-2)+"* ")
        print("")
#letter S
    def letterS():
        for i in range(1,N+1):
            if(i % 2 != 0):
                print("* "*N)
            elif(i == 4):
                print("  "*i+"* ")
            else:
                print("* ")
        print("")

#letter T
    def letterT():
        for i in range(1,N+1):
            if(i == 1):
                print("* "*N)
            else:
                print("  "* 2+"* ")
        print("")
#letter U
    def letterU():
        for i in range(1,N+1):
            if(i == N):
                print("  "+"* "*3)
            else:
                print("* "+"  "*3+"* ")
        print("")
#letter V
    def letterV():
        for i in range(1,N+1):
            if(i == N):
                print("  "*2+"* ")
            else:
                leftsp = " "*(i-1)
                hollow = "  "*(N-i-1)
                print(leftsp+"* "+hollow+"* ")
        print("")
#letter W
    def letterW():
        for i in range(1,N+1):
            if(i == 3):
                print("* "+"  "+"* "+"  "+"* ")
            elif(i == 4):
                print("* "*2+"  "+"* "*2)
            else:
                print("* "+"  "* 3+"* ")
        print("")
#letter X
    def letterX():
        for i in range(1,N+1):
            if(i < 3):
                left_spa = "  "*(i-1)
                hollow = "  "*(N-i*2)
                print(left_spa+"* "+hollow+"* ")
            elif(i == 3):
                print("  "* 2+"* ")
            else:
                left_spa = "  "*(N-i)
                hollow = "  "*(2*i-N -2)
                print(left_spa+"* "+hollow+"* ")
        print("")
#letter Y
    def letterY():
        for i in range(1,N+1):
            if(i < 3):
                left_spa ="  "*(i-1)
                hollow = "  "*(N - i*2)
                print(left_spa+"* "+hollow+"* ")
            else:
                print("  "*2+"* ")
        print("")
#letter Z
    def letterZ():
        for i in range(1,N+1):
            if(i == 1 or i == N):
                print("* "*N)
            else:
                left_spa = "  "*(N-i)
                print(left_spa+"* ")
        print("")

#condition checking and function calling for individual characters
    if(i == "A"):
        letterA()
    elif(i == "B"):
        letterB()
    elif(i == "C"):
        letterC()
    elif(i == "D"):
        letterD()
    elif(i == "E"):
        letterE()
    elif(i == "F"):
        letterF()
    elif(i == "G"):
        letterG()
    elif(i == "H"):
        letterH()
    elif(i == "I"):
        letterI()
    elif(i == "J"):
        letterJ()
    elif(i == "K"):
        letterK()
    elif(i == "L"):
        letterL()
    elif(i == "M"):
        letterM()
    elif(i == "N"):
        letterN()
    elif(i == "O"):
        letterO()
    elif(i == "P"):
        letterP()
    elif(i == "R"):
        letterR()
    elif(i == "S"):
        letterS()
    elif(i == "T"):
        letterT()
    elif(i == "U"):
        letterU()
    elif(i == "V"):
        letterV()
    elif(i == "W"):
        letterW()
    elif(i == "X"):
        letterX()
    elif(i == "Y"):
        letterY()
    else:
        letterZ()

name = input("Enter the String input : ")
name = name.upper()
for i in name:
    starletter(i)
