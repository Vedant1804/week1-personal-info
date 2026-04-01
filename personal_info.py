def main():
    # Stored information
    name = "Vedant"
    age = 22
    city = "Pune"
    university = "COEP Technological University"

    print("=" * 40)
    print("      Personal Information Manager")
    print("=" * 40)

    # User inputs
    fav_food = input("Enter your favorite food: ").strip()
    fav_color = input("Enter your favorite color: ").strip()

    # Calculation
    age_in_months = age * 12

    # Formatted output
    print("\n" + "-" * 40)
    print("            USER PROFILE")
    print("-" * 40)
    print(f"Name:           {name}")
    print(f"Location:       {city}")
    print(f"Education:      {university}")
    print(f"Current Age:    {age} ({age_in_months} months old)")
    print(f"Favorite Food:  {fav_food if fav_food else 'Home meal'}")
    print(f"Favorite Color: {fav_color if fav_color else 'Red'}")
    print("-" * 40)
    print("=" * 40)

if __name__ == "__main__":
    main()
