# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jay Ahlschwede
#               Aidan Murphy
#               Israel Prado
#               Bobby Hao
# Section:      525
# Assignment:   9.15.1: LAB: Shoelace formula
# Date:         26 10 2022
#
#
# YOUR CODE HERE
def getpoints(verts):
    '''This functions takes in the vertices coordinates 
    and splits them into a list of length that is readable for the 
    next function'''
    plength=[]
    for x in verts.split(' '):
        tlist=x.split(',')
        tlist=[int(i) for i in tlist]
        plength.append(tlist)
    return plength

def cross(p1, p2):
    ''''This function takes the cross product
    of two vertices as outlined in the equation this 
    program is based on, and then returns the cross product for 
    each appropriate operation'''
    cp=(p1[0]*p2[1])-(p1[1]*p2[0])
    return cp

def shoelace(ps):
    '''This function calculates the overall area by taking
    information from the cross product and position of the points and
    goes through each point or vertice to do so.'''
    ps.append(ps[0])
    parea=0
    for i in range(len(ps)-1):
        parea+=cross(ps[i],ps[i+1])
    return parea/2

def main():
    ''''This is the main function, which gathers the user input
    and houses the print statement which is a compilation of the other
    functions'''
    verts=input('Please enter the vertices: ')
    print(f'The area of the polygon is',shoelace(getpoints(verts)))
    
if __name__=='__main__':
    main()
    