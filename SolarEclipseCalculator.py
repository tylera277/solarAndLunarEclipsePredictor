import numpy as np
import math

from sideFunctions import time2Julian, earth2Sun, sun2Moon
from sideFunctions import leapYearAdjuster
from angleCalculations import AngleCalculations as angleCalc



class SolarEclipseCalculator:
    """
    This class calculates the times in which a solar eclipse
    is scheduled to take place.
    """

    def __init__(self, year, month, minuteSteps):
        self.year = year
        self.month = month
        self.minuteSteps = minuteSteps

    def MonthLimits(self):
        """
        Allows one to either run a single month or the whole year
        """
        if self.month == 'ALL':
            lowerMonthLimit = 1
            upperMonthLimit = 13
        else:
            lowerMonthLimit = self.month
            upperMonthLimit = self.month+1

        return lowerMonthLimit, upperMonthLimit

    def DetermineTimes(self):

        lowerMonthLimit, upperMonthLimit = self.MonthLimits()

        # this gets the position vectors of the stellar bodies that we are using
        from jplephem.spk import SPK
        kernel = SPK.open('de440.bsp')

        possibleSolarEclipseDates = np.zeros((13, 1000))

        # + These for loops check each date to see whether it meets the criteria below,
        #   basically that the moons shadow hits somewhere within the cross-section of the earth.
        for TestYear in range(self.year, self.year+1, 1):

            for TestMonth in range(lowerMonthLimit, upperMonthLimit, 1):
                counter = 0

                # this function handles if its a leap year, adjusting the days in that particular month
                dayUpperRange = leapYearAdjuster(TestYear, TestMonth)

                for TestDay in range(1, dayUpperRange, 1):
                #for TestDay in range(1, 15, 1):
                    for TestHour in range(1, 24, 1):
                        for TestMinute in range(1, 60, self.minuteSteps):


                            # This gets the julian date for that specific time of year
                            julianTime = time2Julian(TestYear, TestMonth, TestDay, TestHour, TestMinute)

                            # position of earths center w.r.t. the sun
                            positionEarth = earth2Sun(julianTime)

                            xEarthCent = positionEarth[0]
                            yEarthCent = positionEarth[1]
                            zEarthCent = positionEarth[2]


                            # position of moon w.r.t. the sun
                            positionMoon = sun2Moon(julianTime)

                            xMoonCent = positionMoon[0]
                            yMoonCent = positionMoon[1]
                            zMoonCent = positionMoon[2]

                            # radius of the respective body (km)
                            r_earth = 6378
                            r_moon = 1737
                            r_sun = 696000

                            # For the sun
                            sun_x_point1 = r_sun * math.sin(90-math.atan(yMoonCent/xMoonCent))
                            sun_y_point1 = -r_sun * math.cos(90-math.atan(yMoonCent/xMoonCent))

                            sun_x_point2 = -r_sun * math.sin(90-math.atan(yMoonCent/xMoonCent))
                            sun_y_point2 = r_sun * math.cos(90-math.atan(yMoonCent/xMoonCent))

                            sun_z_pointT = r_sun
                            sun_z_pointB = -r_sun

                            # For the moon
                            moon_x_point1 = xMoonCent + r_moon * math.sin(90-math.atan(yMoonCent/xMoonCent))
                            moon_y_point1 = yMoonCent + -r_moon * math.cos(90-math.atan(yMoonCent/xMoonCent))

                            moon_x_point2 = xMoonCent + -r_moon * math.sin(90 - math.atan(yMoonCent / xMoonCent))
                            moon_y_point2 = yMoonCent + r_moon * math.cos(90 - math.atan(yMoonCent / xMoonCent))

                            moon_z_pointT = r_moon + zMoonCent
                            moon_z_pointB = -r_moon + zMoonCent

                            # For the earth
                            earth_x_point1 = xEarthCent + r_earth * math.sin(90 - math.atan(yEarthCent / xEarthCent))
                            earth_y_point1 = yEarthCent + -r_earth * math.cos(90 - math.atan(yEarthCent / xEarthCent))

                            earth_x_point2 = xEarthCent + -r_earth * math.sin(90 - math.atan(yEarthCent / xEarthCent))
                            earth_y_point2 = yEarthCent + r_earth * math.cos(90 - math.atan(yEarthCent / xEarthCent))

                            earth_z_pointT = r_earth + zEarthCent
                            earth_z_pointB = -r_earth + zEarthCent

                            # ####################################

                            sun2moon_point1_1 = math.atan(
                                (moon_y_point1 - sun_y_point1) / (moon_x_point1 - sun_x_point1))
                            sun2earth_point1_1 = math.atan(
                                (earth_y_point1 - sun_y_point1) / (earth_x_point1 - sun_x_point1))

                            sun2moon_point2_2 = math.atan(
                                (moon_y_point2 - sun_y_point2) / (moon_x_point2 - sun_x_point2))
                            sun2earth_point2_2 = math.atan(
                                (earth_y_point2 - sun_y_point2) / (earth_x_point2 - sun_x_point2))

                            sun2moon_point1_2 = math.atan(
                                (moon_y_point2 - sun_y_point1) / (moon_x_point2 - sun_x_point1))
                            sun2earth_point1_2 = math.atan(
                                (earth_y_point2 - sun_y_point1) / (earth_x_point2 - sun_x_point1))

                            sun2moon_point2_1 = math.atan(
                                (moon_y_point1 - sun_y_point2) / (moon_x_point1 - sun_x_point2))
                            sun2earth_point2_1 = math.atan(
                                (earth_y_point1 - sun_y_point2) / (earth_x_point1 - sun_x_point2))

                            moon_cent = (xMoonCent**2+yMoonCent**2+zMoonCent**2)**(1.0/2.0)
                            earth_cent = (xEarthCent ** 2 + yEarthCent ** 2+zEarthCent**2) ** (1.0 / 2.0)

                            sun2moon_point_B2B = math.atan((moon_z_pointB - sun_z_pointB)/(moon_cent))
                            sun2earth_point_B2B = math.atan((earth_z_pointB - sun_z_pointB)/(earth_cent))

                            sun2moon_point_T2T = math.atan((moon_z_pointT - sun_z_pointT) / (moon_cent))
                            sun2earth_point_T2T = math.atan((earth_z_pointT - sun_z_pointT) / (earth_cent))

                            # X & Y alignment checker
                            if ((sun2earth_point1_1<=sun2moon_point1_1<=sun2earth_point1_2) or \
                                    (sun2earth_point2_1<=sun2moon_point2_2<=sun2earth_point2_2)) or \
                                    ((sun2earth_point1_1 >= sun2moon_point1_1 >= sun2earth_point1_2) or \
                                     (sun2earth_point2_1 >= sun2moon_point2_2 >= sun2earth_point2_2)):

                                    # Z-axis alignment checker
                                    if ((sun2moon_point_B2B <= sun2earth_point_B2B) and (sun2moon_point_T2T >= sun2earth_point_T2T)) \
                                            or \
                                            ((sun2moon_point_B2B >= sun2earth_point_B2B) and (sun2moon_point_T2T <= sun2earth_point_T2T)):

                                        print(TestYear, TestMonth, TestDay, TestHour, TestMinute)
                                        possibleSolarEclipseDates[TestMonth][counter] = (julianTime)
                                        counter += 1

        return possibleSolarEclipseDates