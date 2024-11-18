print("WELCOME TO COS101")
print("Name:AKINTOLURE DAVID OLUWATOMISIN  ")
print("Matric number:BHU/24/04/09/0025                                                                                                              ic number:BHU/24/04/09/0025 ")
def a():
    length= int(input("Enter value of length "))
    breadth= int(input("Enter value of breadth "))
 #   area= length * breadth
    output= str(length * breadth)
    print("The result= " +  output)

def b():
    force= int(input("Enter value of force "))
    mass = int(input("Enter value of mass "))
#   acceleration= force * mass
    output= str(force * mass)
    print("The result= " + output)
def c():
     mass = int(input("Enter value of mass "))
     acceleration = int(input("Enter value of acceleration "))
 #    Force= mass * acceleration
     output = str(mass * acceleration)
     print("The result= " + output)

def d():
    force= int(input("Enter value of force "))
    time= int(input("Enter value of time "))
 #   impluse= force * time
    output= str(force * time)
    print("The result= " +  output)

def e():
    distance= int(input("Enter value of distance "))
    time= int(input("Enter value of time "))
 #  velocity= distance * time
    output= str(distance * time)
    print("The result= " +  output)

def main():
    user_choice = input("Enter operation of your choice (a, b, c, d, e): ")

    if user_choice == "a":
        a()
    if user_choice == "b":
        b()
    if user_choice == "c":
        c()
    if user_choice == "d":
        d()
    if user_choice == "e":
        e()
if __name__ == "__main__":
    main()