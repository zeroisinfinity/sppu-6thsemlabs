n = int(input("enter: ").strip())
board = [['.' for i in range(n)] for j in range(n)]
cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

def solve(row):

    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end="     ")
            print('\n')
            
        return True

    for col in range(n):
        d1 = row - col + n - 1
        d2 = row + col 

        if cols[col] or diag1[d1] or diag2[d2]:
            continue
        
        board[row][col] = 'Q'
        cols[col] = True
        diag1[d1] = True
        diag2[d2] = True

        if solve(row+1):
            return True
        
        board[row][col] = '.'
        cols[col] = False
        diag1[d1] = False
        diag2[d2] = False

    return False


solve(0)
        

