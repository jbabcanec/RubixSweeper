from minesweeper import Minesweeper
from utils import rotate_2d_array

class Rubix:
    def __init__(self, size, mines):
        # Define faces of the Rubik's Cube
        self.faces = {
            'front': Minesweeper(size, mines),
            'back': Minesweeper(size, mines),
            'left': Minesweeper(size, mines),
            'right': Minesweeper(size, mines),
            'top': Minesweeper(size, mines),
            'bottom': Minesweeper(size, mines)
        }

    def update_adjacent_faces(self, face_name, direction):
        """
        Update the edge cells of adjacent faces after rotating a face.
        """
        # Define a dictionary to know which faces are adjacent to each face
        adjacent_faces = {
            'front': ['top', 'bottom', 'left', 'right'],
            'back': ['top', 'bottom', 'left', 'right'],
            'left': ['top', 'bottom', 'front', 'back'],
            'right': ['top', 'bottom', 'front', 'back'],
            'top': ['front', 'back', 'left', 'right'],
            'bottom': ['front', 'back', 'left', 'right']
        }
        
        # Get the Minesweeper boards of the adjacent faces
        adjacent_boards = {face: self.faces[face].board for face in adjacent_faces[face_name]}
        
        # If rotating the 'front' face
        if face_name == 'front':
            top_face = self.faces['top'].board
            bottom_face = self.faces['bottom'].board
            left_face = self.faces['left'].board
            right_face = self.faces['right'].board
            front_face = self.faces['front'].board
            
            # If rotating clockwise
            if direction == 'clockwise':
                # Update the top row of the 'top' face
                top_face[-1] = front_face[0]
                
                # Update the bottom row of the 'bottom' face
                bottom_face[0] = front_face[-1]
                
                # Update the rightmost column of the 'right' face and leftmost column of the 'left' face
                for i in range(len(right_face)):
                    right_face[i][-1], left_face[i][0] = front_face[i][-1], front_face[i][0]
            
            # If rotating counterclockwise
            elif direction == 'counterclockwise':
                # Similar logic, but reversed
                pass  # TODO

    def get_revealed(self, face_name):
        """
        Get the revealed status of a specific face.
        """
        return self.faces[face_name].revealed

    def get_flagged(self, face_name):
        """
        Get the flagged status of a specific face.
        """
        return self.faces[face_name].flagged


    def rotate_face(self, face_name, direction):
        """
        Rotate a face of the cube.
        """
        face_to_rotate = self.faces[face_name].board
        rotated_face = rotate_2d_array(face_to_rotate, direction)
        self.faces[face_name].board = rotated_face

    def reveal_cell(self, face_name, row, col):
        """
        Reveal a cell in the Minesweeper board of the specified face.
        """
        face = self.faces[face_name]
        face.reveal_cell(row, col)

    def flag_cell(self, face_name, row, col):
        """
        Toggle a flag on a cell on the Minesweeper board of the specified face.
        """
        face = self.faces[face_name]
        face.flag_cell(row, col)
        print(f"Flagged status in Rubix for cell ({row}, {col}) on face {face_name}: {face.flagged[row][col]}")


    def get_face(self, face_name):
        """
        Get the Minesweeper board of a specific face.
        """
        return self.faces[face_name].board
