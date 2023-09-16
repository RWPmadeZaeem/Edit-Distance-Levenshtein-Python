def levenshtein_distance(str1, str2):
    # Create a matrix to store the distances between characters
    matrix = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    # Initialize the first row and column of the matrix
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    for j in range(len(str2) + 1):
        matrix[0][j] = j

    # Fill in the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # Deletion
                matrix[i][j - 1] + 1,      # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )

    # Print the matrix
    print("Levenshtein Distance Matrix:")
    for row in matrix:
        print(row)

    # The final value in the matrix is the Levenshtein distance
    levenshtein_distance = matrix[len(str1)][len(str2)]
    print(f"The Levenshtein distance between '{str1}' and '{str2}' is {levenshtein_distance} operations.")

    # Return both the matrix and the number of operations
    return matrix, levenshtein_distance

# Example usage:
str1 = "kitten"
str2 = "sitting"
matrix, distance = levenshtein_distance(str1, str2)
