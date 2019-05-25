import bge
from bge import render as r

def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    perc = 3
    
    cY = r.getWindowHeight()//2
    cX = r.getWindowWidth()//2

    sens = cont.sensors['Mouse']
    actuXR = cont.actuators['Motion.XR']
    actuXL = cont.actuators['Motion.XL']
    actuYR = cont.actuators['Motion.YR']
    actuYL = cont.actuators['Motion.YL']
    
    if own["propX"] < sens.position[0]+perc:
        cont.activate(actuXR)
    else:
        cont.deactivate(actuXR)
        
    if own["propX"] > sens.position[0]-perc:
        cont.activate(actuXL)
    else:
        cont.deactivate(actuXL)
        
    if own["propY"] < sens.position[1]+perc:
        cont.activate(actuYR)
    else:
        cont.deactivate(actuYR)
        
    if own["propY"] > sens.position[1]-perc:
        cont.activate(actuYL)
    else:
        cont.deactivate(actuYL)
        
    own["propX"] = sens.position[0]
    own["propY"] = sens.position[1]
    
    if sens.position[0] <= 25 or sens.position[0] >= r.getWindowWidth()-25:
        r.setMousePosition(cX, sens.position[1])
        
    if sens.position[1] <= 25 or sens.position[1] >= r.getWindowHeight()-125:
        r.setMousePosition(sens.position[0], cY)    
    

main()
