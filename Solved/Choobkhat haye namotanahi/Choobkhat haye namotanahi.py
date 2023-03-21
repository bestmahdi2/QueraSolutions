import math
board = [0,0]
earaser = [0,0]
board[0] = int(input())
board[1] = int(input())
earaser[0] = int(input())
earaser[1] = int(input())
print(math.ceil(min(board)/max(earaser)))