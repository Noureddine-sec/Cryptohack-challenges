

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
  
    b=[]
    for i in range (len(s)):
        b.append([])
    for i in range (len(s)):
        for j in range (len (s)):
            print (i,j)
            b[i].append(s[i][j]^k[i][j])
    return b




print(add_round_key(state, round_key))

