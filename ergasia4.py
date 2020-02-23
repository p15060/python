#Π15060
def is_prime_number(num):
    if num >= 2:
        for x in range(2,num):
            if not ( num % x ):
                return False
    else:
        return False
    return True
	        
while True:
   txt=input("Παρακαλώ γράψτε κάτι...\n")
   if txt=='exit':
      break
   num=(''.join(str(ord(c)) for c in txt))
   print('To κείμενο που εισάγατε σε ASCI code είναι: ',num)
   intnum=int(num)
   if is_prime_number(intnum):
        print ('Ο αριθμός ',intnum, ' είναι πρώτος\nΕάν επιθυμείτε να αποχωρήσετε πληκτρολογήστε "exit".\n')
   else:
        print('Ο αριθμός ',intnum, ' δεν είναι πρώτος\nΕάν επιθυμείτε να αποχωρήσετε πληκτρολογήστε "exit".\n')
quit()  
#Π15060