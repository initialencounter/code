from typing import  List
# case1 = [[1, 0, 1, 0, 0],
#          [1, 0, 1, 1, 1],
#          [1, 1, 1, 1, 1],
#          [1, 0, 0, 1, 0]]
# case1 = [[1, 1, 1, 1, 1],
#          [1, 1, 1, 1, 1],
#          [1, 1, 1, 1, 1],
#          [1, 1, 1, 1, 1]]
def longest_chain(lst: List[int]) -> int:
    """
    Your longest_chain function from last week, make sure this works properly
    before proceeding with the rest of the lab!
    """
    i = 0
    length = 0
    while i < len(lst):
        if lst[i] == 1:
            length += 1
        elif lst[i] == 0:
            return length
        i += 1
    return length

def largest_at_position(matrix: List[List[int]], row: int, col: int) -> int:
    """
    Returns the area of the largest rectangle whose top left corner is at
    position <row>, <col> in <matrix>.

    You MUST make use of the helper <longest_chain> here as you loop through
    each row of the matrix. Do not modify (i.e., mutate) the input matrix.

    # >>> case1 = [[1, 0, 1, 0, 0],
    # ...          [1, 0, 1, 1, 1],
    # ...          [1, 1, 1, 1, 1],
    # ...          [1, 0, 0, 1, 0]]
    # >>> largest_at_position(case1, 0, 0)
    # 4
    # >>> largest_at_position(case1, 2, 0)
    # 5
    # >>> largest_at_position(case1, 1, 2)
    # 6
    """
    area=0
    minx =longest_chain(matrix[row][col:])
    y=1
    if minx==0:
        return 0
    for i in matrix[row:]:
        x = longest_chain(i[col:])
        if x<=minx:
            minx=x
        else:
            x=minx
        if x*y>area:
            area = x*y
        y+=1
    return area

# print(largest_at_position(case1,0,0))

def largest_in_matrix(matrix: List[List[int]]) -> int:
    """
    Returns the area of the largest rectangle in <matrix>.

    The area of a rectangle is defined by number of 1's that it contains.

    Again, you MUST make use of the helper <largest_at_position> here. If you
    managed to code <largest_at_position> correctly, this function should be
    simple to implement.

    Similarly, do not modify (i.e., mutate) the input matrix.

    Precondition:
        <matrix> will only contain the integers 1 and 0.

    # >>> case1 = [[1, 0, 1, 0, 0],
    # ...          [1, 0, 1, 1, 1],
    # ...          [1, 1, 1, 1, 1],
    # ...          [1, 0, 0, 1, 0]]
    # >>> largest_in_matrix(case1)
    6
    """
    area = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]==1:
                minx = longest_chain(matrix[row][col:])
                y = 1
                for i in matrix[row:]:
                    x = longest_chain(i[col:])
                    if x <= minx:
                        minx = x
                    else:
                        x = minx
                    if x * y > area:
                        area = x * y
                    y += 1
    return area

# print(largest_in_matrix(case1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

