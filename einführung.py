""" 
- Listenfunktion
- Eintrag löschen und Hinzufügen
- Länge der Liste
- Zugriff auf einzelne Elemente
"""
"""
student0 = "Max"
student1 = "Moritz"
student2 = "Lisa"
student3 = "Anna"

students = [student0, student1, student2, student3]
#students.pop() # entfernt das letzte Element der Liste
students.append(input("Neuer Schüler: ")) # fügt einen neuen Namen am Ende der Liste hinzu

print("Alle Schüler: ", students)#gibt die ganze Liste aus

print("Es gibt: ", len(students), " Schüler") #gibt die Länge der Liste aus
print("Wer ist der zweite Schüler? "+students[1]) # gibt das zweite Element der Liste aus
"""

"""
Operatoren
- Vergleichsoperatoren <, >, ==, !=
- Logische Operatoren and, or, not
- Booleans True, False
"""
a = 5
b = 10

y = a < b
print("y = a < b is", y)
y = a > b
print("y = a > b is", y)
y = a == b
print("y = a == b is", y)
y = a != b
print("y = a != b is", y)

istaufgestanden = True
hatsichangezogen = False
#hatgefruehstueckt = True

perfektgetartet = istaufgestanden and hatsichangezogen #AND Operator
print("Und perfekt gestartet? ", perfektgetartet)
perfektgetartet = istaufgestanden or hatsichangezogen #OR Operator
print("Oder perfekt gestartet? ", perfektgetartet)
perfektgetartet = not istaufgestanden #NOT Operator
print("Nicht perfekt gestartet? ", perfektgetartet)



"""
Aufgaben SLP
"""

