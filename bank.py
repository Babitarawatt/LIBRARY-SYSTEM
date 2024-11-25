heading = "Bank Management System"
print(heading)
bankaccount = {}

def createaccount():
    print("Create your New Account")
    email = input("Enter your Email ID : ")
    if email in bankaccount:
        print("An Account with this Email ID already exists")
        return
    
    name = input("Enter Name")
    age = int(input("Enter Age"))
    address = input("Enter Address ")
    mobile = input("Enter Mobile Number")
    gender = input("Enter Gender M/F")

    bankaccount[email] = {
        "name" : name,
        "age" : age,
        "address" : address,
        "mobile" : mobile,
        "gender" : gender,
        "balance" : 0.0
    }

    print("Account Created Successfully")

def viewaccount():
    print("View Your Account Details")
    email = ("Enter your Email ID to login")

    if email not in bankaccount:
        print("No account is found with this Email ID")

    details = bankaccount[email]
    print(f"Account details for {email}:")
    for key, value in details.items():
        print(f"{key}: {value}")

def creditamount():
    print("Credit Amount")
    email = input("Enter your Email ID")

    if email not in bankaccount:
        print("No account is found with this Email ID")
        return
    
    amount = float(input("Enter Amount to Credit"))
    bankaccount[email]["Balance"] += amount
    print(f"Amount credited successfully! New Balance:{bankaccount[email]} ")


def debitamount():
    print("Debit Amount")
    email = input("Enter your Email ID ")

    if email not in bankaccount:
        print("No account is found with this Email ID")
        return
    
    amount = float(input("Enter Amount to Debit"))
    if amount > bankaccount[email]["Balance"]:
        print("Insufficient balance!")
    else:
        bankaccount[email]["balance"] -= amount
        print(f"Amount credited successfully! New Balance:{bankaccount[email]["balance"]} ")


def deleteaccount():
    print("\nDelete Account")
    email = input("Enter your Email ID to delete ")

    if email not in bankaccount:
        print("No account found with this Email ID/!")
        return
    
    confirm = input("Are you sure you want to delete this account? (yes/no):").lower()
    if confirm == "yes":
        del bankaccount[email]
        print("Account deleted successfully!")
    else:
        print("Account deletion canceled.")

def main():
    while True:
        print("/nBank Management System")
        print("1. Create Account")
        print("2. View Account")
        print("3. Credit amount ")
        print("4. Debit Amount")
        print("5. Delete Account")
        print("6. Exit")
        choice = input("Enter your choice")

        if choice == "1":
            createaccount()
        elif choice == "2":
            viewaccount()
        elif choice == "3":
            creditamount()
        elif choice == "4":
            debitamount()
        elif choice == "5":
            deleteaccount()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()