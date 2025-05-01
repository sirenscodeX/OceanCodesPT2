def car_finder_v8():
  """
  A program to display, search, add, delete, and exit authorized vehicles with confirmation.
  """

  allowed_vehicles_list = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan", "Rivian R1T"]

  print("*****************************")
  print("AutoCountry Vehicle Finder v0.4")
  print("*****************************")
  print("Please enter the following number below from the following menu:")
  print("\n1. PRINT all Authorized Vehicles")
  print("2. SEARCH for Authorized Vehicle")
  print("3. ADD Authorized Vehicle")
  print("4. DELETE Authorized Vehicle")
  print("5. Exit")
  print("*****************************")

  choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

  if choice == "1":
    print("\nAuthorized Vehicles:")
    for vehicle in allowed_vehicles_list:
      print(f"- {vehicle}")
  elif choice == "2":
    search_term = input("Please Enter the full Vehicle name to search: ")
    if search_term in allowed_vehicles_list:
      print(f"\nYes, '{search_term}' is an authorized vehicle.")
    else:
      print(f"\nSorry, '{search_term}' is NOT an authorized vehicle.")
  elif choice == "3":
    add_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
    allowed_vehicles_list.append(add_vehicle)
    print(f"\n'{add_vehicle}' has been added to the authorized vehicles list.")
  elif choice == "4":
    delete_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    if delete_vehicle in allowed_vehicles_list:
      confirmation = input(f"Are you sure you want to remove '{delete_vehicle}' from the Authorized Vehicles list? (yes/no): ")
      if confirmation.lower() == "yes":
        allowed_vehicles_list.remove(delete_vehicle)
        print(f"\nYou have REMOVED '{delete_vehicle}' as an authorized vehicle.")
      else:
        print(f"\nDeletion of '{delete_vehicle}' cancelled.")
    else:
      print(f"\nSorry, '{delete_vehicle}' is not in the authorized vehicles list.")
  elif choice == "5":
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
  else:
    print("Invalid choice.")

if __name__ == "__main__":
  car_finder_v8()