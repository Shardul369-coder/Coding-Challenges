"""
Write a Python program that:
1) Asks the user whether they want to generate a Series or a DataFrame based on the user's choice.
#For Series:
  a] Ask how many elements the Series should have.
  b] Generate a Pandas Series with random numbers (0 to 1).
  c] Set the index as consecutive lowercase alphabets ('a', 'b', 'c', etc.).
#For DataFrame:
  a] Ask for the total number of elements.
  b] Ask for the number of rows and columns.
  c] Generate a Pandas DataFrame with random numbers reshaped according to rows and columns.
  d] Set the row index as consecutive lowercase alphabets.
2) Allow multiple repetitions based on user input.
3) Validate that the number of rows × columns matches the total number of elements for DataFrame.
4) Handle invalid inputs gracefully.
"""

import numpy as np
import pandas as pd
import string

class MySeries:
    def __init__(self, n):
        self.s = pd.Series(np.random.rand(n))
        alpha = list(string.ascii_lowercase[:n])
        self.s.index = alpha
        print(self.s)

class MyDataFrame:
    def __init__(self, n, rows, columns):
        self.df = pd.DataFrame(np.random.rand(n).reshape(rows, columns))
        alpha = list(string.ascii_lowercase[:rows])
        self.df.index = alpha
        print(self.df)

def main():
    choice = input("Enter your choice (Series/DataFrame): ").strip().lower()
    
    if choice not in ['series', 'dataframe']:
        print("Invalid choice. Please enter 'Series' or 'DataFrame'.")
        return

    try:
        repetitions = int(input("Enter the number of repetitions: "))
        
        for _ in range(repetitions):
            if choice == 'series':
                n = int(input("Enter the number of elements: "))
                MySeries(n)
            else:
                n = int(input("Enter the total number of elements: "))
                rows = int(input("Enter number of rows: "))
                columns = int(input("Enter number of columns: "))
                
                if rows * columns != n:
                    print(f"Error: rows x columns must equal {n}. Try again.")
                    continue

                MyDataFrame(n, rows, columns)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
