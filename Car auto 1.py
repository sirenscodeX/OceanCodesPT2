def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

def main():
    # Required input for Unit Test #1: OnLoad (Program execution)
    display_menu()
    
    while True:
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\nDisplaying authorized vehicles...")
        elif choice == '2':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
