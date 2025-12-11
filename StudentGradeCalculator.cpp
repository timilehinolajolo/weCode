#include <iostream>
#include <string>
using namespace std;

// Function to calculate grade based on average
char calculateGrade(float avg) {
    if (avg >= 90) return 'A';
    else if (avg >= 80) return 'B';
    else if (avg >= 70) return 'C';
    else if (avg >= 60) return 'D';
    else return 'F';
}

int main() {
    string studentName;
    int numSubjects;

    cout << "Enter student name: ";
    getline(cin, studentName);

    cout << "Enter number of subjects: ";
    cin >> numSubjects;

    float marks[numSubjects];
    float total = 0;

    for (int i = 0; i < numSubjects; i++) {
        cout << "Enter marks for subject " << i + 1 << ": ";
        cin >> marks[i];
        total += marks[i];
    }

    float average = total / numSubjects;
    char grade = calculateGrade(average);

    cout << "\n--- Result ---\n";
    cout << "Student Name: " << studentName << endl;
    cout << "Total Marks: " << total << endl;
    cout << "Average Marks: " << average << endl;
    cout << "Grade: " << grade << endl;

    return 0;
}
