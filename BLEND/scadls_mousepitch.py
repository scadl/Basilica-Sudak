import bge
from bge import render as r

def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner    
    
    cY = r.getWindowHeight()//2
    cX = r.getWindowWidth()//2

    sens = cont.sensors['Mouse']
    actuYR = cont.actuators['Motion.YR']
    actuYL = cont.actuators['Motion.YL']
        
    if own["propY"] < sens.position[1]+3:
        cont.activate(actuYR)
    else:
        cont.deactivate(actuYR)
        
    if own["propY"] > sens.position[1]-3:
        cont.activate(actuYL)
    else:
        cont.deactivate(actuYL)
        
    own["propY"] = sens.position[1]
        
    if sens.position[1] <= 25 or sens.position[1] >= r.getWindowHeight()-125:
        r.setMousePosition(sens.position[0], cY)    
    

main()
