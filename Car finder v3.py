def car_finder_v3():
  """
  A program to display, search, add, and exit authorized vehicles.
  """

  allowed_vehicles_list = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan"]

  print("*****************************")
  print("AutoCountry Vehicle Finder v0.3")
  print("*****************************")
  print("Please enter the following number below from the following menu:")
  print("\n1. PRINT all authorized vehicles")
  print("2. SEARCH for authorized vehicle")
  print("3. ADD Authorized Vehicle")
  print("4. Exit")
  print("*****************************")

  choice = input("Enter your choice (1, 2, 3, or 4): ")

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
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
  else:
    print("Invalid choice.")

if __name__ == "__main__":
  car_finder_v3()