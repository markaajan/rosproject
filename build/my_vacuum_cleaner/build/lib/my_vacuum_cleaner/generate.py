import math as math

width = 0.27

def genpoints (a,b,c,d): #Send points ,x1,y1,x2,y2

    points = []
    if a > c:
        y = a
        a = c
        c = y
        y = b
        b = d
        d = y
        # This is to flip the coordinated for ease of handling


    n = math.floor((c - a) / width)
    flag = False
    for i in range(n):
        for j in range(i+1):
            if flag:
                points.append(((a + (width * j)),(b + (width * (i - j)))))
            else:
                points.append(((a + (width * (i-j))), (b + (width *  j))))
        flag = not flag


    print (points)

genpoints(-6.9064,0.58458,-5.16437,-3.65905)