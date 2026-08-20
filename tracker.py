import json
from pathlib import Path

DATA_FILE = Path("applications.json")


def load_applications():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_applications(applications):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(applications, file, indent=4)


def add_application(applications):
    print("\nAdd a job application")
    company = input("Company name: ")
    role = input("Job title: ")
    location = input("Location or remote: ")
    date_applied = input("Date applied: ")
    status = input("Status (Applied/Interview/Rejected/Offer): ")

    applications.append({
        "company": company,
        "role": role,
        "location": location,
        "date_applied": date_applied,
        "status": status
    })

    save_applications(applications)
    print("Application saved successfully.\n")


def view_applications(applications):
    if not applications:
        print("\nNo job applications saved yet.\n")
        return

    print("\nYour job applications")
    print("-" * 60)

    for number, application in enumerate(applications, start=1):
        print(
            f"{number}. {application['role']} at {application['company']} | "
            f"{application['location']} | {application['status']}"
        )

    print()


def update_status(applications):
    view_applications(applications)

    if not applications:
        return

    try:
        number = int(input("Enter the application number to update: "))
        application = applications[number - 1]
        new_status = input("New status: ")

        application["status"] = new_status
        save_applications(applications)
        print("Status updated successfully.\n")
    except (ValueError, IndexError):
        print("That application number does not exist.\n")


def main():
    applications = load_applications()

    while True:
        print("JOB APPLICATION TRACKER")
        print("1. Add an application")
        print("2. View applications")
        print("3. Update application status")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            view_applications(applications)
        elif choice == "3":
            update_status(applications)
        elif choice == "4":
            print("Good luck with your applications!")
            break
        else:
            print("Please choose a number from 1 to 4.\n")


if __name__ == "__main__":
    main()
    