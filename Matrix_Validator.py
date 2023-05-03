import re
import json


def validate_matrix(matrix):
    # Define the pattern that the strings should follow
    pattern = re.compile(r"^[A-Z][A-Za-z]{0,10}(_[A-Za-z]{0,10})*$")
    
    # Validate that all elements in the matrix are strings
    if not all(isinstance(element, str) for row in matrix for element in row):
        raise ValueError("All elements in the matrix must be strings")
    
    # Validate that there are no repeated elements in each column
    if any(len(set(column)) != len(column) for column in zip(*matrix)):
        raise ValueError("There cannot be repeated elements in each column")
    
    # Validate that there are no null or empty elements
    if any(not element or element.isspace() for row in matrix for element in row):
        raise ValueError("There cannot be null or empty elements")
    
    # Validate that the strings follow the defined pattern
    if any(not pattern.match(element) for row in matrix for element in row):
        raise ValueError("Elements must be strings of maximum 12 characters that start with uppercase letters and only contain letters and underscores")
    
    # Export the matrix as a JSON
    num_rows, num_cols = len(matrix), len(matrix[0])
    matrix_json = {"num_rows": num_rows, "num_cols": num_cols, "data": matrix}
    return json.dumps(matrix_json)


# Example usage

matrix = [["Apple", "Banana", "Cherry"], ["Polka" ,"El_der_ey", "Fig"]]

validate_matrix(matrix)
