
def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


def main():
    student_name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    marks = []
    total = 0

    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
        total += mark

    average = total / num_subjects
    grade = calculate_grade(average)

    print("\n--- Result ---")
    print(f"Student Name: {student_name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
