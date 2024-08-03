"""
_0178_stump

#ml

"""

def main():

    # N = int(input())
    # points = [list(map(int, input().split())) for _ in range(N)]

    N = 4
    points = [
        [0,1],
        [1,1],
        [2,0],
        [3,0]
    ]

    N = 8
    points = [
        [4,0],
        [5,0],
        [0,1],
        [1,1],
        [2,1],
        [3,1],
        [6,0],
        [7,0]
    ]

    # N = 1
    # points = [
    #     [6,3],
    # ]

    # N = 5
    # points = [
    #     [0,1],
    #     [1,1],
    #     [2,0.5],
    #     [3,0],
    #     [4,0],
    # ]

    a,b,c = solver(N, points)
    print(f"{a:.6f} {b:.6f} {c:.6f}")

def solver(N, points):

    points.sort()

    saved_mean_1 = 0
    saved_mean_2 = 0
    saved_split = None
    tresh = 0

    min_err = float('inf')

    for i in range(1, N):

        mean_1, var_1, frac_1 = mean_var(points, 0, i)
        mean_2, var_2, frac_2 = mean_var(points, i, N)

        err = frac_1 * var_1 + frac_2 * var_2 # where is it come from? cs4780?

        # print(mean_1, var_1, frac_1)
        # print(mean_2, var_2, frac_2)
        # print(err)
        
        if err < min_err:
            min_err = err
            saved_mean_1 = mean_1
            saved_mean_2 = mean_2
            saved_split = i

    if saved_split:
        if N % 2 == 0:
            tresh = (points[saved_split-1][0] + points[saved_split][0]) / 2
        else:
            tresh = points[saved_split][0]
    else:
        if len(points) == 1:
            saved_mean_1 = points[0][1]
            saved_mean_2 = points[0][1]
            tresh = points[0][0]

    return saved_mean_1, saved_mean_2, tresh

def mean_var(points, low, high):

    mean = 0
    for i in range(low, high):
        mean += points[i][1]
    mean /= (high-low)

    var = 0
    for i in range(low, high):
        var += (points[i][1] - mean)**2
    var /= (high-low)

    return mean, var, (high-low)/len(points)

if __name__ == '__main__':
    main()