
# Variables
center_x=50
center_y=50
diameter=10

# Functions packs instructions together
def draw_bubble():
    global center_x
    global center_y
    global diameter
    ellipse(center_x,center_y,diameter,diameter)
    # Shortcut for increment
    # It is the same as diameter=diameter+2
    diameter+=2
    center_x+=diameter
    
draw_bubble()
draw_bubble()
draw_bubble()