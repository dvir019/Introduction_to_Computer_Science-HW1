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

    # Set the salaries per hour
    # * Weekday = sunday until thursday
    # * Weekend = friday until saturday
    weekday_up_to_8_hours = 30
    weekday_more_than_8_hours = 35
    weekend_up_to_8_hours = 42
    weekend_more_than_8_hours = 49

    # Get the employee type
    print("Menu:\nr: Regular\ns: Supervisor\nm: Manager")
    employee_type = input()

    # Get the work day
    print("Enter work day:")
    work_day = input()

    # Get the work hours
    print("Enter work hours:")
    work_hours = input()

    # Calculate the base salaries


if __name__ == '__main__':
    main()
