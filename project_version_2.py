# Initialize an empty dictionary to store student names and their grades.

students_grades = {}

#Define a list of subjects.

subjects = ["Programming", "Communications Engineering", "Networking Concepts", "Fundamentals Of Computing"]

# This will define the function to store grades and students

def adding_grades_of_students():

    # Ask for the student's name

    student_name = input("Enter the student's name: ")

    # Initialize an empty dictionary to store the current student's grades.

    grades = {}

    # Loop through each subject and ask for the grade.

    for subject in subjects:
        grade = input(f"Enter {student_name}'s grade for {subject}: ")
        grades[subject] = grade

    # Store the student's grades in the main dictionary. 
    students_grades[student_name] = grades 


# adding students and their grades.

number_of_students = int(input("How many students do you want to add? "))

for i in range(number_of_students):
    adding_grades_of_students()

# Display the grades

print("Student's grades: ")
for student, grades in students_grades.items():
    print(f"{student}: {grades}")
    
# Function to calculate the mean (average) of a list of grades.

def calculate_mean(grades):
    return sum(grades) / len(grades)

# Function to calculate the median of a sorted list of grades.

def calculate_median(grades):
    sorted_grades = sorted(grades)
    n = len(sorted_grades)
    mid = n // 2
    if n % 2 == 0:
        # If the list has an even number of elements, the median is the average of the two middle elements.
        return(sorted_grades[mid - 1] + sorted_grades[mid]) / 2
    else:
        # If the list has an odd number of elements, the median is the middle element.
        return sorted_grades[mid]
# This function will calculate the mode(s) (most frequent values in a list of grades.
def calculate_mode(grades):
    frequency = {}
    # This counts the frequency of each grade in the list.
    for grade in grades:
        frequency[grade] = frequency.get(grade, 0) + 1
    # This will determine the maximum frequency.
    max_frequency = max(frequency.values())
    # This identifies all grades that have the maximum frequency.
    modes = [key for key, val in frequency.items() if val == max_frequency]
    # This is will output message if all grades are equally common.
    if len(modes) == len(grades):
        return 'All numbers are equally common'
    # Otherwise, return the list of mode.
    return modes
# This will display a menu of options and return the user's choice.
def display_menu_and_get_choice():
    print("\nMenu of choices: ")
    print("1. Print the mean of the numbers")
    print("2. Print the median of the numbers")
    print("3. print the mode of the numbers")
    print("4. Go back and enter a new set of numbers")
    print("5. Exit the application")
    choice = input("Enter your choice: ")
    return choice
# Function to calculate skewness (asymmetry of the distribution) of a list of grades.
def calculate_skewness(grades):
    n = len(grades)
    # This calculates the mean of the grades.
    mean = calculate_mean(grades)
    # Standard deviation calculation without math.sqrt
    variance = sum((grade - mean) ** 2 for grade in grades) / n
    std_dev = variance ** 0.5  # Equivalent to math.sqrt(variance)
    # Skewness calculation without math library
    skewness = (n / ((n - 1) * (n - 2))) * sum(((grade - mean) / std_dev) ** 3 for grade in grades)
    return skewness

# Main function to drive the program.
def main():
    grades = []  # Initialize the list to store grades.
    print("Enter grades one by one and type 'done' when you are finished:")

    while True:  # This loop should allow for continuous entry until 'done' is typed.
        grade_input = input("Enter a grade (or 'done' to finish): ")
        if grade_input.lower() == 'done':
            if len(grades) < 2:
                print("Please enter at least two numbers.")
            else:
                 break  # If 'done' is entered, break out of the loop.
        else:
            try:
                grade = int(grade_input)
                grades.append(grade)  # Add the grade to the list.
            except ValueError:
                print("Invalid input. Please Enter only numbers.")
                # If an invalid input is given, the loop continues, prompting for another grade.

    print(f"You have entered {len(grades)} grades.")

    while True:
        choice = display_menu_and_get_choice()
        if choice == '1':
            # Option 1: This prints the mean of the grades.
            print(f"Mean: {calculate_mean(grades)}")
        elif choice == '2':
            # Option 2: This will print the median of the grades.
            print(f"Median: {calculate_median(grades)}")
        elif choice == '3':
            # Option 3: This will print the mode of the grades.
            print(f"Mode: {calculate_mode(grades)}")
        elif choice == '4':
            # Option 4: This will clear the list and restart the main function.
            grades.clear()
            main()
            continue
        elif choice == '5':
            # Option 5: This will exit the application.
            print("Exiting the application.")
            break  # If '5' is entered, break out of the loop to exit the program.
        else:
            print("Invalid choice. Please try again.")
            # If an invalid choice is given, the loop continues, prompting for the menu again.

# This will check if the script is being run directly (not imported) and then it runs main();
if __name__ == "__main__":
    main()
