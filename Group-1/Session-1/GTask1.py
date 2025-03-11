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

    elif all(char.isalpha() or char.isspace() for char in x): 

        
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
        return "email bayad bishtar az 4 character bashad"
    else :
        return f"{email}@gmail.com"
try :
    user = input("email ra vared konid : ")
    re = EmailInpt(user)
    if not user[0].isalpha():
        print("email bayad ba character shoro shavad")
    if not any(char.isalpha() for char in user) or not any(char.isdigit() for char in user):
        print("email bayad tarkibi az horof va adad bashand")
    elif user in ["@",".","-","_"]:
        print("vorodi namotabar ast")
    else :
        print(re)
except Exception as eror:
    print(f"khatay nashenakhteh : {eror}")

#CClear()
#NameInpt()