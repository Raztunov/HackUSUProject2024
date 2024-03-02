from matrices import Matrix


def encrypt_str(string, matrix):
    ret = ""
    for i in range(len(string)):
        for v in range(len(matrix.ALPHABET)):
            if string[i] == matrix.ALPHABET[v]:
                for x in range(len(matrix.matrix[v])):
                    if matrix.matrix[v][x] == 1:
                        ret += matrix.ALPHABET[x]
        if string[i] not in matrix.ALPHABET:
            ret += string[i]
    return ret


def decrypt_str(string, matrix):
    ret = ""
    listna = []
    for i in range(len(matrix.matrix)):
        str = ""
        for v in range(len(matrix.ALPHABET)):
            if matrix.matrix[i][v] == 1:
                str += matrix.ALPHABET[v]
        listna.append(str)

    for z in range(len(string)):
        for k in range(len(listna)):
            lenta = len(listna[k])
            if string[z:z+lenta] == listna[k]:
                ret += matrix.ALPHABET[k]
        if string[z] not in matrix.ALPHABET:
            ret += string[z]
    return ret


def main():
    matrix_1 = Matrix()

    while True:
        sel = input("""
Would you like to :
(s) scramble the matrix, 
(r) row swap within the matrix, 
(a) encrypt the alphabet, 
(e) encrypt a string,
(d) decrypt a string, or
(q) quit? 
""")

        if sel == "s":
            matrix_1.scramble_matrix()

        elif sel == "r":
            row_1 = input("First row to swap: ")
            row_2 = input("Second row to swap: ")
            matrix_1.row_swap(row_1, row_2)

        elif sel == "a":
            inp = input("Enter a word to encrypt the alphabet by: ")
            matrix_1.alphabet_encryption(inp)

        elif sel == "e":
            stri = input("Enter a string to encrypt: ")
            print(f"Your encrypted string is: {encrypt_str(stri, matrix_1)}")

        elif sel == "d":
            strin = input("Enter a string to decrypt: ")
            print(f"Your decrypted string is: {decrypt_str(strin, matrix_1)}")

        elif sel == "q":
            break

        else:
            continue


if __name__ == '__main__':
    main()