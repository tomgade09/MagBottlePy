from visual import *

def drawWindow(wd, ht, centx, centy, centz, to, d, R):
    # Graphical Necessities
    scene = display(title='Electron in Magnetic Bottle', autocenter=0, width=wd, 
        height=ht, center=(centx,centy,centz), exit=0, range=(15,15,15))
    xaxpt=[0,1,2,3,4,5,6,7,8,9,10]
    yaxpt=[0,1,2,3,4,5,6,7,8,9,10]
    zaxpt=[0,1,2,3,4,5,6,7,8,9,10]
    ring(pos=(-d,0,0), axis=(1,0,0), radius=R, thickness=0.01)
    ring(pos=(d,0,0), axis=(1,0,0), radius=R, thickness=0.01)
    xlbl = label(pos=(10,1,0), text='x')
    ylbl =  label(pos=(1,10,0), text='y')
    zlbl =  label(pos=(0,1,10), text='z')
    for i in range(0,10,1):
        points(pos=(xaxpt[i],0,0), size=5, color=color.cyan)
        points(pos=(0,yaxpt[i],0), size=5, color=color.cyan)
        points(pos=(0,0,zaxpt[i]), size=5, color=color.cyan)

    relativetime = label(pos=(-6.5, 0, 0), text='t = ' + str(to) + ' s')
    
    return scene, relativetime
    
def drawParticlePic(po_x, po_y, po_z):
    particle = sphere(pos=(po_x,po_y,po_z), radius=0.0000001, color=color.green,
        make_trail=True, trail_type="points", interval=10, retain=100)
        
    return particle
    
def updateParticlePic(partObj,relclockObj,px,py,pz,relt):
    partObj.pos = (px,py,pz)
    relclockObj.text = 't = ' + str(relt) + ' s'