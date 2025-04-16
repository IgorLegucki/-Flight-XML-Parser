def get_status_choice() -> str:
    print("Select flight status to display:")
    print("1. scheduled")
    print("2. delayed")
    print("3. cancelled")

    while True:
        choice = input("Your choice (1-3): ").strip()
        if choice == "1":
            return "scheduled"
        elif choice == "2":
            return "delayed"
        elif choice == "3":
            return "cancelled"
        else:
            print("Invalid selection, please try again.")
