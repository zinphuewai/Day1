
students = []
grade_categories = ("Excellent", "Good", "Pass", "Fail")

# Get student information
for i in range(5):
    print(f"\nStudent {i + 1}")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    study_hours = float(input("Enter study hours: "))
    score = float(input("Enter Python score: "))

    while score < 0 or score > 100:
        print("Invalid marks")
        score = float(input("Enter Python score: "))

    student = {
        "name": name,
        "age": age,
        "study_hours": study_hours,
        "score": score
    }

    students.append(student)


# Classify grade
def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid marks"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


# Calculate average
def calculate_average(scores):
    total = 0

    for score in scores:
        total += score

    return total / len(scores)


# Count passing students
def count_passed(students):
    count = 0

    for student in students:
        if student["score"] >= 40:
            count += 1

    return count


# Display report
print("\n===== STUDENT PERFORMANCE REPORT =====")

scores = []
for student in students:
    score = student["score"]
    scores.append(score)

    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Study Hours:", student["study_hours"])
    print("Score:", score)
    print("Grade:", classify_grade(score))
    print()

# Summary
print("===== SUMMARY =====")

print("Total Students:", len(students))
print("Average Score:", calculate_average(scores))
print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print("Passed Students:", count_passed(students))
print("Failed Students:", len(students) - count_passed(students))

# Find top student
top_student = students[0]

for student in students:
    if student["score"] > top_student["score"]:
        top_student = student

print("Top Student:", top_student["name"])
