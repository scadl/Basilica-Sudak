import bge
from bge import render as r

def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    cY = r.getWindowHeight()//2
    cX = r.getWindowWidth()//2

    sens = cont.sensors['Mouse']
    actuXR = cont.actuators['Motion.XR']
    actuXL = cont.actuators['Motion.XL']
    
    if own["propX"] < sens.position[0]:
        cont.activate(actuXR)
    else:
        cont.deactivate(actuXR)
        
    if own["propX"] > sens.position[0]:
        cont.activate(actuXL)
    else:
        cont.deactivate(actuXL)
        
    own["propX"] = sens.position[0]
    
    if sens.position[0] <= 25 or sens.position[0] >= r.getWindowWidth()-25:
        r.setMousePosition(cX, sens.position[1])    

main()
