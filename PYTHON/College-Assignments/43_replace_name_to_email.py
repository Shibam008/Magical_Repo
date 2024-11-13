def makeEmail(s):
    name = list(s.split())
    print(name[0].casefold()+"@ecmt.in")
    
strn = input("Enter your name : ")
makeEmail(strn)
