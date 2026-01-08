import json
import os

file_name = "vault_data.json"


if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        json.dump({}, f)

while True:
    print("\n--- Vault Lite ---")
    print("1. View credentials")
    print("2. Add credential")
    print("3. Update credential")
    print("4. Exit")

    choice = input("Enter choice: ")

    # red data fron file
    with open(file_name, "r") as f:
        data = json.load(f)

    # -------- Veiw -----------
    if choice == "1":
        if data == {}:
            print("No credentials saved.")
        else:
            num = 1
            for key in data:
                print(num, key)
                num += 1

    
    elif choice == "2":
        website = input("Enter website: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        key = website + "_" + username
        data[key] = password

        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

        print("Credential saved.")

    
    elif choice == "3":
        if data == {}:
            print("No data to update.")
        else:
            keys = list(data.keys())
            num = 1
            for k in keys:
                print(num, k)
                num += 1

            index = int(input("Enter number: ")) - 1
            new_pass = input("Enter new password: ")

            data[keys[index]] = new_pass

            with open(file_name, "w") as f:
                json.dump(data, f, indent=4)

            print("Password updated.")

    
    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Wrong choice.")