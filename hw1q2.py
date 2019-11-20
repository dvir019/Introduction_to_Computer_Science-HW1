def main():
    """
    The program gets the employee type, the work day and the work hours,
    and calculates the employee's salary for that day.
    """

    # Set the employees types
    regular = "r"
    supervisor = "s"
    manager = "m"

    # Set the weekend days
    # *** No need to save the other days, because I will check if it's weekend,
    #     and if it's not, than it's weekday.
    friday = "fri"
    saturday = "sat"

    # Set the salaries per hour
    # *** Weekday = sunday until thursday
    #     Weekend = friday until saturday
    weekday_up_to_8_hours = 30
    weekday_more_than_8_hours = 35
    weekend_up_to_8_hours = 42
    weekend_more_than_8_hours = 49

    # Get the employee type
    print(f"Menu:\n{regular}: Regular\n{supervisor}: Supervisor\n{manager}: Manager")
    employee_type = input()

    # Get the work day
    print("\nEnter work day:")
    work_day = input()

    # Get the work hours
    print("Enter work hours:")
    work_hours = int(input())

    # Calculate the base salaries
    weekday_salary = weekday_up_to_8_hours * min(work_hours, 8) \
                     + weekday_more_than_8_hours * max(work_hours - 8, 0)
    weekend_salary = weekend_up_to_8_hours * min(work_hours, 8) \
                     + weekend_more_than_8_hours * max(work_hours - 8, 0)

    # Check if it's weekend
    is_weekend = (work_day == friday) or (work_day == saturday)

    # Calculate the total salary
    total_salary = weekend_salary * int(is_weekend) \
                   + weekday_salary * int(not is_weekend)
    total_salary *= 1 * int(employee_type == regular) \
                    + 1.2 * int(employee_type == supervisor) \
                    + 1.5 * int(employee_type == manager)
    # *** I know that the conversion to int is not necessary, but it's more comfortable for me

    # Print the result
    print(f"The daily salary is {total_salary:.1f}")


if __name__ == '__main__':
    main()
