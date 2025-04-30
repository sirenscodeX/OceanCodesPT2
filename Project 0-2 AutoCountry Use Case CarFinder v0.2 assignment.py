def car_finder_v2_revised():
  """
  A program to display and search for authorized vehicles (revised).
  """

  allowed_vehicles_list = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan"]

  print("*****************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("*****************************")
  print("Please enter the following number below from the following menu:")
  print("\n1. PRINT all authorized vehicles")
  print("2. SEARCH for authorized vehicle")
  print("3. Exit")
  print("*****************************")

  choice = input("Enter your choice (1, 2, or 3): ")

  if choice == "2":
    search_term = input("Please Enter the full Vehicle name to search: ")
    if search_term in allowed_vehicles_list:
      print(f"\nYes, '{search_term}' is an authorized vehicle.")
    else:
      print(f"\nSorry, '{search_term}' is NOT an authorized vehicle.")
  elif choice == "1":
    print("\nAuthorized Vehicles:")
    for vehicle in allowed_vehicles_list:
      print(f"- {vehicle}")
  elif choice == "3":
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
  else:
    print("Invalid choice.")

if __name__ == "__main__":
  car_finder_v2_revised()