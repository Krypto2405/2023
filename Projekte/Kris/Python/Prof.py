"""Professor Ungerechtmann der Kantonsschule Unfairdorf braucht ein Programm für die Notenvergabe der Abschlussprüfung. Die Abschlussnote hängt von den folgenden Parametern ab:

    Prüfungsnote (von 1 bis 6 mit Halbpunkten);
    Augenfarbe (z.B. dunkel=1, hell=0);
    Frisur (z.B. kurze Haare=1, lange Haare=0);
    Wetter (z.B. schön=1, nicht schön=0).

Es gilt folgendes:

    Hat der Prüfling dunkle Augen und…

        kurze Haare, so wird die Abschlussnote um 10% erhöht (d.h. Abschlussnote = Prüfungsnote + 10% Prüfungsnote).
        lange Haare, so wird die Abschlussnote um 10% reduziert.

    Hat der Prüfling helle Augen und…

        kurze Haare, so wird die Abschlussnote um 10% reduziert.
        lange Haare, so wird die Abschlussnote um 10% erhöht.

    Ist das Wetter schön, so wird die Abschlussnote um eine Einheit reduziert.

    Die Abschlussnoten müssen auf halbe Noten gerundet werden.

Hinweis: Wie kann man auf halbe Noten runden? Die Funktion round() rundet auf ganze Noten, z.B. round(5.4) = 5 aber round(5.4*2) = 11… ;)
"""

p = int(input("Prüfungsnote [von 1 bis 6 mit Halbpunkten]:"))
a = input("Augenfarbe [dunkel=1, hell=0]:")
f = input("Frisur [kurze Haare=1, lange Haare=0]:")

if a + f == 2:
    print(int(p * 1.1))
elif a + f == 0:
    print(int(p * 0.9))
else:
    print("Fehler")
    