class Pet:

    def __init__(self, name="Not Provided", type="Not Provided", age=0):
        self.__name = name
        self.__type = type
        self.__age = age

    def setName(self, name):
        self.__name = name
    def setType(self, type):
        self.__type = type
    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name
    def getType(self):
        return self.__type
    def getAge(self):
        return self.__age

    def __str__(self):
        return f"Name of Pet: {self.getName()}\nType of Animal: {self.getType()}\nAge of Pet: {self.getAge()}"

def main():
    myPet = Pet()
    print(myPet)

    print("Let's update the pet")
    name = input("Enter a name for the pet >> ")
    type = input("Enter the type of animal of the pet >> ")
    age = input("Enter the age of the pet >> ")

    myPet.setName(name)
    myPet.setType(type)
    myPet.setAge(age)

    print("Here are the updated details of the pet")
    print(myPet)


if __name__ == "__main__":
    main()