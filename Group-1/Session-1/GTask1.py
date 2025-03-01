def CClear():
    # baraye pak kardan comand line hast , edit nakonin
    import os
    if os.name == "nt" :
        os.system("cls")
    else :
        os.system("clear")
        
CClear()