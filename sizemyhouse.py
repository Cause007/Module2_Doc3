def areaOfHouse(*length):
    '''
        areaOfHouse(*length)
        Input the length, in feet, of each side of the house. 
        For a more complex house, divide the house into rectangular sections and INPUT length and width 
        of each section (input in pairs of two).
        -------------------------
        For example: 
        for a rectangular house with smaller out-juts, input: 
        areaOfHouse(lengthOfSection1,widthOfSection1,lengthOfSection2,widthOfSection2, ...and so on).
        areaOfHouse(5,10,4,5,2,3) will return 5x10 + 4x5 + 2x3 = 76 square feet
    '''
    area = 0
    for num in range(1,len(length),2):
        area += length[num] * length[num-1]
    return f"The area of your house is {area} square feet."

def circumference(radius):
    ''' 
        circumference(radius)
        input radius and the function will return the circumference
    '''
    pi = 3.14159
    circ = round(2*pi*radius,3)
    return f'The circumference of a circle with a radius of {radius} is {circ}.'
    
print(areaOfHouse(5,10,5,9,20,2))
print(circumference(3))
