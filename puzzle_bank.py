a_level = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8']
b_level = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8']
c_level = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8']
d_level = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8']
e_level = ['e1']

bt_safe_boards = a_level + b_level
fc_safe_boards = a_level + b_level + c_level + d_level + e_level
gac_safe_boards = a_level + b_level + c_level + d_level + e_level

board_db = {
    'a1': [
        [13, None, None, 17, 18, 20],
        [14, 15, None, 25, None, 19],
        [None, 8, 10, 26, 24, None],
        [7, 5, None, None, 36, 23],
        [4, 1, None, 35, 31, 33],
        [None, 3, 29, 30, None, None],
    ],
    'a2': [
        [32, 33, None, 29, 1, None],
        [34, None, 30, 27, None, 2],
        [None, 36, 26, 13, 11, 5],
        [None, 25, 14, None, 10, 6],
        [24, 22, 18, None, None, 7],
        [None, 20, None, None, 16, 8],
    ],
    'a3': [
        [6, 8, 4, 1, 2, 35],
        [None, 5, 9, 3, 36, 34],
        [13, 12, None, 10, 23, None],
        [14, None, 16, 22, 32, 24],
        [None, None, 21, None, 26, None],
        [18, None, None, None, None, 27],
    ],
    'a4': [
        [None, 25, 12, 11, None, 8],
        [26, 23, 5, None, 7, 9],
        [None, 4, None, None, 14, None],
        [3, 28, None, None, 17, 15],
        [2, None, 19, 20, 36, 34],
        [1, 30, None, None, 33, 35],
    ],
    'a5': [
        [35, 33, None, 31, None, None],
        [36, None, None, 5, 9, 8],
        [28, 29, 1, None, None, 12],
        [27, 26, 3, 2, None, 13],
        [None, 21, None, 18, 16, 14],
        [None, 23, 20, 19, 17, None],
    ],
    'a6': [
        [17, 16, None, 1, 13, None],
        [20, 18, None, None, 2, 11],
        [19, None, None, 23, 10, None],
        [32, 33, 26, 25, 4, 9],
        [31, 27, None, 36, None, 5],
        [None, None, None, 35, 7, 6],
    ],
    'a7': [
        [19, 18, None, 16, 11, 10],
        [24, 20, 15, None, 9, 12],
        [None, 25, None, 8, None, 34],
        [None, 22, 7, 36, None, 33],
        [27, 6, None, 4, None, None],
        [28, None, 5, 31, None, 1],
    ],
    'a8': [
        [3, 2, 1, None, None, 32],
        [None, 5, None, 9, 33, 31],
        [None, None, None, 28, 30, None],
        [12, 14, None, 26, 29, 35],
        [None, 18, 20, 22, None, 36],
        [16, 17, None, 21, 23, 24],
    ],
    'b1': [
        [18, None, 12, 13, 35, 36],
        [None, 21, None, None, None, 34],
        [None, 26, 22, 15, None, None],
        [25, 23, None, 9, 32, None],
        [None, 5, 8, None, 2, 30],
        [6, None, None, 3, None, 1],
    ],
    'b2': [
        [None, None, 30, None, 27, None],
        [None, 31, 36, 29, 26, 24],
        [12, 32, None, 9, None, None],
        [None, None, 19, None, 8, 22],
        [14, 17, 18, 3, 4, None],
        [15, None, 1, None, 6, None],
    ],
    'b3': [
        [3, None, 1, 9, None, 11],
        [6, None, None, None, 10, 13],
        [None, None, 18, 34, None, None],
        [None, 27, 33, 19, 35, None],
        [29, 32, 26, None, 23, 36],
        [31, None, 25, None, None, 22],
    ],
    'b4': [
        [None, 32, 31, None, 29, 26],
        [33, 35, None, 30, None, 25],
        [1, 8, 36, None, None, 24],
        [None, 7, 21, 22, None, 13],
        [None, 6, None, 18, None, 14],
        [5, None, None, None, 16, None],
    ],
    'b5': [
        [5, None, None, 1, None, 13],
        [4, 3, 2, None, 12, None],
        [31, None, 9, None, 11, None],
        [None, 30, 25, 10, 23, None],
        [34, 29, 26, None, 19, None],
        [36, None, None, 27, None, 20],
    ],
    'b6': [
        [None, 5, None, None, 30, 28],
        [1, 3, 8, 31, None, 29],
        [2, 9, None, 26, None, None],
        [None, None, 25, 36, 35, 34],
        [None, None, 22, 21, None, 18],
        [None, 13, None, 16, 17, None],
    ],
    'b7': [
        [2, 1, 24, None, 26, 36],
        [None, 3, 23, 27, 35, None],
        [None, None, None, None, 32, 34],
        [21, None, 30, 29, 13, None],
        [None, None, 17, None, 15, None],
        [None, None, None, None, None, None],
    ],
    'b8': [
        [27, None, 29, 31, 32, 36],
        [25, 26, None, 33, None, 35],
        [None, 23, None, None, 5, None],
        [22, None, 1, 3, None, 6],
        [None, 21, 16, 9, None, None],
        [18, None, None, None, 10, 12],
    ],
    'c1': [
        [33, 32, None, 30, 29, 1],
        [35, None, None, 28, 17, 2],
        [36, None, 20, 18, None, None],
        [None, None, 19, 15, None, None],
        [None, 22, 10, None, None, None],
        [23, 9, None, None, None, None]
    ],
    'c2': [
        [16, 17, None, None, None, 22],
        [None, 14, None, 31, 21, None],
        [8, None, 32, 12, None, 24],
        [None, 9, None, 33, None, 25],
        [4, None, None, None, None, 28],
        [3, None, 1, 36, None, None]
    ],
    'c3': [
        [None, None, 22, 20, 19, 18],
        [None, 36, None, None, 15, None],
        [None, None, 30, None, 14, None],
        [None, 28, None, 33, None, 12],
        [3, 1, 6, None, 9, 11],
        [None, 4, None, 7, None, None]
    ],
    'c4': [
        [21, None, None, None, None, None],
        [22, None, 35, None, 14, 16],
        [26, 24, 36, 31, None, 13],
        [None, None, None, 30, 32, None],
        [None, 1, 28, 7, 9, None],
        [2, None, None, None, None, 10]
    ],
    'c5': [
        [None, 29, 30, None, 32, 4],
        [28, 26, 1, None, 3, None],
        [25, 23, None, None, None, 8],
        [None, None, 22, 14, None, 7],
        [36, None, 15, None, None, None],
        [None, 16, None, None, None, 11]
    ],
    'c6': [
        [30, 28, None, 36, 1, 3],
        [31, None, None, 26, None, 2],
        [32, None, None, None, None, 5],
        [33, None, 14, 24, None, None],
        [None, 15, None, None, 8, None],
        [None, 17, 21, None, 10, None]
    ],
    'c7': [
        [None, None, None, 12, None, None],
        [31, 27, 11, None, 9, 15],
        [32, None, None, 8, None, 17],
        [None, 25, None, 6, 5, None],
        [34, None, None, None, 19, 20],
        [1, None, 36, None, 22, None]
    ],
    'c8': [
        [22, None, 25, None, 35, None],
        [20, 21, None, None, None, 36],
        [19, None, None, 7, None, None],
        [None, 18, None, None, 31, 5],
        [None, 14, 10, 9, None, 4],
        [13, None, 11, 1, None, None]
    ],
    'd1': [
        [None, None, 28, None, 25, 23],
        [None, None, None, None, None, None],
        [None, None, 32, None, None, 1],
        [None, 9, None, None, None, None],
        [None, 11, None, None, 18, None],
        [36, None, None, 13, None, 17],
    ],
    'd2': [
        [None, None, 2, None, None, 30],
        [36, None, None, 1, None, None],
        [5, None, 25, None, 23, None],
        [None, 8, None, None, None, 21],
        [None, 12, None, 19, None, 17],
        [None, None, None, None, 18, None],
    ],
    'd3': [
        [None, None, None, 1, None, None],
        [5, 6, None, None, None, 24],
        [None, None, None, None, 31, None],
        [None, None, None, 30, 20, None],
        [9, None, 13, None, None, None],
        [None, None, None, None, 17, 36],
    ],
    'd4': [
        [None, 13, None, None, None, None],
        [None, None, None, 31, None, 36],
        [11, None, None, None, None, 35],
        [None, 9, None, None, None, 26],
        [5, None, None, None, None, 21],
        [None, None, 3, 1, None, None],
    ],
    'd5': [
        [None, None, None, None, 14, None],
        [None, 26, 25, 18, None, 12],
        [None, None, 36, 17, None, None],
        [None, 34, None, None, None, 8],
        [None, None, None, 1, None, 9],
        [None, None, 32, None, None, None],
    ],
    'd6': [
        [None, 3, None, None, 34, None],
        [None, None, None, None, None, None],
        [10, None, None, 1, 36, None],
        [None, None, 19, None, 24, None],
        [17, None, None, None, None, None],
        [None, None, None, None, None, None],
    ],
    'd7': [
        [None, None, 15, None, 17, None],
        [None, 9, None, None, 35, None],
        [None, 8, None, 28, None, 36],
        [None, None, None, None, None, None],
        [6, None, None, None, None, 26],
        [4, 3, None, 1, None, None],
    ],
    'd8': [
        [None, None, None, None, None, 1],
        [30, None, 36, 27, None, 24],
        [None, None, None, 17, None, None],
        [None, None, 14, None, None, None],
        [None, None, 9, None, 21, None],
        [12, None, None, None, None, None],
    ],
    'e1': [
        [None, None, None, None, None, None, 47],
        [None, None, 29, 35, 31, None, 49],
        [23, None, 25, None, None, 44, None],
        [None, None, None, None, None, None, None],
        [None, None, 4, None, None, 39, 40],
        [None, None, 2, 1, None, None, 16],
        [None, None, None, None, None, 17, None],
    ]
}
