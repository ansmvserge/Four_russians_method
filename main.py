import numpy as np
import math


def calculate_block_size(matrix_a, matrix_b):
    """ Block split calculation

    :param matrix_a: Left matrix
    :param matrix_b: Right matrix
    :return: block size (-1 if matrices are incorrect)
    """
    dim_a = matrix_a.shape[0]
    dim_b = matrix_b.shape[0]
    if dim_a == dim_b:
        return math.floor(math.log2(dim_a))
    else:
        return -1


def split_block(row, start, size, matrix):
    """Split block from matrix (row or column)

    :param row: true if extracting block is a row, false if extracting block is a column
    :param start: start index to cut from
    :param size: size of extracting block
    :param matrix: matrix to extract from
    :return: extracted block
    """
    if row:
        block_size = min(size, matrix.shape[0])
        extracted_row = matrix[start: start + block_size]
        result_block = np.asmatrix(extracted_row)
    else:
        block_size = min(size, matrix.shape[1])
        extracted_column = []
        for i in range(matrix.shape[0]):
            extracted_column.append(matrix[i][start: start + block_size])
        result_block = np.asmatrix(extracted_column)
    return result_block


def rows_disjunction(matrix_a, matrix_a_index, matrix_b, matrix_b_index):
    """Matrix (vector) disjunction

    :param matrix_a: left matrix
    :param matrix_a_index: left matrix index
    :param matrix_b: right matrix
    :param matrix_b_index: right matrix index
    :return: disjunction vector
    """
    row_vector = matrix_a[matrix_a_index].copy()
    column_vector = np.asarray(matrix_b[matrix_b_index]).reshape(-1)
    for i, item in enumerate(column_vector):
        row_vector[i] = int(row_vector[i]) | int(item)
    return row_vector


def multiply_bit_matrices(left_matrix, right_matrix):
    """

    :param left_matrix: row matrix block
    :param right_matrix: column matrix block
    :return: multiplied matrix
    """
    size = left_matrix.shape[0]
    counter = 0
    res_matrix = np.zeros((size, size))
    vectors_table = np.zeros((pow(2, left_matrix.shape[1]), size))
    between_powers = 1

    for i in range(1, pow(2, left_matrix.shape[1])):
        new_row = rows_disjunction(vectors_table, i - pow(2, counter), right_matrix, right_matrix.shape[0] - counter - 1)
        vectors_table[i,:] = new_row
        if between_powers == 1:
            counter += 1
            between_powers = i + 1
        else:
            between_powers -= 1
    for i in range(size):
        res_matrix[i] = vectors_table[convert_to_int(left_matrix[i])]
    return res_matrix


def convert_to_int(row):
    """Convert binary row to int

    :param row: bool vector
    :return: int number
    """
    row = np.asarray(row).reshape(-1)
    bit_str = ""
    for i in range(len(row)):
        bit_str += str(row[i])
    return int(bit_str,2)


def matrix_ior(matrix_a, matrix_b):
    """ 'OR' matrices operation

    :param matrix_a: left matrix
    :param matrix_b: right matrix
    :return: result matrix
    """
    for i in range(matrix_a.shape[0]):
            for j in range(matrix_a.shape[1]):
                matrix_a[i][j] = int(matrix_a[i][j]) | int(matrix_b[i][j])
    return matrix_a


def four_russians_method(matrix_a, matrix_b):
    """Calculating matrix multiplication by 4 Russians method

    :param matrix_a: First matrix
    :param matrix_b: Second matrix
    :return: result matrix
    """
    dim = matrix_a.shape[0]
    block_size = calculate_block_size(matrix_a, matrix_b)
    number_of_blocks = math.ceil(dim/block_size)
    result_matrix = np.zeros((dim, dim))
    for i in range(number_of_blocks):
        column_block = split_block(False, i * block_size, block_size, matrix_a)
        row_block = split_block(True, i * block_size, block_size, matrix_b)
        multiplied_block = multiply_bit_matrices(column_block, row_block)
        result_matrix = matrix_ior(result_matrix, multiplied_block)
    return result_matrix.astype(int)


def main():
    # Read left matrix
    matrix_A = np.loadtxt("matrixA.txt", dtype='i', delimiter=',')

    # Read second matrix
    matrix_B = np.loadtxt("matrixB.txt", dtype='i', delimiter=',')

    if (matrix_A.shape[0] == matrix_A.shape[1] & matrix_B.shape[0] == matrix_B.shape[1] & matrix_A.shape[0] == matrix_B.shape[1]):
        print(four_russians_method(matrix_A, matrix_B))


if __name__ == "__main__":
    main()
