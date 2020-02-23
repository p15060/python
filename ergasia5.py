#Π15060
inp=input('Πληκτρολογήστε το όνομα του txt αρχείου (δεν απαιτείται η κατάληξη txt) \n')
txt=open(inp + '.txt').read()
for i in txt.split():
    if len(i)>3:
        i=i[1:]+i[0]+"ay"
        print(i)
    else:
        print(i)
input()
#Π15060 
