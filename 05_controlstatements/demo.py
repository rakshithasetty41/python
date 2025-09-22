# Student Grade Tracker

# Collect student details
student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
attendance = int(input("Enter Attendance Percentage: "))

# Variables for score tracking
total_score = 0
count_scores = 0

# Repeatedly ask for scores
while True:
    score = float(input("Enter score: "))
    total_score += score
    count_scores += 1

    choice = input("Do you want to enter another score? (yes/no): ").lower()
    if choice != "yes":
        break

# Calculate average
average_score = total_score / count_scores if count_scores > 0 else 0

# Determine grade
if average_score >= 85:
    grade = "A"
elif average_score >= 70:
    grade = "B"
elif average_score >= 50:
    grade = "C"
else:
    grade = "FAIL"

# Attendance criteria
if attendance < 75:
    attendance_status = "WARNING: LOW ATTENDANCE"
else:
    attendance_status = "OK: GOOD ATTENDANCE"

# Award eligibility
if grade == "A" and attendance >= 75:
    award = "Eligible for Award"
else:
    award = "Not Eligible for Award"

# Output section
print("\n===== Student Report =====")
print("Student ID      :", student_id)
print("Student Name    :", student_name)
print("Attendance      :", str(attendance) + "%")
print("Total Score     :", total_score)
print("Average Score   :", round(average_score, 2))
print("Number of Scores:", count_scores)
print("Student Grade   :", grade)
print("Attendance Info :", attendance_status)
print("Award Eligibility:", award)

