#Π15060
sum=0   
print("Πληκτρολογήστε έναν αριθμό...")
number=int(input())

number=(number*3)+1

print("Ο αριθμός πολλαπλασιασμένος με 3 και αυξημένος κατά 1: ",number)

while number!=0:
    sum=number%10
    number=int(number/10)
   
    if number==0 and int(sum/10)!=0:
        number=sum
        
        sum=0
        number=(number*3)+1
        
        continue
print("Το τελικό μονοψήφιο αποτέλεσμα είναι: ",sum)

input()
    

#Π15060 