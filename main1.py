import math
print()
print("The next outputs are the area of the circle testes")
print()

#Function to get the area of the circle
def areaCircle(radio):
    circle = math.pi * (radio ** 2)
    return print("%.2f" % circle)

#inputs from the assignment
areaCircle(10)
areaCircle(6)
areaCircle(24)
areaCircle(2)
areaCircle(1)

#making a space
print()
print("The next outputs are the taxes testes")
print()

#Test data taxes
def taxes(money, taxRates):
    totalDue = money + (money * taxRates)
    return print ("%.2f" % totalDue)

taxes(20,0.06)
taxes(54,0.04)
taxes(68, 0.08)

print()
print("The next outputs are the temperature testes")
print()

#Test Data - Temperature

def temperature(Fahrenheit):
    celsius = (Fahrenheit - 32) * (5/9)
    return print ("%.4f" % celsius)

temperature(32)
temperature(80)
temperature(73)
temperature(42)
