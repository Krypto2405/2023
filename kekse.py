# OT compiler


# Variablen

name = input("Kunde:")
b_price = float(input("Einkaufspreis in € Angeben:"))
s_price = int(input("Bestellung in € angeben:"))
com_s = input("Auf Kommission y/n:")
com_b = int(input("Verbindlichkeiten bezahlt in €:"))
print("________________")

#! name = "Peter"
#! b_price = 6.5
#! s_price = 50
#! com_s = "y"
#! com_b = 20


# Gewinn Rechner (Terminal)

if s_price < 50:
    print("Für "+ str(s_price) + " € = " + str(s_price/10) + "Gramm")
elif s_price >= 50:
    print("Für "+ str(s_price) + " € = " + str(s_price/(8+1/3)) + "Gramm")

if s_price < 50: # 35% bei 10€ = +3,5€  
    print("Bei " + str(s_price) + " € sind davon " + str(round(s_price*((10-b_price)/10), 2)) + " € Gewinn")
elif s_price >= 50: # 22% bei 50€ = +11€  
    print("Bei " + str(s_price) + " € sind davon " + str(s_price*(100-(12*b_price))/100) + " € Gewinn")


# K-Liste_str/int Schreiben & Anhängen (Kommission)

from datetime import date
datum = date.today()
import os

path = "/Users/kris/Documents/CODE/Projekte/Python/OT/K-Liste_str/" + name + "_str.txt"

if com_s == "y" and os.path.exists(path) == True:
    datei = open("/Users/kris/Documents/CODE/Projekte/Python/OT/K-Liste_str/" + name + "_str.txt",'a')
    datei.write("\n" + "________________" + "\n" + str(datum) + "\n" + "+" + str(s_price))
    datei.close()
    datei = open("/Users/kris/Documents/CODE/Projekte/Python/OT/K-Liste_int/" + name + "_int.txt",'a')
    datei.write("\n" + "+" + str(s_price))
    datei.close()    
elif com_s == "y" and os.path.exists(path) == False:
    datei = open("/Users/kris/Documents/CODE/Projekte/Python/OT/K-Liste_str/" + name + "_str.txt",'w')
    datei.write(name + "\n" + "________________" + "\n" + str(datum) + "\n" + "+" + str(s_price))
    datei.close()
    datei = open("/Users/kris/Documents/CODE/Projekte/Python/OT/K-Liste_int/" + name + "_int.txt",'w')
    datei.write("\n" + "+" + str(s_price))
    datei.close()  
else:
     print("________________")


# K-Liste_str/int Schreiben & Anhängen (Verbindlichkeiten)

if int(com_b) > 0:
    datei = open("/Users/kris/Documents/CODE/Projekte/Python/OT/K-Liste_str/" + name + "_str.txt",'a')
    datei.write("\n" + "________________" + "\n" + str(datum) + "\n" + "-" + str(com_b))
    datei.close()
    datei = open("/Users/kris/Documents/CODE/Projekte/Python/OT/K-Liste_int/" + name + "_int.txt",'a')
    datei.write("\n" + "-" + str(com_b))
    datei.close()
else:
    print("________________")
   
    
# K-Liste_str (Terminal)

str_list = open("/Users/kris/Documents/CODE/Projekte/Python/OT/K-Liste_str/" + name + "_str.txt", "r")
print("\n" + "K-Liste" + "\n" + str_list.read())
str_list.close()
print()


# K-Liste_int (Terminal)

numbers = []
f = open("/Users/kris/Documents/CODE/Projekte/Python/OT/K-Liste_int/" + name + "_int.txt",encoding="utf-8")
line = f.readline()
while line != "":
    line = line.strip()
    line = line.replace(",",".")
    line = f.readline()
    try:
        number = float(line)
        numbers.append(number)
    except ValueError:
        pass
f.close()

k = sum(numbers)
print(name + " Verbindlichkeiten: " + str(k) + "€")

