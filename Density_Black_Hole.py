import math
import matplotlib.pyplot as plt

c=299792458
G=6.67e-11

def Density(x):
    mass=x*1.989e30
    radius=2*G*mass/(c*c)
    vol=(4*math.pi*radius**3)/3
    den=mass/vol
    return den

massplot=[]
densityplot=[]
water=[]

for x in range(1,1000000000,1000):
    massplot.append(x)
    densityplot.append(Density(x))
    water.append(1e3)

plt.plot(massplot,densityplot,'-',label='Black Hole')
plt.plot(massplot,water,'-',label='Water')

plt.xscale('log')
plt.yscale('log')
plt.legend(loc=1)
plt.xlabel('mass/Solar masses')
plt.ylabel('density/kg^m3')
plt.savefig('black hole density.png',dpi=1000)