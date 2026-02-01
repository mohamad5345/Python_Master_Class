# matrix = [
#     ['a11', 'a12', 'a13'],
#     ['a21', 'a22', 'a23'],
#     ['a31', 'a32', 'a33']
# ]
def Matrix():

    matrix = []
    # Function for creating rows
    def create_rows():
        for i in range(3):
            row_input = input(f'Enter number of Row {i+1} with space: ')
            row = list(map(int, row_input.split()))
            matrix.append(row)
            print(matrix)

    # Function for sum rows
    def sum_rows():
        print("\nRow sums:")
        for i in range(3):
            row_sum = sum(matrix[i])
            print(f"Row {i+1}: {row_sum}")

    def create_and_sum_columns():
        print("\nColumn sums:")
        for j in range(3):
            col_sum = 0
            for i in range(3):
                col_sum += matrix[i][j]
            print(f"Column {j + 1}: {col_sum}")

    # Running the functions
    create_rows()
    sum_rows()
    create_and_sum_columns()


Matrix()