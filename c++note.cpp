
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int add(int a, int b) { return a + b; } // Function example

class Student {  // Class example
public:
    string name;
    int age;
    void display() { cout << name << " " << age << endl; }
};

int main() {
    // --------------------
    // 1. Variables & Data Types
    // --------------------
    int age = 20;
    float height = 5.7;
    double salary = 45000.50;
    char grade = 'A';
    string name = "Alice";
    bool isStudent = true;

    cout << "Name: " << name << ", Age: " << age << endl;

    // --------------------
    // 2. Input/Output
    // --------------------
    int num;
    cout << "Enter a number: ";
    cin >> num;
    cout << "You entered: " << num << endl;

    // --------------------
    // 3. Operators
    // --------------------
    cout << "5 + 3 = " << 5 + 3 << endl;
    cout << "5 > 3? " << (5 > 3) << endl;  // 1 = true
    cout << "Logical AND: " << (true && false) << endl;

    // --------------------
    // 4. Conditional Statements
    // --------------------
    if (num > 0) cout << "Positive" << endl;
    else if (num < 0) cout << "Negative" << endl;
    else cout << "Zero" << endl;

    // --------------------
    // 5. Loops
    // --------------------
    for (int i = 0; i < 3; i++) cout << i << " ";
    cout << endl;

    int i = 0;
    while (i < 3) { cout << i << " "; i++; }
    cout << endl;

    int j = 0;
    do { cout << j << " "; j++; } while (j < 3);
    cout << endl;

    // --------------------
    // 6. Arrays
    // --------------------
    int arr[3] = {1, 2, 3};
    for (int k = 0; k < 3; k++) cout << arr[k] << " ";
    cout << endl;

    // --------------------
    // 7. Vectors
    // --------------------
    vector<int> nums;
    nums.push_back(10);
    nums.push_back(20);
    cout << "Vector size: " << nums.size() << endl;

    // --------------------
    // 8. Strings
    // --------------------
    string str = "Hello";
    cout << str.length() << " " << str[0] << endl;

    // --------------------
    // 9. Functions
    // --------------------
    cout << "Add 5 + 3 = " << add(5, 3) << endl;

    // --------------------
    // 10. Classes & Objects
    // --------------------
    Student s;
    s.name = "Bob";
    s.age = 22;
    s.display();

    // --------------------
    // 11. File I/O
    // --------------------
    ofstream outFile("example.txt");
    outFile << "Hello, C++!";
    outFile.close();

    ifstream inFile("example.txt");
    string line;
    getline(inFile, line);
    cout << line << endl;
    inFile.close();

    return 0;
}
