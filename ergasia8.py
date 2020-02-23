#Π15060
from random import seed
from random import randint
import time




cars1 = randint(0,10) 
cars2 = randint(0,10) 
cars3 = randint(0,10) 
print("Τα οχήματα στα φανάρια i, ii, iii είναι ",cars1,cars2,cars3,"αντίστοιχα. \n")
time.sleep(2)
while True:
    cars1Come=randint(0,5)
    cars2Come=randint(0,5)
    cars3Come=randint(0,5)
    
    cars1Leave=randint(0,cars1)
    cars2Leave=randint(0,cars2)
    cars3Leave=randint(0,cars3)
   
    if cars1 >= cars2:
        if cars1 > cars3:
            print("Φανάρια: i πράσινο, ii κόκκινο, iii κόκκινο.")
            cars1 = cars1-cars1Leave
            cars2=cars2 + cars2Come
            cars3=cars3 + cars3Come
            print("Στο φανάρι i φεύγουν ", cars1Leave, "οχήματα.")
            time.sleep(2)
            
            print("Στα φανάρια ii, iii έρχονται ",cars2Come,cars3Come, "αντίστοιχα.\n")
            
           
            time.sleep(2)
            print("Tα οχήματα στα φανάρια i,ii,iii είναι ", cars1,cars2,cars3," αντίστοιχα\n\n")
            time.sleep(2)
        else:
            print("Φανάρια: i κόκκινο, ii κόκκινο, iii πράσινο.")
            cars3 = cars3-cars3Leave
            cars2=cars2 + cars2Come
            cars1=cars1 + cars1Come
            print("Στο φανάρι iii φεύγουν ", cars3Leave, "οχήματα.")
            time.sleep(2)
            
            print("Στα φανάρια i, ii έρχονται ",cars1Come,cars2Come, "αντίστοιχα.\n")
            
           
            time.sleep(2)
            print("Tα οχήματα στα φανάρια i,ii,iii είναι ", cars1,cars2,cars3," αντίστοιχα\n\n")
            time.sleep(2)
    else:
        if cars2 >= cars3:
            print("Φανάρια: i κόκκινο, ii πράσινο, iii κόκκινο.")
            cars2 = cars2-cars2Leave
            cars3=cars3 + cars3Come
            cars1=cars1 + cars1Come
            print("Στο φανάρι ii φεύγουν ", cars2Leave, "οχήματα.")
            time.sleep(2)
            
            print("Στα φανάρια i, iii έρχονται ",cars1Come,cars3Come, "αντίστοιχα.\n")
            
           
            time.sleep(2)
            print("Tα οχήματα στα φανάρια i,ii,iii είναι ", cars1,cars2,cars3," αντίστοιχα\n\n")
            time.sleep(2)
        else:
            print("Φανάρια: i κόκκινο, ii κόκκινο, iii πράσινο.")
            cars3 = cars3-cars3Leave
            cars2=cars2 + cars2Come
            cars1=cars1 + cars1Come
            print("Στο φανάρι iii φεύγουν ", cars3Leave, "οχήματα.")
            time.sleep(2)
            
            print("Στα φανάρια i, ii έρχονται ",cars1Come,cars2Come, "αντίστοιχα.\n")
           
           
            time.sleep(2)
            print("Tα οχήματα στα φανάρια i,ii,iii είναι ", cars1,cars2,cars3," αντίστοιχα\n\n")
            time.sleep(2)

    

#Π15060 
