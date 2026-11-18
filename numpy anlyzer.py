import numpy as np


class DataAnalytics:
    def __init__(self):
        self.array = None

    @classmethod
    def create_object(cls):
        return cls()

    @staticmethod
    def show_message(message):
        print(message)

    def create_array(self):
        print("\n1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                values = input("Enter numbers separated by space: ").split()
                self.array = np.array([float(x) for x in values])

            elif choice == "2":
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                values = input("Enter array elements separated by space: ").split()

                if rows <= 0 or cols <= 0 or len(values) != rows * cols:
                    print("Please enter valid rows, columns and elements.")
                    return

                self.array = np.array([float(x) for x in values]).reshape(rows, cols)

            elif choice == "3":
                layers = int(input("Enter number of layers: "))
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                values = input("Enter array elements separated by space: ").split()

                if layers <= 0 or rows <= 0 or cols <= 0:
                    print("Dimensions must be positive.")
                    return

                if len(values) != layers * rows * cols:
                    print("Please enter the correct number of elements.")
                    return

                self.array = np.array([float(x) for x in values]).reshape(
                    layers, rows, cols
                )
            else:
                print("Invalid choice.")
                return

            print("Array created successfully:")
            print(self.array)

        except ValueError:
            print("Please enter numbers only.")

    def indexing_slicing(self):
        if self.array is None:
            print("Please create an array first.")
            return

        print("\nCurrent array:")
        print(self.array)
        print("1. Indexing")
        print("2. Slicing")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                if self.array.ndim == 1:
                    index = int(input("Enter index: "))
                    print("Element:", self.array[index])
                elif self.array.ndim == 2:
                    row = int(input("Enter row index: "))
                    col = int(input("Enter column index: "))
                    print("Element:", self.array[row, col])
                else:
                    layer = int(input("Enter layer index: "))
                    row = int(input("Enter row index: "))
                    col = int(input("Enter column index: "))
                    print("Element:", self.array[layer, row, col])

            elif choice == "2":
                if self.array.ndim == 1:
                    start = int(input("Enter start index: "))
                    end = int(input("Enter end index: "))
                    print(self.array[start:end])
                elif self.array.ndim == 2:
                    row_start = int(input("Enter row start: "))
                    row_end = int(input("Enter row end: "))
                    col_start = int(input("Enter column start: "))
                    col_end = int(input("Enter column end: "))
                    print(self.array[row_start:row_end, col_start:col_end])
                else:
                    layer_start = int(input("Enter layer start: "))
                    layer_end = int(input("Enter layer end: "))
                    row_start = int(input("Enter row start: "))
                    row_end = int(input("Enter row end: "))
                    col_start = int(input("Enter column start: "))
                    col_end = int(input("Enter column end: "))
                    print(self.array[
                        layer_start:layer_end,
                        row_start:row_end,
                        col_start:col_end
                    ])
            else:
                print("Invalid choice.")

        except (ValueError, IndexError):
            print("Please enter valid indices.")

    def mathematical_operations(self):
        if self.array is None:
            print("Please create an array first.")
            return

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = input("Enter your choice: ")

        try:
            if choice in ["5", "6"] and self.array.ndim != 2:
                print("This operation needs a 2D array.")
                return

            if choice == "5":
                values = input("Enter same number of elements for second array: ").split()
                if len(values) != self.array.size:
                    print("Enter the correct number of elements.")
                    return
                second = np.array([float(x) for x in values]).reshape(self.array.shape)
                print("Dot product:", np.sum(self.array * second))

            elif choice == "6":
                rows = int(input("Enter rows for second matrix: "))
                cols = int(input("Enter columns for second matrix: "))
                values = input("Enter second matrix elements: ").split()

                if rows <= 0 or cols <= 0 or len(values) != rows * cols:
                    print("Invalid dimensions or number of elements.")
                    return

                second = np.array([float(x) for x in values]).reshape(rows, cols)

                if self.array.shape[1] != second.shape[0]:
                    print("Matrix dimensions do not match.")
                else:
                    print("Matrix multiplication:")
                    print(np.matmul(self.array, second))

            elif choice in ["1", "2", "3", "4"]:
                values = input("Enter same number of elements for second array: ").split()

                if len(values) != self.array.size:
                    print("Enter the correct number of elements.")
                    return

                second = np.array([float(x) for x in values]).reshape(self.array.shape)

                if choice == "1":
                    result = self.array + second
                elif choice == "2":
                    result = self.array - second
                elif choice == "3":
                    result = self.array * second
                else:
                    if np.any(second == 0):
                        print("Division by zero is not allowed.")
                        return
                    result = self.array / second

                print("Result:")
                print(result)
            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid numbers.")

    def combine_split(self):
        if self.array is None:
            print("Please create an array first.")
            return

        print("\n1. Combine Arrays")
        print("2. Split Array")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                values = input("Enter elements for second array: ").split()
                if len(values) != self.array.size:
                    print("Enter the correct number of elements.")
                    return

                second = np.array([float(x) for x in values]).reshape(self.array.shape)

                if self.array.ndim == 1:
                    print("Combined array:")
                    print(np.concatenate((self.array, second)))
                else:
                    print("Combined array:")
                    print(np.concatenate((self.array, second), axis=0))

            elif choice == "2":
                if self.array.ndim == 1:
                    parts = int(input("Into how many parts? "))
                    if parts <= 0 or self.array.size % parts != 0:
                        print("Array cannot be split equally.")
                        return
                    print(np.split(self.array, parts))
                else:
                    print("1. Split rows")
                    print("2. Split columns")
                    axis_choice = input("Enter your choice: ")
                    axis = 0 if axis_choice == "1" else 1

                    if axis_choice not in ["1", "2"]:
                        print("Invalid choice.")
                        return

                    parts = int(input("Into how many parts? "))
                    if parts <= 0 or self.array.shape[axis] % parts != 0:
                        print("Array cannot be split equally.")
                        return
                    print(np.split(self.array, parts, axis=axis))
            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid input.")

    def search_sort_filter(self):
        if self.array is None:
            print("Please create an array first.")
            return

        print("\n1. Search a value")
        print("2. Sort array")
        print("3. Filter values")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                value = float(input("Enter value to search: "))
                positions = np.argwhere(self.array == value)
                if positions.size > 0:
                    print("Value found at index/indices:")
                    print(positions)
                else:
                    print("Value not found.")

            elif choice == "2":
                print("1. Ascending")
                print("2. Descending")
                order = input("Enter your choice: ")
                result = np.sort(self.array, axis=None)

                if order == "2":
                    result = result[::-1]
                elif order != "1":
                    print("Invalid choice.")
                    return

                print("Sorted array:")
                print(result)

            elif choice == "3":
                limit = float(input("Show values greater than: "))
                print(self.array[self.array > limit])

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")

    def statistics(self):
        if self.array is None:
            print("Please create an array first.")
            return

        print("\n1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum and Maximum")
        print("7. Percentile")
        print("8. Correlation")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                print("Sum:", np.sum(self.array))
            elif choice == "2":
                print("Mean:", np.mean(self.array))
            elif choice == "3":
                print("Median:", np.median(self.array))
            elif choice == "4":
                print("Standard deviation:", np.std(self.array))
            elif choice == "5":
                print("Variance:", np.var(self.array))
            elif choice == "6":
                print("Minimum:", np.min(self.array))
                print("Maximum:", np.max(self.array))
            elif choice == "7":
                percentile = float(input("Enter percentile from 0 to 100: "))
                if percentile < 0 or percentile > 100:
                    print("Percentile must be from 0 to 100.")
                else:
                    print("Percentile:", np.percentile(self.array, percentile))
            elif choice == "8":
                values = input("Enter same number of elements for second array: ").split()
                if len(values) != self.array.size:
                    print("Enter the correct number of elements.")
                    return

                second = np.array([float(x) for x in values]).reshape(self.array.shape)

                if self.array.size < 2:
                    print("At least two elements are required.")
                elif np.std(self.array) == 0 or np.std(second) == 0:
                    print("Correlation cannot be calculated for constant values.")
                else:
                    result = np.corrcoef(self.array.flatten(), second.flatten())[0, 1]
                    print("Correlation coefficient:", result)
            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid input.")

    def run(self):
        while True:
            print("\n===== NUMPY ANALYZER =====")
            print("1. Create NumPy Array")
            print("2. Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Aggregates and Statistics")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_array()
                if self.array is not None:
                    self.indexing_slicing()
            elif choice == "2":
                self.mathematical_operations()
            elif choice == "3":
                self.combine_split()
            elif choice == "4":
                self.search_sort_filter()
            elif choice == "5":
                self.statistics()
            elif choice == "6":
                print("Thank you for using NumPy Analyzer. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    obj = DataAnalytics.create_object()
    obj.run()