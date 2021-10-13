from mpl_toolkits import mplot3d
import numpy as np
import datetime
import matplotlib.pyplot as plt
from sideFunctions import time2Julian, earth2Sun, sun2Moon, vecMathBtwn2Points, rhoPrime
from sideFunctions import leapYearAdjuster

import math
import time
from angleCalculations import AngleCalculations as angleCalc


# this gets the position vectors of the stellar bodies that we are using
from jplephem.spk import SPK
kernel = SPK.open('de440.bsp')


yearEclipse = []
possibleSolarEclipseDates = []


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

solarEclipseLat = [[0 for x in range(10000)] for y in range(13)]
solarEclipseLon = [[0 for x in range(10000)] for y in range(13)]
m = 0


# + These for loops check each date to see whether it meets the criteria below,
#   basically that the moons shadow hits somewhere within the cross section of the earth.
# + I have been selecting a specific year in order to compare to resources online to see
#   the accuracy of my model.
for TestYear in range(2021, 2022, 1):

    for TestMonth in range(1,13,1):

        # this function handles if its a leap year, adjusting the days in that particular month
        dayUpperRange = leapYearAdjuster(TestYear,TestMonth)

        for TestDay in range(1,dayUpperRange,1):
            for TestHour in range(1, 24, 1):
                for TestMinute in range(1,60,60):

                    # This gets the julian date for that specific time of year
                    julianTime = time2Julian(TestYear, TestMonth, TestDay, TestHour,TestMinute)

                    # position of earths center w.r.t. the sun
                    position1 = earth2Sun(julianTime)

                    xEarthCent = position1[0]
                    yEarthCent = position1[1]
                    zEarthCent = position1[2]

                    # position of moon w.r.t. the sun
                    position2 = sun2Moon(julianTime)

                    xMoonCent = position2[0]
                    yMoonCent = position2[1]
                    zMoonCent = position2[2]


                    # radius of the respective body (km)
                    r_earth = 6378
                    r_moon = 1737
                    r_sun = 696340

                    # straight line from center of sun to center of moon
                    VecStart_x[0] = 0
                    VecStart_y[0] = 0
                    VecStart_z[0] = 0
                    VecEnd_x[0] = xMoonCent
                    VecEnd_y[0] = yMoonCent
                    VecEnd_z[0] = zMoonCent

                    # +line that is perpendicular to the line connecting the sun and the earth,
                    # parallel with the xy plane (horizontal)
                    # originally centered at the sun but I've translated it by adding x1,y1,z1 to
                    # it in order to get it centered on the earth
                    vecStart1, vecEnd1 = vecMathBtwn2Points(xEarthCent, yEarthCent, zEarthCent, 1, 0)

                    VecStart_x[1] = (vecStart1[0] + xEarthCent)+r_earth
                    VecStart_y[1] = vecStart1[1] + yEarthCent
                    VecStart_z[1] = vecStart1[2] + zEarthCent
                    VecEnd_x[1] = (vecEnd1[0] + xEarthCent)-r_earth
                    VecEnd_y[1] = vecEnd1[1] + yEarthCent
                    VecEnd_z[1] = vecEnd1[2] + zEarthCent

                    # +line that is perpendicular to the line connecting the sun and the earth,
                    # parallel with the xz-plane (vertical)
                    # +originally centered at the sun but I've translated it by adding x1,y1,z1 to
                    # it in order to get it centered on the earth
                    vecStart2, vecEnd2 = vecMathBtwn2Points(xEarthCent, yEarthCent, zEarthCent, 1, 0)

                    VecStart_x[2] = vecStart1[0] + xEarthCent
                    VecStart_y[2] = vecStart1[1] + yEarthCent
                    VecStart_z[2] = (vecStart1[2] + zEarthCent) + r_earth
                    VecEnd_x[2] = vecEnd1[0] + xEarthCent
                    VecEnd_y[2] = vecEnd1[1] + yEarthCent
                    VecEnd_z[2] = (vecEnd1[2] + zEarthCent) - r_earth

                    # + line that is perpendicular to the line connecting the sun and the moon,
                    # and I have translated it to the moon
                    # + this is horizontal line(parallel with the xz-plane)
                    vecStart3, vecEnd3 = vecMathBtwn2Points(xMoonCent, yMoonCent, zMoonCent, 1, 0)

                    VecStart_x[3] = (vecStart3[0] + xMoonCent) + r_moon
                    VecStart_y[3] = vecStart3[1] + yMoonCent
                    VecStart_z[3] = (vecStart3[2] + zMoonCent)
                    VecEnd_x[3] = (vecEnd3[0] + xMoonCent) - r_moon
                    VecEnd_y[3] = vecEnd3[1] + yMoonCent
                    VecEnd_z[3] = (vecEnd3[2] + zMoonCent)

                    # + this is vertical line(parallel with the yz-plane) at the moon
                    vecStart4, vecEnd4 = vecMathBtwn2Points(xMoonCent, yMoonCent, zMoonCent, 1, 0)

                    VecStart_x[4] = (vecStart4[0] + xMoonCent)
                    VecStart_y[4] = vecStart4[1] + yMoonCent
                    VecStart_z[4] = (vecStart4[2] + zMoonCent) + r_moon
                    VecEnd_x[4] = (vecEnd4[0] + xMoonCent)
                    VecEnd_y[4] = vecEnd4[1] + yMoonCent
                    VecEnd_z[4] = (vecEnd4[2] + zMoonCent) - r_moon








                # these are the angle theta from spherical coord.
                # theta plus and minus are angles to get from one side of the earth to the other,horizontally
                # thetaSun2Moon is the angle of the line that goes from sun to moon center
                    thetaPlusEarth = angleCalc.theta(0, VecEnd_x[1], VecEnd_y[1])
                    thetaMinusEarth = angleCalc.theta(0, VecStart_x[1], VecStart_y[1])
                    thetaSun2Moon = angleCalc.theta(0, VecEnd_x[0], VecEnd_y[0])
                    ####### TEST ########
                # lines that are being drawn from center of sun to horizontal edges of the moon
                    thetaSun2Moon1 = angleCalc.theta(0, VecEnd_x[3], VecEnd_y[3])
                    thetaSun2Moon2 = angleCalc.theta(0, VecStart_x[3], VecStart_y[3])



                # phi plus and minus are the upper and lower points on the edges of the earth
                # phiSun2Moon is the angle of the line that goes from sun to moon center
                    phiPlusEarth = angleCalc.phi(0, VecEnd_x[2], VecEnd_y[2], VecEnd_z[2])
                    phiMinusEarth = angleCalc.phi(0, VecStart_x[2], VecStart_y[2], VecStart_z[2])
                    phiSun2Moon = angleCalc.phi(0, VecEnd_x[0], VecEnd_y[0], VecEnd_z[0])
                # lines that are being drawn from center of sun to vertical edges of the moon
                    phiSun2Moon1 = angleCalc.phi(0, VecEnd_x[4], VecEnd_y[4], VecEnd_z[4])
                    phiSun2Moon2 = angleCalc.phi(0, VecStart_x[4], VecStart_y[4], VecStart_z[4])




                    # +this checks whether the angle of the line from the sun's center to the moons horizontal
                    # and vertical edges, where I have split the moon's cross section into two perpendicular lines,
                    # is within the range of the angle from left/right
                    # and top/bottom parts of the earth, same thing being done to the earth as was done to the moon.



                    if ((phiMinusEarth <= phiSun2Moon1 <= phiPlusEarth) or (phiMinusEarth <= phiSun2Moon2 <= phiPlusEarth)) and \
                            (((thetaPlusEarth <= thetaSun2Moon1 <= thetaMinusEarth) or (thetaPlusEarth <= thetaSun2Moon2 <= thetaMinusEarth)) or \
                             (thetaMinusEarth <= thetaSun2Moon1 <= thetaPlusEarth) or (thetaMinusEarth <= thetaSun2Moon2 <= thetaPlusEarth)):

                        possibleSolarEclipseDates.append(julianTime)
                        print(TestYear, TestMonth, TestDay, TestHour)









