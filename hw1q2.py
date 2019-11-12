def main():
    # Set the employees types
    regular = "r"
    supervisor = "s"
    manager = "m"

    # Set the days
    sunday = "sun"
    monday = "mon"
    tuesday = "tue"
    wednesday = "wed"
    thursday = "thu"
    friday = "fri"
    saturday = "sat"

    # Get the employee type
    print("Menu:\nr: Regular\ns: Supervisor\nm: Manager")
    employee_type = input()

    # Get the work day
    print("Enter work day:")
    work_day = input()

    # Get the work hours
    print("Enter work hours:")
    work_hours = input()


if __name__ == '__main__':
    main()
