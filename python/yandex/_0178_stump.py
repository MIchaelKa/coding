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

    a,b,c = solver(N, points)
    print(f"{a:.6f} {b:.6f} {c:.6f}")

def solver(N, points):

    saved_mean_1 = None
    saved_mean_2 = None
    saved_split = None

    min_err = None

    for i in range(1, N):

        mean_1, var_1, frac_1 = mean_var(points, 0, i)
        mean_2, var_2, frac_2 = mean_var(points, i, N)

        err = frac_1*var_1 + frac_2*var_2

        # print(mean_1, var_1, frac_1)
        # print(mean_2, var_2, frac_2)
        # print(err)
        
        if min_err is None or err < min_err:
            min_err = err
            saved_mean_1 = mean_1
            saved_mean_2 = mean_2
            saved_split = i

    tresh = (points[saved_split-1][0] + points[saved_split][0]) / 2

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



