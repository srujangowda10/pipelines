# List of student grades
grades = [85, 92, 78, 88, 95, 80, 70]

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Calculate the average grade
average_grade = calculate_average(grades)

# Output the result
print(f"The average grade is: {average_grade:.2f}")
