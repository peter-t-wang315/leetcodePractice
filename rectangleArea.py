# __Big O time__
# The big O time complexity of this algorithm is O(1). This is because no matter the sizes of any of the inputs, it will take a constant time to compute everything as 
# there is no iteration over any of the inputs.

# __Space complexity__
# The space complexity of this algorithm is O(1). This is because no matter the inputs, there is always only a constant number of data variables being made.

def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    x_len=0
    y_len=0
    # --This section accounts for overlap--
    # Determining length of x side
    if ax1<=bx1<ax2:
        x_len=min(bx2,ax2)-bx1
    elif ax1<bx2<=ax2:
        x_len=bx2-max(ax1, bx1)
    elif bx1<=ax1<bx2:
        x_len=min(bx2,ax2)-ax1
    elif bx1<ax2<=bx2:
        x_len=ax2-max(ax1, bx1)
    # Determining height of y side
    if ay1<=by1<ay2:
        y_len=min(by2,ay2)-by1
    elif ay1<by2<=ay2:
        y_len=by2-max(ay1, by1)
    elif by1<=ay1<by2:
        y_len=min(by2,ay2)-ay1
    elif by1<ay2<=by2:
        y_len=ay2-max(ay1, by1)
    # -------------------------------------
    overlap_area = x_len*y_len
    
    square_a=(ax2-ax1)*(ay2-ay1)
    square_b=(bx2-bx1)*(by2-by1)
    
    return square_a+square_b-overlap_area



if __name__ == "__main__":
    ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = map(int, input().split())
    
    print(computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))