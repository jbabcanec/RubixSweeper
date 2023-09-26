# Sample test code to test the Rubix class methods for rotation and updating adjacent faces

# Dummy Minesweeper class for demonstration (replace with your actual Minesweeper class)
class Minesweeper:
    def __init__(self, board):
        self.board = board

# Dummy rotate_2d_array function for demonstration (replace with your actual function from utils.py)
def rotate_2d_array(matrix, direction):
    if direction == 'clockwise':
        return [list(reversed(row)) for row in zip(*matrix)]
    else:
        return matrix

# Rubix class (simplified for this test)
class Rubix:
    def __init__(self):
        self.faces = {
            'front': Minesweeper([[' ', '1'], ['1', 'M']]),
            'back': Minesweeper([['1', 'M'], ['M', '2']]),
            'left': Minesweeper([['M', '1'], ['2', '2']]),
            'right': Minesweeper([['2', '2'], ['1', 'M']]),
            'top': Minesweeper([[' ', '1'], ['1', '1']]),
            'bottom': Minesweeper([['1', '1'], ['1', ' ']])
        }

    def rotate_face(self, face_name, direction):
        face_to_rotate = self.faces[face_name].board
        rotated_face = rotate_2d_array(face_to_rotate, direction)
        self.faces[face_name].board = rotated_face

    def update_adjacent_faces(self, face_name, direction):
        if face_name == 'front':
            top_face = self.faces['top'].board
            bottom_face = self.faces['bottom'].board
            left_face = self.faces['left'].board
            right_face = self.faces['right'].board
            front_face = self.faces['front'].board
            
            if direction == 'clockwise':
                top_face[-1] = front_face[0]
                bottom_face[0] = front_face[-1]
                for i in range(len(right_face)):
                    right_face[i][-1], left_face[i][0] = front_face[i][-1], front_face[i][0]
                    
    def print_faces(self):
        for face_name, face in self.faces.items():
            print(f"{face_name} face:")
            for row in face.board:
                print(row)
            print()

# Initialize Rubix instance and print initial state
rubix = Rubix()
print("Initial state:")
rubix.print_faces()

# Rotate the 'front' face clockwise
rubix.rotate_face('front', 'clockwise')

# Update adjacent faces
rubix.update_adjacent_faces('front', 'clockwise')

# Print state after rotation
print("State after clockwise rotation of 'front' face:")
rubix.print_faces()

