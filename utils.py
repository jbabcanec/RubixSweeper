def rotate_2d_array(matrix, direction):
    if direction == 'clockwise':
        # Transpose and then reverse each row for clockwise rotation
        return [list(reversed(row)) for row in zip(*matrix)]
    elif direction == 'counterclockwise':
        # Reverse each row and then transpose for counterclockwise rotation
        return list(zip(*[reversed(row) for row in matrix]))
    else:
        return matrix  # Return the original matrix (should not happen)