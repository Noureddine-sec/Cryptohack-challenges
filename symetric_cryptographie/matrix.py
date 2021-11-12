def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    text=""
    for i in range (0,len(matrix)):
        for j in range (0, len(matrix[i])):
            text=text + chr(matrix[i][j])
            # print(chr(matrix[i][j]))
    return text
    print(text)


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

add_round_key=[[99, 114, 121, 112], [116, 111, 123, 114], [48, 117, 110, 100], [107, 51, 121, 125]]
print(matrix2bytes(matrix))
print(matrix2bytes(add_round_key))
