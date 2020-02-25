
global N
N = 4

def printSolution(sol):

    for i in range(N):
        for j in range(N):
            print(sol[i][j],end = ' ')
        print()

def issafe(maze,x,y):

    if x < N and y < N and x >= 0 and y >= 0 and maze[x][y] == 1:
        return True

    return False

def solveutil(maze,x,y,sol):

    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True

    if issafe(maze,x,y):

        sol[x][y] = 1

        if solveutil(maze,x+1,y,sol) is True:
            return True

        if solveutil(maze,x,y+1,sol) is True:
            return True

        sol[x][y] = 0


def sove(maze):

    sol = [[0 for j in range(N)] for i in range(N)]

    if solveutil(maze,0,0,sol) is False:
        print('No solution')
        return False
    printSolution(sol)
    return True


if __name__ == '__main__':

    maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]

    sove(maze)
