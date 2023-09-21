









# ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#<--------------------[!!! A WARNING !!!]--------------------->
#
#       THIS PROJECT IS WORK IN PROGRESS STILL! 
#   THE CODE IS MESSY, THIS IS A PERSONAL PROJECT 
#                  SO IT FITS MY NEEDS
#                         NOTE :
#           THERE IS A FUNCTION THAT SEARCHES 
#         THROUGH A TEXT FILE 'readSpecificFile'
# ADD A TXT FILE NAMED 'input.txt' IN THE SCRIPT DIRECTORY
#           WITH WHATEVER TEXT YOU WISH TO TEST
#              OR COMMENT THAT FUNCTION CALL
#
#           MODIFY AT YOUR OWN RISK. THANK YOU!
#
#<--------------------[~.~.~ GOOD LUCK ~.~.~]--------------------->
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION ATTENTION 







gpsums = {

"F"   : 2,
"U"   : 3,
"V"   : 3,
"TH"  : 5,
"O"   : 7,
"R"   : 11,
"C"   : 13,
"K"   : 13,
"G"   : 17,
"W"   : 19,
"H"   : 23,
"N"   : 29,
"I"   : 31,
"J"   : 37,
"EO"  : 41,
"P"   : 43,
"X"   : 47,
"S"   : 53,
"Z"   : 53,
"T"   : 59,
"B"   : 61,
"E"   : 67,
"M"   : 71,
"L"   : 73,
"NG"  : 79,
"ING" : 79,
"OE"  : 83,
"D"   : 89,
"A"   : 97,
"AE"  : 101,
"Y"   : 103,
"IA"  : 107,
"IO"  : 107,
"EA"  : 109

}

runes2 = {

"ᚠ"   : (2,"F"),
"ᚢ"   : (3,"U"),
"ᚢ"   : (3,"V"),
"ᚦ"   : (5,"TH"),
"ᚩ"   : (7,"O"),
"ᚱ"   : (11,"R"),
"ᚳ"   : (13,"C"),
"ᚳ"   : (13,"K"),
"ᚷ"   : (17,"G"),
"ᚹ"   : (19,"W"),
"ᚻ"   : (23,"H"),
"ᚾ"   : (29,"N"),
"ᛁ"   : (31,"I"),
"ᛄ"   : (37,"J"),
"ᛇ"   : (41,"EO"),
"ᛈ"   : (43,"P"),
"ᛠ"   : (47,"X"),
"ᛋ"   : (53,"S"),
"ᛋ"   : (53,"Z"),
"ᛏ"   : (59,"T"),
"ᛒ"   : (61,"B"),
"ᛖ"   : (67,"E"),
"ᛗ"   : (71,"M"),
"ᛚ"   : (73,"L"),
"ᛝ"   : (79,"NG"),
"ᛝ"   : (79,"ING"),
"ᛟ"   : (83,"OE"),
"ᛞ"   : (89,"D"),
"ᚪ"   : (97,"A"),
"ᚫ"   : (101,"AE"),
"ᚣ"   : (103,"Y"),
"ᛡ"   : (107,"IA"),
"ᛡ"   : (107,"IO"),
"ᛉ"   : (109,"EA")

}

runes = {

"ᚠ"   : "F",
"ᚢ"   : "U",
"ᚢ"   : "V",
"ᚦ"   : "TH",
"ᚩ"   : "O",
"ᚱ"   : "R",
"ᚳ"   : "C",
"ᚳ"   : "K",
"ᚷ"   : "G",
"ᚹ"   : "W",
"ᚻ"   : "H",
"ᚾ"   : "N",
"ᛁ"   : "I",
"ᛄ"   : "J",
"ᛇ"   : "EO",
"ᛈ"   : "P",
"ᛠ"   : "X",
"ᛋ"   : "S",
"ᛋ"   : "Z",
"ᛏ"   : "T",
"ᛒ"   : "B",
"ᛖ"   : "E",
"ᛗ"   : "M",
"ᛚ"   : "L",
"ᛝ"   : "NG",
"ᛝ"   : "ING",
"ᛟ"   : "OE",
"ᛞ"   : "D",
"ᚪ"   : "A",
"ᚫ"   : "AE",
"ᚣ"   : "Y",
"ᛡ"   : "IA",
"ᛡ"   : "IO",
"ᛉ"   : "EA"

}



#The two squares from the solved pages
square1 = [272,138,341,131,151,366,199,130,320,18,226,245,91]
square2 = [434,1311,312,278,966,204,812,934,280,1071,626,620,809]


#<--------------------[start of additional functions]--------------------->
def menu():

    print()
    print()

    print("<============ [ GPSUM ] ============>")
    print("                                     ")
    print(" gematria primus sum in the terminal ")
    print("                                     ")
    print("<============= [ wip ] =============>")
    print("            # by SvEn #")

    print()
    print()

def line():
    print("======================================")

def lineshort():
    print("--------------------------")

def func(word, n):
    return [''.join(item) for item in zip(*[word[n:] for n in range(n)])]

def factors(x):
    arr = []
    arrprimes = []

    for i in range (1, x + 1):
        if x % i == 0:
            arr.append(i)
            if isprime3(i):
                arrprimes.append(i)

    print(f"the factors of {x} are: {arr}")
    print(f"the PRIME FACTORS of {x} are : {arrprimes}")

def isprime(x):

    if x == 1 :
        print(f"{x} is not prime ")

    if x > 1:
        for i in range(2,x):
            if(x % i) == 0:
                print(f"{x} is not prime ")
                print(f"{i} times {x//i} is {x}")
                break
        else:
                print(f"{x} is PRIMEEEE!!!!")
    else:
        print(f"{x} is not prime ")


#def isprime2():
#            val = int(input(">value: "))
#            isprime(val)




def isprime3(x):

    if x <= 1 :
        return False

    if x > 1:
        for i in range(2,x):
            if(x % i) == 0:
                return False
            
        return True
    


def gcd(p,q):
    while q != 0:
        p,q = q, p%q
    return p 

def is_coprime(x,y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x, y)]
        return len(n)


def iteratelist(x):
    if x in square2 :
        print(f" Value {x} is FOUND in SQUARE 2")
    else :
        print(f"{x} NOT FOUND in square2")
    
    if x in square1 :
        print(f"{x} is FOUND in SQUARE 1")
    else :
        print(f"{x} NOT FOUND in square1")   



def isEmirp(num):
   num = int(num)
   if  isprime3(num) == False:
      return False

   reverse_num = 0
   while num != 0:
      d = num % 10
      reverse_num = reverse_num * 10 + d
      num = int(num / 10)
   return isprime3(reverse_num)



def readSpecificFile(k):
    try:
        print("[THE BOOk OF URIZEN ~ PRELUDE (w/o punc/symb/whsp)]")
        newstr = ""
        f = open("BOU.txt","r")

        for x in f:
            a_string = x

            alphanumeric = " "

            for character in a_string:
                if character.isalnum():
                    alphanumeric+=character
            #print(alphanumeric)
            newstr += alphanumeric
        print(f"{k}th char is >>>>> {newstr[k]}")
        
    except:
        print("[!!!] SOMETHING WENT WRONG ~TRY/CATCH PATH ~")    
      

    



def nThPrime(n):
    i = 2
    while(n > 0):
 
       
        if(isprime3(i)):
            n -= 1
 
        i += 1  
 
    i -= 1 
   
    return i




def translateRunes(shift):
    shift = 0
    res = ""
    rune  = input("Runes: ")
    runecopy = rune


    for item in func(rune, 1):
            for key,value in runes.items():
                if key == item:
                    res += str(value)
                    res += " "
   
        
               
    print(res)
            
            

def op1():
            sum=0
            word = input("Word: ").upper()
            wordcopy = word

# =============  searching for  ======================================================================= 
#                     ING

            for item in func(word, 3):
                for key,value in gpsums.items():
                    if key == item:
                        sum = sum + value
                        word = word.replace(item,'#')
                                  
# =============  searching for  ======================================================================= 
#           EA,IO,IA,AE,OE,NG,EO,TH

            sum2 = sum
            for item in func(word, 2):
                for key,value in gpsums.items():
                    if key == item:
                        sum2 = sum2 + value
                        word = word.replace(item,'#')
                                    
# =============  searching for  ======================================================================= 
#            REMAINING SINGLE LETTERS

            sum3 = sum2
            for item in func(word, 1):
                for key,value in gpsums.items():
                    if key == item:
                        sum3 = sum3 + value
                        word = word.replace(item,'#')
                                    




# = = = = = PRINTING THE GPSUM AND ALL THE OTHER INFO BASED ON THE SUM = = = = =
            
  
            print(f"\n     !!----> [{wordcopy}]  = {sum3} <----!! \n")
            
            line()
            lineshort()

            iteratelist(sum3)

            lineshort()

            isprime(sum3)

            if isEmirp(sum3):
                print("EMIRP")
            else :
                print("not emirp")

            lineshort()

            print(f"phi({sum3}) =               {phi_func(sum3)}")
            print(f"{sum3} % 29 =                {sum3 % 29}")
            letters_wo_space = len(wordcopy) - wordcopy.count(" ")
            print(f"char count w/o space =   {letters_wo_space}")
            print(f"char count w space =     {len(wordcopy)}")
            lineshort()
            factors(sum3)

            lineshort()
            maxv = 550
            if(sum3 > maxv):
                print(f"nth prime function disabled for values > {maxv}")

            else:
                 print(f"{sum3}th prime is {nThPrime(sum3)}")

            lineshort()
            line()






def op2():
            val = int(input(">value: "))
            
            line()
            lineshort()
            
            isprime(val)
            
            lineshort()
            
            if isEmirp(val):
                print("EMIRP")
            else :
                print("not emirp")

            lineshort()
            line()

            print(f"phi({val}) =               {phi_func(val)}")
            print(f"{val} % 29 =                {val % 29}")
            factors(val)

            lineshort()
                       
            readSpecificFile(val)
            
            lineshort()
            
            maxv = 550
            if(val > maxv):
                print(f"nth prime function disabled for values > {maxv}")

            else:
                 print(f"{val}th prime is {nThPrime(val)}")
            
            lineshort()
            
            iteratelist(val)
            
            line()

#<--------------------[end of additional functions]--------------------->
#                                   ***
#<-----------------------[ main function ]----------------------->

def main():

    
    print("Please input numeric value: ")
    print("[1] GP SUM + other")
    print("[2] Check prime value + other")
    print("[3] 1:1 RUNE TO TEXT ~ wip")
    print("[0] Exit")
        
    option = int(input(">: "))
    
    while option!=0:
     
#<--------------------[ [1] RESULT GPSUM + OTHER ]--------------------->   #  
        if(option == 1):
 
            op1()
             
            print("\nwant to sum another input? Y/ N")

            q = input(">: ")
            if q == "y" or q =="Y" or q == "yes" or q == "YES" or q == "Yes":
                option = 0
                main()

            elif q == "n" or q =="N" or q == "no" or q == "NO" or q == "No":
                print("exiting...farewell...")
                break
#<--------------------[ [2] CHECK PRIME NUMBER + OTHER ]--------------------->   

        elif (option == 2):
           
            op2()
        
            print("\n want to check another value? Y/N")
             
            q = input(">: ")
            
            if q == "y" or q =="Y" or q == "yes" or q == "YES" or q == "Yes":
                option = 0
                main()

            elif q == "n" or q =="N" or q == "no" or q == "NO" or q == "No":
                print("exiting...farewell...")
                break





        elif(option == 3):
            translateRunes()

            print("\n want to check another value? Y/N")
             
            q = input(">: ")
            
            if q == "y" or q =="Y" or q == "yes" or q == "YES" or q == "Yes":
                option = 0
                main()

            elif q == "n" or q =="N" or q == "no" or q == "NO" or q == "No":
                print("exiting...farewell...")
                break

#<--------------------[ [0] EXIT  ]--------------------->   

        elif (option == 0):
            print("Exiting...Farewell...")

        else:
            print("Invalid input!!!")
            gepsum()

menu()
main()


