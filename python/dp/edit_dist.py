"""
[dp] edit_dist
Levenshtein distance implementation
"""

PATH_INVLID = -1
PATH_MATCH = 0
PATH_INSERT = 1
PATH_DELETE = 2  

def edit_dist(p: str, t: str, verbose=False) -> int:
    """
    Calculates edit distance between two strings

    Args:
        p (str): Pattern string (Search string)
        t (str): Target string
    """

    if len(p) == 0:
        return len(t)

    if len(t) == 0:
        return len(p)

    dp_matrix = [[0] * (len(t)+1) for _ in range(len(p) + 1)]
    path_matrix = [[PATH_INVLID] * (len(t)+1) for _ in range(len(p) + 1)]

    # init first column
    for i in range(len(p)+1):
        dp_matrix[i][0] = i
        path_matrix[i][0] = PATH_DELETE

    # init first row
    for j in range(len(t)+1):
        dp_matrix[0][j] = j
        path_matrix[0][j] = PATH_INSERT

    path_matrix[0][0] = PATH_INVLID

    # Индексы в матрице и строках сдвинуты на 1
    for i in range(1, len(p)+1):
        for j in range(1, len(t)+1):
            match = dp_matrix[i-1][j-1] + match_cost(p[i-1], t[j-1])
            insert = dp_matrix[i][j-1] + 1 # слева: продвинулись в таргете, но остались на месте в паттерне -> вставка в паттерн
            delete = dp_matrix[i-1][j] + 1 # сверху: продвинулись в паттерне, но остались на месте в таргете -> удаление из паттерна

            # dp_matrix[i][j] = min(match, delete, insert)

            ops = [-1] * 3
            ops[PATH_MATCH] = match
            ops[PATH_INSERT] = insert
            ops[PATH_DELETE] = delete

            min_op = PATH_MATCH
            for op in [PATH_INSERT, PATH_DELETE]:
                if ops[op] < ops[min_op]:
                    min_op = op

            dp_matrix[i][j] = ops[min_op]
            path_matrix[i][j] = min_op
    
    if verbose:
        print_cost_matrix(dp_matrix)
        print()
        print_cost_matrix(path_matrix)
        print()
        reconstruct_path(p, t, path_matrix, len(p), len(t))

    return dp_matrix[-1][-1]

def reconstruct_path(p: str, t: str, path_matrix: list[list[int]], i: int, j: int) -> None:
    if path_matrix[i][j] == -1:
        return

    if path_matrix[i][j] == PATH_MATCH:
        reconstruct_path(p, t, path_matrix, i-1, j-1)
        handle_match(p[i-1], t[j-1])
        return

    if path_matrix[i][j] == PATH_INSERT:
        reconstruct_path(p, t, path_matrix, i, j-1)
        handle_insert(p[i-1], t[j-1])
        return

    if path_matrix[i][j] == PATH_DELETE:
        reconstruct_path(p, t, path_matrix, i-1, j)
        handle_delete(p[i-1], t[j-1])
        return
        
def handle_match(a: str, b: str):
    if a == b:
        print(f"M: {a}")
    else:
        print(f"S: {a}->{b}")

def handle_insert(a: str, b: str):
    print(f"I: {b}")

def handle_delete(a: str, b: str):
    print(f"D: {a}")

def match_cost(a: str, b: str) -> int:
    if a == b:
        return 0
    return 1

def print_cost_matrix(matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
        print("[", end="")
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:3d}", end="")
        print("]")

def run_tests():

    dist = edit_dist("thou", "you")
    assert(dist==2)

    dist = edit_dist("bcdef", "obndef")
    assert(dist==2)

    dist = edit_dist("sdfbsdfcdf", "abc")
    assert(dist==8)

    print("tests passed!")


if __name__ == '__main__':  

    dist = edit_dist("bcdef", "obndef", verbose=True)
    print(dist)

    run_tests()
