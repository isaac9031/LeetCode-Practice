class Mammal:
    def __init__(self, temperature, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.temperature = temperature

class Flyer:
    altitude = 0

    def flap(self):
        self.altitude += 10

    def dive(self):
        self.altitude -= 10

class Bat(Mammal, Flyer): #inheriting allows this class to have the function of the Mammal and Flyer classes
    pass

# Create an instance of Bat
bat_instance = Bat(temperature=98)  # Assume any temperature

# Flap wings until altitude is greater than 32
flap_count = 0
while bat_instance.altitude <= 32:
    bat_instance.flap()  #able to access flap from inheriting the function of class flyer
    flap_count += 1

print("Minimum flaps required:", flap_count)
print("Final altitude:", bat_instance.altitude)
