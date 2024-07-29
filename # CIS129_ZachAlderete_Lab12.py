# CIS129_ZachAlderete_Lab12
# 7/28/2024
# Program defines a pet class that represents a name, type, and age. Program creates an instance and promps a user to input pet detaisl. Lastly, prints user input. 

class Pet:
    # Declaring fields and values
    def __init__(self, name='', pet_type='', age=0):
        self.__name = name
        self.__type = pet_type
        self.__age = age

    # Methods to set
    def setName(self, n):
        self.__name = n

    def setType(self, t):
        self.__type = t

    def setAge(self, a):
        self.__age = a

    # Methods to get
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age

def main():
   
    # Pet object
    Animal = Pet()

    # Prompts the user to enter the pet's name, type, age and set them
    print("Enter a pet name:")
    inputName = input()
    Animal.setName(inputName)

    print("Enter a pet type:")
    inputType = input()
    Animal.setType(inputType)

    print("Enter a pet age:")
    inputAge = int(input())
    Animal.setAge(inputAge)

    # Print user input
    print("The pet name is", Animal.getName())
    print("The pet type is", Animal.getType())
    print("The pet age is", Animal.getAge())

if __name__ == "__main__":
    main()