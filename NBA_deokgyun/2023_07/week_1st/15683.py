# [BOJ] 15683. 감시
# 소요 시간 : 00분

class Cameras:
    board = []
    backup_board = []
    deadzone = 0
    row = 0
    col = 0
    min_deadzone = 10000
    cam_cnt = 0
    rotate_list = []
    camera_list = []
    cam_dir = [
        [],
        [[(0,1)], [(1,0)],[(0,-1)],[(-1,0)]],
        [[(1,0),(-1,0)], [(0,-1),(0,1)], [(1,0),(-1,0)], [(0,-1),(0,1)]],
        [[(-1,0),(0,1)],[(-1,0),(0,-1)],[(1,0),(0,-1)],[(1,0),(0,1)]],
        [[(-1,0), (0,-1), (0,1)], [(-1,0), (0,-1),(1,0)], [(1,0), (0,-1), (0,1)], [(-1,0), (0,1),(1,0)]],
        [[(-1,0), (0,-1), (0,1), (1,0)]]
    ]
    def __init__(self, board, row, col, deadzone, camera_list) -> None:
        self.cam_cnt = len(camera_list)
        self.camera_list = camera_list
        self.board = [[0 for _ in range(col)] for _ in range(row)]
        self.backup_board = [[0 for _ in range(col)] for _ in range(row)]
        self.row = row
        self.col = col
        for i in range(row):
            for j in range(col):
                self.board[i][j] = board[i][j]
                self.backup_board[i][j] = board[i][j]
        self.deadzone = deadzone

    def cam(self,num,i,j,dir) -> None:
        board = self.board
        row = self.row
        col = self.col
        for di, dj in self.cam_dir[num][dir]:
            ni = i + di
            nj = j + dj
            while 0 <= ni < row and 0 <= nj < col:
                if board[ni][nj] == 0:
                    board[ni][nj] = -1
                    self.deadzone -= 1
                elif board[ni][nj] >= 1:
                    break
        
    def reset(self):
        self.board = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                self.board[i][j] = self.backup_board[i][j]
        if self.min_deadzone > self.deadzone:
            self.min_deadzone = self.deadzone
        self.deadzone = 0

    def rotate(self):
        for i in range(3):
            self.rotate_list.append(i)
            self.rotate

row, col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(row)]

camera_list = []

deadzone = row * col

for i in range(row):
    for j in range(col):
        if board[i][j] > 0:
            camera_list.append((i, j, board[i][j]))
            deadzone -= 1

cameras = Cameras(board, row, col, deadzone, camera_list)
