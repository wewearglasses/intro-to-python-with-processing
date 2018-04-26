
# Variables
center_x=50
center_y=50
diameter=10

# Functions packs instructions together
def draw_bubbles():
    # _x, _y, _d are the parameters of this function
    ellipse(center_x,center_y,diameter, diameter)
    ellipse(center_x+diameter,center_y,diameter, diameter)
    ellipse(center_x+diameter*2,center_y,diameter, diameter)
    
draw_bubbles()
center_y+=diameter
draw_bubbles()
center_y+=diameter
draw_bubbles()