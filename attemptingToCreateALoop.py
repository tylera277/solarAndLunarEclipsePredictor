from mpl_toolkits import mplot3d
import numpy as np
import datetime
import matplotlib.pyplot as plt
from sideFunctions import time2Julian, earth2Sun, sun2Moon, vecMathBtwn2Points
from sideFunctions import leapYearAdjuster
import math
import time


# this gets the position vectors of the stellar bodies that we are using
from jplephem.spk import SPK
kernel = SPK.open('de440.bsp')


yearEclipse = []
possibleSolarEclipseDates = []

# +initial number of days in a month that I set it to, changed according to which month
#
#dayUpperRange = 31

# trying to plot a line from center of sun to center of moon,
# as well as two lines which approximate the diameter of the earth
VecStart_x = [0 for rows in range(20)]
VecEnd_x = [0 for rows in range(20)]
VecStart_y = [0 for rows in range(20)]
VecEnd_y = [0 for rows in range(20)]
VecStart_z = [0 for rows in range(20)]
VecEnd_z = [0 for rows in range(20)]

VecConnection_x = [0 for rows in range(20)]
VecConnection_y = [0 for rows in range(20)]
VecConnection_z = [0 for rows in range(20)]

# +this is how Im going to try to check for possible eclipse dates
#  via this caveman programming for loop, which checks each year,month,day & hour.
# + I have been selecting a specific year in order to compare to resources online to see
#   the accuracy of my model.
for TestYear in range(2021, 2022, 1):
    print(TestYear)
    #time.sleep(4)
    for TestMonth in range(1,13,1):
        # this function handles if its a leap year, adjusting the days in that particular month
        dayUpperRange = leapYearAdjuster(TestYear,TestMonth)


        ##########TEST########
        #lower range of this for loop for TestDay was originally 1
        for TestDay in range(1,dayUpperRange,1):
            for TestHour in range(1, 24, 1):
                julianTime = time2Julian(TestYear, TestMonth, TestDay, TestHour)
                #print(julianTime)
                # position of earths center w.r.t. the sun
                position1 = earth2Sun(julianTime)

# +this is to test when I want to check if the circle that i have placed representing
# the earths cross section is still there, at its normal distance, the cirle becomes too
# small to be able to see
###### T E S T ########
                #position1 = [0,0,0]
###### T E S T ######
                x1 = position1[0]
                y1 = position1[1]
                z1 = position1[2]
                #print(x1, y1, z1)

# position of moon w.r.t. the sun
                position2 = sun2Moon(julianTime)
##### T E S T ########
#position2 = kernel[3,399].compute(julianTime)
#position2 += kernel[3,301].compute(julianTime)
##### T E S T ########

                x2 = position2[0]
                y2 = position2[1]
                z2 = position2[2]
                #print(x2, y2, z2)


# radius of the respective body (km)
                r_earth = 6378
                r_moon = 1737
                r_sun = 696340








#straight line from center of sun to center of moon
                VecStart_x[0] = 0
                VecStart_y[0] = 0
                VecStart_z[0] = 0
                VecEnd_x[0] = x2
                VecEnd_y[0] = y2
                VecEnd_z[0] = z2

# +line that is perpendicular to the line connecting the sun and the earth,
# parallel with the xy plane (horizontal)
# originally centered at the sun but I've translated it by adding x1,y1,z1 to
# it in order to get it centered on the earth
                vecStart1, vecEnd1 = vecMathBtwn2Points(x2, y2, z2, 1, 0)

                VecStart_x[1] = (vecStart1[0] + x1)+r_earth
                VecStart_y[1] = vecStart1[1] + y1
                VecStart_z[1] = vecStart1[2] + z1
                VecEnd_x[1] = (vecEnd1[0] + x1)-r_earth
                VecEnd_y[1] = vecEnd1[1] + y1
                VecEnd_z[1] = vecEnd1[2] + z1
# +line that is perpendicular to the line connecting the sun and the earth,
# parallel with the xz-plane (vertical)
# +originally centered at the sun but I've translated it by adding x1,y1,z1 to
# it in order to get it centered on the earth
                vecStart2, vecEnd2 = vecMathBtwn2Points(x2, y2, z2, 1, 0)

                VecStart_x[2] = vecStart1[0] + x1
                VecStart_y[2] = vecStart1[1] + y1
                VecStart_z[2] = (vecStart1[2] + z1) + r_earth
                VecEnd_x[2] = vecEnd1[0] + x1
                VecEnd_y[2] = vecEnd1[1] + y1
                VecEnd_z[2] = (vecEnd1[2] + z1) - r_earth








                # these are the angle theta from spherical coord.
                # theta plus and minus are angles to get from one side of the earth to the other,horizontally
                # thetaSun2Moon is the angle of the line that goes from sun to moon center

                thetaPlusEarth = math.atan((VecEnd_y[1]) / (VecEnd_x[1]))
                thetaMinusEarth = math.atan((VecStart_y[1]) / VecStart_x[1])
                thetaSun2Moon = math.atan(VecEnd_y[0] / VecEnd_x[0])


                # phi plus and minus are the upper and lower points on the edges of the earth
                # phiSun2Moon is the angle of the line that goes from sun to moon center
                phiPlusEarth = math.atan((math.sqrt(VecEnd_y[2]**2.0 + VecEnd_x[2]**2.0))/VecEnd_z[2])
                phiMinusEarth = math.atan((math.sqrt(VecStart_y[2]**2.0 + VecStart_x[2]**2.0))/VecStart_z[2])
                phiSun2Moon = math.atan((math.sqrt(VecEnd_x[0]**2.0 + VecEnd_y[0]**2.0))/VecEnd_z[0])

                #print(TestYear,TestMonth,TestDay,TestHour)
                #print(phiMinusEarth,phiSun2Moon, phiPlusEarth)
                #print(thetaPlusEarth,thetaSun2Moon, thetaMinusEarth)

# +this checks whether the angle of the line from the sun's center to the moons
# center is within the range of the angle from left/right
# and top/bottom parts of the earth. Im using 2 lines to approximate the cross
# section of the earth right now, may update that later for better accuracy.

# + The last check of this if statement I had to switch the bounds for theta in order for it to get
# solar and lunar eclipses later in the year, not entirely sure why though
                if ((phiMinusEarth <= phiSun2Moon <= phiPlusEarth) and
                    (thetaPlusEarth <= thetaSun2Moon <= thetaMinusEarth)) or \
                    ((phiMinusEarth <= phiSun2Moon <= phiPlusEarth) and
                     (thetaMinusEarth <= thetaSun2Moon <= thetaPlusEarth)):


                    possibleSolarEclipseDates.append(julianTime)
                    #yearEclipse.append(TestYear)
                    #print('#########################')
                    #print(phiMinusEarth, phiSun2Moon, phiPlusEarth)
                    #print(thetaPlusEarth, thetaSun2Moon, thetaMinusEarth)
                    print(TestYear,TestMonth,TestDay,TestHour)
                    #print(possibleSolarEclipseDates)


#+ line that is perpendicular to the line connecting the sun and the moon,
# and I have translated it to the moon
# + this is horizontal line(parallel with the xz-plane)
                    vecStart3, vecEnd3 = vecMathBtwn2Points(x2, y2, z2, 1, 0)

                    VecStart_x[3] = (vecStart3[0] + x2)+ r_moon
                    VecStart_y[3] = vecStart3[1] + y2
                    VecStart_z[3] = (vecStart3[2] + z2)
                    VecEnd_x[3] = (vecEnd3[0] + x2) - r_moon
                    VecEnd_y[3] = vecEnd3[1] + y2
                    VecEnd_z[3] = (vecEnd3[2] + z2)
# + this is vertical line(parallel with the yz-plane) at the moon
                    vecStart4, vecEnd4 = vecMathBtwn2Points(x2, y2, z2, 1, 0)

                    VecStart_x[4] = (vecStart4[0] + x2)
                    VecStart_y[4] = vecStart4[1] + y2
                    VecStart_z[4] = (vecStart4[2] + z2)+ r_moon
                    VecEnd_x[4] = (vecEnd4[0] + x2)
                    VecEnd_y[4] = vecEnd4[1] + y2
                    VecEnd_z[4] = (vecEnd4[2] + z2)- r_moon

#+ line that is perpendicular to the line connecting the sun and the moon,
# sitting on the sun with the suns radius in each direction
# + this is horizontal line(parallel with the xz-plane)
                    vecStart5, vecEnd5 = vecMathBtwn2Points(x2, y2, z2, 1, 0)

                    VecStart_x[5] = vecStart5[0]+ r_sun
                    VecStart_y[5] = vecStart5[1]
                    VecStart_z[5] = vecStart5[2]
                    VecEnd_x[5] = vecEnd5[0]  - r_sun
                    VecEnd_y[5] = vecEnd5[1]
                    VecEnd_z[5] = vecEnd5[2]
# + this is vertical line(parallel with the yz-plane)
                    vecStart6, vecEnd6 = vecMathBtwn2Points(x2, y2, z2, 1, 0)

                    VecStart_x[6] = vecStart6[0]
                    VecStart_y[6] = vecStart6[1]
                    VecStart_z[6] = vecStart6[2]+ r_sun
                    VecEnd_x[6] = vecEnd6[0]
                    VecEnd_y[6] = vecEnd6[1]
                    VecEnd_z[6] = vecEnd6[2]- r_sun

# +trying to draw a line connecting the four edges of the sun to the, in the same plane,
# four edges on the moon. The hope is to eventually project these lines onto the earth in order
# to get location of solar eclipse
# +vec_start(3)&(4) is moon, vecStart(5)&(6) is sun
                    #+these two are connecting the edges on the two bodies in the xz-plane(horizontal)
                    VecConnection_x[0] = VecStart_x[3]-VecStart_x[5]
                    VecConnection_y[0] = VecStart_y[3]-VecStart_y[5]
                    VecConnection_z[0] = VecStart_z[3]-VecStart_z[5]

                    VecConnection_x[1] = VecEnd_x[3]-VecEnd_x[5]
                    VecConnection_y[1] = VecEnd_y[3]-VecEnd_y[5]
                    VecConnection_z[1] = VecEnd_z[3]-VecEnd_z[5]

                    #+ these two are connecting the edges on the two bodies in the yz-plane
                    # (vertical a.k.a.top&bottom)
                    VecConnection_x[2] = VecStart_x[4] - VecStart_x[6]
                    VecConnection_y[2] = VecStart_y[4] - VecStart_y[6]
                    VecConnection_z[2] = VecStart_z[4] - VecStart_z[6]

                    VecConnection_x[3] = VecEnd_x[4] - VecEnd_x[6]
                    VecConnection_y[3] = VecEnd_y[4] - VecEnd_y[6]
                    VecConnection_z[3] = VecEnd_z[4] - VecEnd_z[6]

                    thetaXZplane1 = math.atan(VecConnection_y[0] / VecConnection_x[0])
                    phiXZplane1 = math.atan((math.sqrt(VecConnection_x[0]**2.0 + VecConnection_y[0]**2.0))/VecConnection_z[0])

                    thetaXZplane2 = math.atan(VecConnection_y[1] / VecConnection_x[1])
                    phiXZplane2 = math.atan((math.sqrt(VecConnection_x[1] ** 2.0 + VecConnection_y[1] ** 2.0)) / VecConnection_z[1])

                    thetaXZplane3 = math.atan(VecConnection_y[2] / VecConnection_x[2])
                    phiXZplane3 = math.atan((math.sqrt(VecConnection_x[2] ** 2.0 + VecConnection_y[2] ** 2.0)) / VecConnection_z[2])

                    thetaXZplane4 = math.atan(VecConnection_y[3] / VecConnection_x[3])
                    phiXZplane4 = math.atan((math.sqrt(VecConnection_x[3] ** 2.0 + VecConnection_y[3] ** 2.0)) / VecConnection_z[3])

                    ######### TEST ##########
                    VecStart_x[8] = VecStart_x[5]
                    VecEnd_x[8] = 1000000*math.sin(phiXZplane1)*math.cos(thetaXZplane1)

                    VecStart_y[8] = VecStart_y[5]
                    VecEnd_y[8] = 1000000*math.sin(phiXZplane1)*math.sin(thetaXZplane1)

                    VecStart_z[8] = VecStart_z[5]
                    VecEnd_z[8] = 1000000* math.cos(phiXZplane1)

                    #################
                    VecStart_x[9] = VecEnd_x[5]
                    VecEnd_x[9] = 1000000 * math.sin(phiXZplane2) * math.cos(thetaXZplane2)

                    VecStart_y[9] = VecEnd_y[5]
                    VecEnd_y[9] = 1000000 * math.sin(phiXZplane2) * math.sin(thetaXZplane2)

                    VecStart_z[9] = VecEnd_z[5]
                    VecEnd_z[9] = 1000000 * math.cos(phiXZplane2)
                    ###################
                    VecStart_x[10] = VecStart_x[6]
                    VecEnd_x[10] = 1000000 * math.sin(phiXZplane3) * math.cos(thetaXZplane3)

                    VecStart_y[10] = VecStart_y[6]
                    VecEnd_y[10] = 1000000 * math.sin(phiXZplane3) * math.sin(thetaXZplane3)

                    VecStart_z[10] = VecStart_z[6]
                    VecEnd_z[10] = 1000000 * math.cos(phiXZplane3)

                    #########
                    VecStart_x[11] = VecEnd_x[6]
                    VecEnd_x[11] = 1000000 * math.sin(phiXZplane4) * math.cos(thetaXZplane4)

                    VecStart_y[11] = VecEnd_y[6]
                    VecEnd_y[11] = 1000000 * math.sin(phiXZplane4) * math.sin(thetaXZplane4)

                    VecStart_z[11] = VecEnd_z[6]
                    VecEnd_z[11] = 1000000 * math.cos(phiXZplane4)


                    #print('x:',VecStart_x[8],VecEnd_x[8])
                    #print('y:',VecStart_y[8],VecEnd_y[8])
                    #print('z:',VecStart_z[8],VecEnd_z[8])




############### +I think I need to calculate 4 more of these angles so I get the angles of the lines
                    # connecting the points on the edges of the moon and the sun
                    #+This may be wrong
                    #+I eventually need to project this onto the earth somehow
                    #print(VecConnection_x[2],VecConnection_y[2], VecConnection_z[2])
                    #print(VecEnd_x[0],VecEnd_y[0],VecEnd_z[0])
                    #print(phiXZplane1, thetaXZplane1)
                    #print(phiSun2Moon, thetaSun2Moon)


#print("Date range complete!")
#print('Eclipse years:...')
#print(yearEclipse)









# im using this for loop as a way to detect if the event is a solar or lunar eclipse

earth2Moon_x = []
earth2Moon_y = []
earth2Moon_z = []
radiusOfMoonOrbit = []
radiusOfEarthOrbit = []
earth2Sun_x = []
earth2Sun_y = []
earth2Sun_z = []
radiusOfEarthSunOrbit = []

for i in range(len(possibleSolarEclipseDates)):

    earth2Moon = sun2Moon(possibleSolarEclipseDates[i])
    earth2Moon_x.append(earth2Moon[0])
    earth2Moon_y.append(earth2Moon[1])
    earth2Moon_z.append(earth2Moon[2])

    radiusOfMoonOrbit.append((earth2Moon_x[i]**2.0 + earth2Moon_y[i]**2.0 + earth2Moon_z[i]**2.0)**(1.0/2.0))

    radiusOfEarthOrbit = earth2Sun(possibleSolarEclipseDates[i])

    earth2Sun_x.append(radiusOfEarthOrbit[0])
    earth2Sun_y.append(radiusOfEarthOrbit[1])
    earth2Sun_z.append(radiusOfEarthOrbit[2])
    radiusOfEarthSunOrbit.append((earth2Sun_x[i]**2.0 + earth2Sun_y[i]**2.0 + earth2Sun_z[i]**2.0)**(1.0/2.0))


    # if earth orbit is closer to sun than moon is,
    #if radiusOfEarthSunOrbit[i] < radiusOfMoonOrbit[i]:
        #print(possibleSolarEclipseDates[i], ' :may be a lunar eclipse.')
    #else:
       #print(possibleSolarEclipseDates[i],' :may be a solar eclipse.')

#print(possibleSolarEclipseDates)
#print('x :',earth2Moon_x)
#print('y :',earth2Moon_y)
#print('z :',earth2Moon_z)
#print(len(possibleSolarEclipseDates))
print('#################################')








# this creates the raw blank figure
fig = plt.figure()
#ax = plt.axes(projection='3d')
ax = fig.add_subplot(projection='3d')
ax.set_xlim(-1.5*10**8,1.5*10**8)
ax.set_ylim(-1.5*10**8, 1.5*10**8)
ax.set_zlim(-1.5*10**8, 1.5*10**8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# the dots representing each planetary body
#ax.scatter(x1, y1, z1, s=r_earth/1000, c='green')
#ax.scatter(x2, y2, z2, s=r_moon/1000, c='gray')
#ax.scatter(0, 0, 0, s=r_sun/1000, c='yellow')

# this puts a circle that faces the sun on earth, representing the middle cross section
#theta = np.linspace(0, 2 * np.pi, 201)
#x = np.cos(theta)*r_earth +x1
#z = np.sin(theta)*r_earth +z1
#y = np.zeros(201) +y1
#ax.plot(x,y,z,c='red')


for i in range(15):
    ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],VecEnd_y[i]],[VecStart_z[i],VecEnd_z[i]])


#plt.show()