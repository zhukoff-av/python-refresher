# Task 1: Calculate student averages and find the best student
# Input: Dictionary with student names (keys) and lists of grades (values)
# Output: Name of best student and their average grade

# Algorithm:
# 1. Create empty dictionary for averages
# 2. For each student:
#    - Calculate average grade (sum/count)
#    - Store in averages dictionary
# 3. Find student with highest average
# 4. Return best student's name and their average

students_data = {
    'Ann': [3, 4, 3, 3, 5],
    'Andrey': [1, 3, 2, 1],
    'Alex': [2, 3, 2, 2]
}


def find_average(students):
    averages = {}
    for name, grade in students.items():
        avg = sum(grade) / len(grade)
        averages[name] = avg
    best_student = max(averages)
    return best_student, averages[best_student]


print(find_average(students_data))

# Task 2. How to get nested dict ?
