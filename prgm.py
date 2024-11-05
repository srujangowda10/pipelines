# calculate_average.py

# List of student grades
grades = [85, 92, 78, 88, 95, 80, 70]

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Calculate the average grade
average_grade = calculate_average(grades)

# Write the result to a text file
with open("average_grade.txt", "w") as file:
    file.write(f"The average grade is: {average_grade:.2f}")

# Output to console (optional)
print(f"The average grade is: {average_grade:.2f}")
