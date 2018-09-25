import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules

myWin = visual.Window(color='white', units='pix', size=[1920,1080], allowGUI=False, fullscr=False) # creates a window
myClock = core.Clock() #this creates and starts a clock which we can later read

diskLeft = visual.Circle(myWin, radius=40, pos=[-180,0], lineWidth=2.5, fillColor='orange', lineColor=None)
diskRight = visual.Circle(myWin, radius=40, pos=[180,0], lineWidth=2.5, fillColor='orange', lineColor=None)
myCircleLeft =visual.Circle(myWin, radius=80, lineWidth=2.5, fillColor=[-1, -1, -1], lineColor='black')
myCircleRight =visual.Circle(myWin, radius=80, lineWidth=2.5, fillColor=[-1, -1, -1], lineColor='black')
myScale = visual.RatingScale(myWin, pos=[0, -360], low=20, high=60,  textSize=0.5, lineColor='black',  tickHeight=False, scale=None, showAccept=False, singleClick=True)
information=visual.TextStim(myWin, pos=[0,-385], text='', height=18, color='blue') 
informationscale1=visual.TextStim(myWin, pos=[-150,-410], text='-25%', height=15, color='black') 
informationscale2=visual.TextStim(myWin, pos=[0,-410], text='0%', height=15, color='black') 
informationscale3=visual.TextStim(myWin, pos=[150,-410], text='+25%', height=15, color='black') 

 # draw circles with radius 'radius' around a ring with radius 'distance'
def ringOfCirclesLeft(centrex, centrey, radius, distance):

    myCircleLeft.setRadius(radius)
    for angle in [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]:
        angle = math.radians(angle)
        x = math.cos(angle) * distance
        y = math.sin(angle) * distance
        myCircleLeft.setPos([centrex+x, centrey+y])
        myCircleLeft.draw()
        

def ringOfCirclesRight(centrex, centrey, radius, distance):

    myCircleRight.setRadius(radius)
    for angle in [0, 60, 120, 180, 240, 300, 360]:
        angle = math.radians(angle)
        x = math.cos(angle) * distance
        y = math.sin(angle) * distance
        myCircleRight.setPos([centrex+x, centrey+y])
        myCircleRight.draw()

# the main loop
def mainLoop(): 
    
    finished = False
    standardRadius = 40.
    diskLeft.setRadius(standardRadius)
    diskRight.setRadius(standardRadius)
    
    while not finished:
    
        diskLeft.draw()
        diskRight.draw()
    
        ringOfCirclesLeft(centrex=-180, centrey=0, radius= 10, distance= 55)
        ringOfCirclesRight(centrex= 180, centrey=0, radius= 70, distance= 150)
        
        myScale.draw()
        information.draw()
        informationscale1.draw()
        informationscale2.draw()
        informationscale3.draw()
        myWin.flip()
        
        if myScale.noResponse ==False: #some new value has been selected with the mouse
            size = myScale.getRating()
            percentage = (size-40) / 40. * 100
            information.setText(str(percentage) + "%")
            diskRight.setRadius(size)
            myScale.reset()
    
        pressedList =event.getKeys(keyList=['escape']) #pressing ESC quits the program
        if len(pressedList) >0:
            if pressedList[0] =='escape':
                finished =True
            event.clearEvents()

mainLoop() #enters the main loop
myWin.close() #closes the window
core.quit() #quits




