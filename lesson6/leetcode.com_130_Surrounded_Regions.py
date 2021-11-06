# board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        substitutes = 1
        if m >= 3 and n >= 3:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == "O" and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                        board[i][j] = "R"  # заменяем все граничные О на R

            while substitutes:
                substitutes = 0  # Счетчик замен
                for i in range(1, m - 1):
                    for j in range(1, n - 1):
                        # если у О есть сосед R то заменим О на R
                        if board[i][j] == "O" and (board[i - 1][j] == "R" or
                                                   board[i][j + 1] == "R" or
                                                   board[i + 1][j] == "R" or
                                                   board[i][j - 1] == "R"):
                            board[i][j] = "R"
                            substitutes += 1

            for i in range(m):
                for j in range(n):
                    if board[i][j] == "O":
                        board[i][j] = "X"
                    elif board[i][j] == "R":
                        board[i][j] = "O"

# затраченное время: сутки (естественно с перерывами) на поиск идеи, 30 минут на реализацию
