import json
from hash_tables.hashTableChaining import HashTableChaining
from hash_tables.hashTableProbing import HashTableProbing

def read_file():
    with open("data.json", "r") as f:
        data = json.load(f)
    return data

def main():
    table_to_use = input("Do you want to use chaining?(y/n): ")
    if table_to_use == "y":
        print("Reading into table with chaining...")
        table = HashTableChaining()
    elif table_to_use == "n":
        print("Reading into table with probing")
        table = HashTableProbing()
    data = read_file()
    for i in data:
        table.add(i)
    while True:
        command = input("Enter the command(add/search/remove/show/exit): ")
        if command == "add":
            cypher = input("Enter the cypher: ")
            name = input("Enter the name: ")
            number = int(input("Enter the number: "))
            comm = [cypher, name, number]
            table.add(comm)
        elif command == "search":
            cypher = input("Enter the cypher: ")
            print(table.search(cypher))
        elif command == "remove":
            cypher = input("Enter the cypher: ")
            name = input("Enter the name: ")
            print(table.delete([cypher, name]))
        elif command == "show":
            order_by = input("Enter the order key(/cypher/name/count): ")
            table.show(order_by)
        elif command == "exit":
            break
        else:
            print("Wrong command")

if __name__ == '__main__':
    main()