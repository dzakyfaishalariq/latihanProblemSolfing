def collinearity(x1, y1, x2, y2):
    '''
        (0,0), (x1,y1), (x2,y2)
        det(a) = [
            [0,  0,  1],
            [x1, y1, 1],
            [x2, y2, 1]
        ]
         = 0
    '''
    return (1*y2*x1) - (1*y1*x2) == 0
    
print(collinearity(1,2,1,-2))