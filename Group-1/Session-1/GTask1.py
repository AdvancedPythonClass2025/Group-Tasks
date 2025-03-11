def CClear():
    # baraye pak kardan comand line hast , edit nakonin
    import os
    if os.name == "nt" :
        os.system("cls")
    else :
        os.system("clear")

def NameInpt():
    #baraye  vrody gereftan esm hast , kamel shode 
    global CClear
    global name
    print("lotfan esm khod ra vared konid\n\n\n\n\n")
    x = input("_____:").strip()

    if x == "":
        
        CClear()
        print("lotfan vrodi ra ba horof por konid\n\n")
        NameInpt()

    elif all(harf.isalpha() or harf.isspace() for harf in x): 

        
        name = x  
      
    else :
      
        CClear()
        print("fagat mitonid az horof alephba estefade konid\n\n\n")
        NameInpt()

def AgeInpt():
    #baraye gereftan vrodi sen hast
    print("")

def EmailInpt():
    #baraye gereftan vrodi email hast
    print("")

form = f"""

name  : {name}

age   :

email :

       """

#CClear()
#NameInpt()
#AgeInpt()
#EmailInpt()
#print(form)