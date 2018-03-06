colors = ['Red', 'Blue', 'Yellow']
car_brands = ['Honda', 'Toyota', 'BMW', 'Audi', 'Mercedes']
car_configurations = []

# "Normal way"
for color in colors:
    for brand in car_brands:
        car_configurations.append(color + " " + brand)
print("Car configurations(normal nested for loops): %s" % car_configurations)
print("----------------------------------------------------------------------")

# Listcomp
car_configurations = [(color + " " + brand) for color in colors for brand in car_brands]
print("Car configurations(listcomp): %s" % car_configurations)
print("----------------------------------------------------------------------")

# Listcomp sorted by brands first.
car_configurations = [(color + " " + brand) for brand in car_brands for color in colors]
print("Car configurations(listcomp): %s" % car_configurations)
print("----------------------------------------------------------------------")

# OUTPUT:

#  ➜  IntroToListcompsPython git:(master) ✗ python list_comp_colorful_cars.py
#  Car configurations(normal nested for loops): ['Red Honda', 'Red Toyota', 'Red BMW', 'Red Audi', 'Red Mercedes', 'Blue Honda', 'Blue Toyota', 'Blue BMW', 'Blue Audi', 'Blue Mercedes', 'Yellow Honda', 'Yellow Toyota', 'Yellow BMW', 'Yellow Audi', 'Yellow Mercedes']
#  ----------------------------------------------------------------------
#  Car configurations(listcomp): ['Red Honda', 'Red Toyota', 'Red BMW', 'Red Audi', 'Red Mercedes', 'Blue Honda', 'Blue Toyota', 'Blue BMW', 'Blue Audi', 'Blue Mercedes', 'Yellow Honda', 'Yellow Toyota', 'Yellow BMW', 'Yellow Audi', 'Yellow Mercedes']
#  ----------------------------------------------------------------------
#  Car configurations(listcomp): ['Red Honda', 'Blue Honda', 'Yellow Honda', 'Red Toyota', 'Blue Toyota', 'Yellow Toyota', 'Red BMW', 'Blue BMW', 'Yellow BMW', 'Red Audi', 'Blue Audi', 'Yellow Audi', 'Red Mercedes', 'Blue Mercedes', 'Yellow Mercedes']
#  ----------------------------------------------------------------------
