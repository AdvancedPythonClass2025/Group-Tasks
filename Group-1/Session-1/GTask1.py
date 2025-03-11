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

def EmailInpt(email:str):
    #baraye gereftan vrodi email hast
    if len(email) <= 4 :
        return "email bayad bishtar az 4 charaacter bashad"
    if not any(harf.isalpha() for harf in Uinput) or not any(harf.isdigit() for harf in Uinput):
        return("email bayad tarkibi az horof va adad bashand")
    else :
        return f"{email}@gmail.com"
try :
    Uinput = input("email ra vared konid : ")
    re = EmailInpt(Uinput)
    if not Uinput[0].isalpha():
        print("email bayad ba character shoro shavad")
    elif any(harf in ["@",".","-","_"] for harf in Uinput):
        print("vorodi namotabar ast")
    else :
        print(re)
except Exception as eror:
    print(f"khatay nashenakhteh : {eror}")

#CClear()
#NameInpt()