"""
[dp] edit_dist
Levenshtein distance implementation
"""


def edit_dist(p: str, t: str) -> int:
    """
    Calculates edit distance betweeb two strings

    Args:
        p (str): Pattern string. (Search string)
        t (str): Target string
    """

    if len(p) == 0:
        return len(t)

    if len(t) == 0:
        return len(p)

    dp_matrix = [[0] * (len(t)+1) for _ in range(len(p) + 1)]

    # init first column
    for i in range(len(p)+1):
        dp_matrix[i][0] = i

    # init first row
    for j in range(len(t)+1):
        dp_matrix[0][j] = j

    # Индексы в матрице и строках сдвинуты на 1
    # i, j в строках p и t соответсвует i+1, j+1 в матрице dp_matrix
    for i in range(len(p)):
        for j in range(len(t)):
            match = dp_matrix[i][j] + match_cost(p[i], t[j])
            insert = dp_matrix[i+1][j] + 1 # слева: продвинулись в таргете, но остались на месте в паттерне -> вставка в паттерн
            delete = dp_matrix[i][j+1] + 1 # сверху: продвинулись в паттерне, но остались на месте в таргете -> удаление из паттерна

            dp_matrix[i+1][j+1] = min(match, delete, insert)
    
    print_cost_matrix(dp_matrix)

    return dp_matrix[-1][-1]

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


if __name__ == '__main__':

    dist = edit_dist("thou", "you")
    print(dist)