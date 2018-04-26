
# Variables
center_x=50
center_y=50
diameter=10

# Function with parameters
def draw_bubbles(cx, cy, d):
    # _x, _y, _d are the parameters of this function
    ellipse(cx,cy,d,d)
    ellipse(cx+d,cy,d,d)
    ellipse(cx+d*2,cy,d,d)
    
draw_bubbles(center_x-diameter,center_y-diameter,diameter)
draw_bubbles(center_x-diameter,center_y,diameter)
draw_bubbles(center_x-diameter,center_y+diameter,diameter)
