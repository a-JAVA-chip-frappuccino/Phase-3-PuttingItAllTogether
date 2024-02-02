# sandbox environment for testing purposes

from Makeup import Makeup
from People import People
from Purchase import Purchase

# makeup objects
lipstick1 = Makeup("Pat McGrath", "lipstick")
lipstick2 = Makeup("ELF", "lipstick")
eyeshadow1 = Makeup("Clinique", "eyeshadow")
mascara1 = Makeup("ELF", "mascara")

# people objects
person1 = People("Morgan Freeman", 87)
person2 = People("Bruce Willis", 75)
person3 = People("Barry Alan", 32)

# purchase objects
purchase1 = Purchase(eyeshadow1, person1, "12/02/1998")
purchase2 = Purchase(lipstick2, person1, "12/02/1998")
purchase3 = Purchase(eyeshadow1, person2, "12/02/1998")
purchase4 = Purchase(mascara1, person1, "12/02/1998")
purchase5 = Purchase(eyeshadow1, person3, "12/02/1998")
purchase6 = Purchase(lipstick1, person1, "12/02/1998")

# sandbox
print(Makeup.get_unique_types())
print(Purchase.get_most_popular_brand())