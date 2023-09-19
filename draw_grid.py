"""Lab1-C-1
Write a function draw_grid(m=2, n=3) 
that draws a similar grid with m rows and n columns.
"""

def draw_grid(m=2, n=3):

    print("+",end='')
    for i in range(n):
        print(" - - +",end='')

    for i in range(m):
        print("\n/",end='')
        for i in range(n):
            print("     /",end='')

        print("\n/",end='')
        for i in range(n):
            print("     /",end='')

        print("\n+",end='')
        for i in range(n):
            print(" - - +",end='')

if __name__ == '__main__':
    draw_grid(m=2, n=3)