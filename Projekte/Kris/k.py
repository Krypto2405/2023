'''Vorkenntnisse: Kapitel 1.
Erstelle ein Programm, das deinen Vorname, Nachname und dein Geburtsdatum auf der Konsole ausgibt.'''
'''
import time

x = str input("Wie ist dein Vorname?")
y = str input("Wie ist dein Nachname?")
z = float input("Geburtsdatum?")

print(x, y, z)
'''
'''
x = 17.13
y = 17
z = "ABC"


s = 17
c = 3
print(x + y)
'''

'''
Schreibe ein Programm, das Temperaturen in verschiedene Skalensystemen ineinander umwandelt. Das Programm soll zu Beginn eine Auswahl mit den verschiedenen Möglichkeiten anbieten:


Bemerkung

Dies kann dir sicher helfen.

    Celsius = 5/9 * (Fahrenheit - 32).

    Celsius = Kelvin - 273.15.

    Die tiefste mögliche Temperatur ist den absoluten Nullpunkt 0K.
    '''

print("""
(a) Umrechnung von Celsius nach Kelvin
(b) Umrechnung von Celsius nach Fahrenheit
(c) Umrechnung von Kelvin nach Celsius
(d) Umrechnung von Kelvin nach Fahrenheit
(e) Umrechnung von Fahrenheit nach Celsius
(f) Umrechnung von Fahrenheit nach Kelvin
""")



r = (input("Wähle zwischen a - f"))
x = int(input("Einheit:"))

if input(r) == a:
    print(x - 273.15)
    