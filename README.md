🚀 NumPy Analyzer
A menu-driven Python application built using NumPy and Object-Oriented Programming (OOP) concepts. This project allows users to create, manipulate, analyze, and perform statistical operations on NumPy arrays through an interactive command-line interface.

📖 Project Overview
The NumPy Analyzer project provides a user-friendly environment for working with NumPy arrays. Users can create 1D, 2D, and 3D arrays, perform mathematical operations, manipulate data through indexing and slicing, combine or split arrays, search and sort values, and generate statistical insights.

🎯 Features
✅ Array Creation
Create 1D Arrays
Create 2D Arrays
Create 3D Arrays
Dynamic user input
Input validation
✅ Indexing and Slicing
Element access using indexing
Slice 1D arrays
Slice 2D arrays
Slice 3D arrays
✅ Mathematical Operations
Addition
Subtraction
Multiplication
Division
Dot Product
Matrix Multiplication
✅ Combine and Split Arrays
Combine arrays using np.concatenate()
Split arrays using np.split()
Row-wise splitting
Column-wise splitting
✅ Search, Sort and Filter
Search specific values
Sort arrays in ascending order
Sort arrays in descending order
Filter values greater than a specified number
✅ Statistical Operations
Sum
Mean
Median
Standard Deviation
Variance
Minimum Value
Maximum Value
Percentile
Correlation Coefficient
✅ Exception Handling
Invalid input checking
Dimension validation
Index validation
Division by zero prevention
Matrix compatibility checking
🛠 Technologies Used
Python 3.x
NumPy
Object-Oriented Programming (OOP)
📂 Project Structure
NumPy-Analyzer/
│
├── numpy_analyzer.py
├── README.md
└── requirements.txt
🔥 OOP Concepts Used
Constructor
def __init__(self):
    self.array = None
Class Method
@classmethod
def create_object(cls):
    return cls()
Static Method
@staticmethod
def show_message(message):
    print(message)
Encapsulation
All functionalities are organized inside the DataAnalytics class.

📋 Main Menu
===== NUMPY ANALYZER =====

1. Create NumPy Array
2. Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Aggregates and Statistics
6. Exit
▶️ Installation
Install NumPy:

pip install numpy
Or create a requirements.txt file:

numpy
Install dependencies:

pip install -r requirements.txt
🚀 How to Run
python numpy_analyzer.py
💻 Sample Output
===== NUMPY ANALYZER =====

1. Create NumPy Array
2. Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Aggregates and Statistics
6. Exit

Enter your choice: 1

1. 1D Array
2. 2D Array
3. 3D Array

Enter your choice: 1

Enter numbers separated by space:
10 20 30 40

Array created successfully:
[10. 20. 30. 40.]
📚 Learning Outcomes
This project helps in understanding:

NumPy Array Creation
Indexing and Slicing
Mathematical Operations
Array Combination and Splitting
Searching, Sorting and Filtering
Statistical Analysis using NumPy
Object-Oriented Programming in Python
Exception Handling
🔮 Future Enhancements
GUI using Tkinter
CSV File Support
Excel File Support
Data Visualization using Matplotlib
Pandas Integration
Analysis Report Export
