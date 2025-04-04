def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

def print_allowed_vehicles():
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")

def main():
    # Required input for Unit Test #1: OnLoad (Program execution)
    display_menu()
    
    while True:
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print_allowed_vehicles()  # Expected outcome for Unit Test #2
        elif choice == '2':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.\n")

if __name__ == "__main__":
    main()
