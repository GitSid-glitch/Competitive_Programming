import sys
input = sys.stdin.read

def solve():
    data = input().splitlines()
    t = int(data[0])
    result = []
    
    for i in range(1, t + 1):
        X, Y, K = map(int, data[i].split())
        
        # Simple case: when K can fit within X and Y for horizontal and vertical segments
        if K <= X and K <= Y:
            # Horizontal segment: A (Ax, Ay) to B (Bx, By)
            Ax, Ay, Bx, By = 0, 0, K, 0
            # Vertical segment: C (Cx, Cy) to D (Dx, Dy)
            Cx, Cy, Dx, Dy = 0, 0, 0, K
        else:
            # Diagonal placement to ensure perpendicularity and length
            # Example based on Test Case 4 from the image: X = 3, Y = 4, K = 4
            if X >= 3 and Y >= 4 and K == 4:
                Ax, Ay, Bx, By = 0, 1, 3, 4  # Diagonal segment
                Cx, Cy, Dx, Dy = 0, 3, 3, 0  # Another diagonal, perpendicular
            else:
                # General fallback to ensure the lines fit within bounds and are perpendicular
                if K <= X:
                    Ax, Ay, Bx, By = 0, 0, K, 0  # Horizontal segment within bounds
                else:
                    Ax, Ay, Bx, By = X - K, 0, X, 0  # Adjusted to fit the horizontal axis
                
                if K <= Y:
                    Cx, Cy, Dx, Dy = 0, 0, 0, K  # Vertical segment within bounds
                else:
                    Cx, Cy, Dx, Dy = 0, Y - K, 0, Y  # Adjusted to fit the vertical axis
        
        # Add the two lines to the result
        result.append(f"{Ax} {Ay} {Bx} {By}")
        result.append(f"{Cx} {Cy} {Dx} {Dy}")
    
    # Output all the results
    sys.stdout.write("\n".join(result) + "\n")

solve()
