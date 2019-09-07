import json

class Address:
    def __init__(self, street, house, apartments):
        self.street = street
        self.house = house
        self.apartments = apartments
    def __str__(self):
        return self.street + ", " + self.house + ", " + self.apartments

class Telephone:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

class Person:
    def __init__(self, surname, name, second_name, street, house, apartments, number):
        self.surname = surname
        self.name = name
        self.second_name = second_name
        self.address = Address(street, house, apartments)
        self.phone = Telephone(number)

    def __str__(self):
        return self.surname.capitalize() + " " + self.name.capitalize() \
               + " " + self.second_name.capitalize() + " " + str(self.address) + " " + str(self.phone)

def read_file():
    """Read file with data in order to reuse it again and again."""
    people = []
    with open("database.json", "r") as f:
        data = json.load(f)
    for p in data:
        print(p)
        people.append(Person(p["surname"], p["name"], p["second_name"],
                             p["street"], p["house"], p["apartments"],
                             p["phone"]))
    return people

def search(people):
    """Search for the person by name and street"""
    name = input("Enter the name: ")
    street = input("Enter the street: ")
    for i in range(len(people)):
        if people[i].name == name and people[i].address.street == street:
            return i
    return -1

def add(people):
    """Add a new person."""
    surname = input("Enter the surname: ")
    name = input("Enter the name: ")
    second_name = input("Enter the second_name: ")
    street = input("Enter the street: ")
    house = input("Enter the house: ")
    apartments = input("Enter the apartments: ")
    phone = input("Enter the phone: ")

    people.append(Person(surname, name, second_name, street, house, apartments, phone))
    return people

def remove(people):
    """Remove a person by name and street."""
    index = search(people)
    if index != -1:
        people.pop(index)
    else:
        print("There is no such a person added yet!")
    return people

def write_file(people):
    """Write the data we have into the json file."""
    data = []
    for p in people:
        data.append({"name": p.name, "surname": p.surname, "second_name": p.second_name,
                     "street": p.address.street, "house": p.address.house, "apartments": p.address.apartments,
                     "phone": p.phone.number})
    with open("database.json", "w") as f:
        json.dump(data, f)

def main():
    """Main function"""
    people = read_file()

    while True:
        command = input("Enter the command please(add/search/remove/exit): ")
        if command == "add":
            people = add(people)
        elif command == "search":
            index = search(people)
            if index != -1:
                print(people[index])
            else:
                print("Person not found!")
        elif command == "remove":
            people = remove(people)
        elif command == "exit":
            break
        else:
            print("Incorrect command!!!")
        for p in people:
            print(p)

    write_file(people)

if __name__ == "__main__":
    main()