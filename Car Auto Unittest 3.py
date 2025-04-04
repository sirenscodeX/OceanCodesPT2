def car_finder():
  """
  A simple program to display allowed vehicles from a list.
  """

  allowed_vehicles_list = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan"]

  while True:
    print("\nCarFinder Menu:")
    print("1. Print Allowed Vehicles")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
      print("\nAllowed Vehicles:")
      for vehicle in allowed_vehicles_list:
        print(f"- {vehicle}")
    elif choice == "2":
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
      input("Press Enter to close...")  # Wait for Enter keypress
      break
    else:
      print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
  car_finder()