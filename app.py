from db import delete_row, get_all_details, get_details_by_id, insert_row, update_name


def run():

    while True:
        print("1. Insert")
        print("2. Update")
        print("3. Get")
        print("4. Get all")
        print("5. Delete")
        print("6. Exit")
        user_input = int(input("Choose an option: "))

        if user_input == 1:
            name = input("\nPlease enter name: \n")
            email = input("\nPlease enter email: \n")
            insert_row(name, email)
            print("\nInsert successful\n")

        elif user_input == 2:
            id = input("\nPlease enter id: \n")
            name = input("\nPlease enter name: \n")
            update_name(id, name)
            print("\nUpdate successful\n")

        elif user_input == 3:
            id = input("\nPlease enter id: \n")
            res = get_details_by_id(id)
            for data in res:
                print(f"ID : {data.id}\n")
                print(f"Name : {data.name}\n")
                print(f"Email : {data.email}\n")
        
        elif user_input == 4:
            res = get_all_details()
            for data in res:
                print(f"ID : {data.id}\n")
                print(f"Name : {data.name}\n")
                print(f"Email : {data.email}\n")

        elif user_input == 5:
            id = input("\nPlease enter id: \n")
            res = delete_row(id)

        elif user_input == 6:
            break

        else:
            print("\nWrong input\n")

run()