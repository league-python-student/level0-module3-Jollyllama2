

def setup():
    # Set the size of your sketch
    size(500,500)
    
    pass
    
def draw():
    s= 250
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range (4):
        if i % 2 == 0:
            fill('#1C34FF')
            
        else:
            fill('#23CBAB')
            
        ellipse(250,250,s,s)
    
        s-=50
    
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass
