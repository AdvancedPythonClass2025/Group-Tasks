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
    global email
    uinput = input("email ra vared konid  \n\n\n\n\n^__^ ")
    if not uinput :
        CClear()
        print("lotfan email ra vared konid\n\n\n")
        EmailInpt()
    if len(uinput) <= 4 :
        CClear()
        print("email bayad bishtaraz 4 harf basheh\n\n\n")
        EmailInpt()
    elif uinput[0].isdigit():
        CClear()
        print("email mbayad ba adad shoro shavad\n\n\n")
        EmailInpt()
    elif not uinput.endswith("@gmail.com") :
        CClear()
        print("bayad @gmail.com ra vared konid\n\n\n")
        EmailInpt()
    elif uinput.count("@") != 1 :
        CClear()
        print("khata faghat yek @ misheh vared kard\n\n\n")
        EmailInpt()
    elif not any(harf.isalpha() for harf in uinput):
        CClear()
        print("lotfan harf vared konid\n\n\n")
        EmailInpt()
    elif any(char in['!','#','$','%','^','&','*',',','-','+','?','_','=','<>','/'] for char in uinput):
        CClear()
        print("dar email az character hay vijeh nmisheh estefade kard\n\n\n")
        EmailInpt()
    else :
        CClear()
        email = uinput
        print(f"email shoma : {email}")
        EmailInpt()
    # gmail.org453d@gmail.com
    # 23432.e.42@gmail.com

    



#CClear()
#NameInpt()
#CClear
#AgeInpt()
CClear()
EmailInpt()

form = f"""

name  : 

age   :

email : 

       """
#CClear()
#print(form)
