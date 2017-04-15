from __future__ import division,print_function

import os, sys, inspect
a = os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda:0)))
sys.path.append(a + '/../')
sys.path.append(a + '/../vis/')

from VPyDraw import *

def main():
    ind = 0                            #Index (Calculation Counter)
    t = 0                              #Initial time [s]
    dt = 5*10**-9
    
    e1center = [-4.75,0,0]
    e1vel = [1000,1000,1000]
    e2center = [4.75,0,0]
    e2vel = [-1000,-1000,-1000]
    wccenter = [0,0,0]
    loopaxis = [1,0,0]
    
    # Draw some things
    windObj1 = drawWindow(1920, 1080, [0,0,0])
    relclockObj1 = drawTimeClock(windObj1, [-6.5,0,0], t)
    
    wireCoils = WireCoilPair(windObj1, wccenter, loopaxis, 1, 1, 5, 5)
    wireCoils.initDraw()
    
    electron1 = Electron(windObj1, e1center, e1vel)
    electron1.initDraw(10, 50)
    
    electron2 = Electron(windObj1, e2center, e2vel)
    electron2.initDraw(10, 50, color.yellow)
    
    B = BField(windObj1)
    B.BObjList.append(wireCoils)
    B.BObjList.append(electron1)
    B.BObjList.append(electron2)
    #Needs a test
    #for i in [[-5,0,-3.5],[-5,-3.5,0],[-5,0,3.5],[-5,3.5,0]]:
        #j = rotateVector(i,wireCoils.axis_theta,wireCoils.axis_phi)
        #j += wireCoils.Cpair
        #k = sphericalToCartesian(2*wireCoils.d,wireCoils.axis_theta,wireCoils.axis_phi)
        #B.drawBlines(j, pupbound=k, multlng=10000)
    
    while ((-10 + wccenter[0]) <= electron1.p[0] <= (10 + wccenter[0])) and ((-10 + 
            wccenter[1]) <= electron1.p[1] <= (10 + wccenter[1])) and ((-10 + 
            wccenter[2]) <= electron1.p[2] <= (10 + wccenter[2])):
        FPSrate(10000)
        B1array = B.totalBatP(electron1.p)
        B2array = B.totalBatP(electron2.p)
        electron1.updP(B1array, dt)
        electron2.updP(B2array, dt)
        electron1.updDraw()
        electron2.updDraw()
        
        t += dt                  #time increase [s]
        ind += 1                 #index increase
        updateTimeClock(windObj1, relclockObj1, t)
        #print(electron1.p)
        #print(electron2.p)
        
    while True:
        FPSrate(10000)

if __name__ == "__main__":
    main()