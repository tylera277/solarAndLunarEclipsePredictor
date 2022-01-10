import numpy as np

import time

from EclipseCalculator import EclipseCalculator
from SolarEclipseCalculator import SolarEclipseCalculator
from eclipsePlotter import EclipsePlotter



start_time = time.time()


possibleSolarEclipseDates = SolarEclipseCalculator(year=2021,
                                                   month='ALL',
                                                   minuteSteps=60).DetermineTimes()


lat, lon = EclipsePlotter(possibleSolarEclipseDates, month=12).latANDlonFinder()
blurb = EclipsePlotter(possibleSolarEclipseDates, month=12).plotter(lat, lon)

end_time = time.time()
print("Execution Time:{}".format(end_time-start_time))

# I want to create a window that makes this program more user-friendly


