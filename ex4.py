#setting the variables and their values
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Now, use these variables in printed sentences.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#Now, create a calculator using your own variables.
i = 12
j = 25
k = 1.0
p = 8.0
x = 90
y = 10
z = 5

print "i + j equals", i+j
print "k / p equals", k/p
print "x + y * z equals", x+y*z

