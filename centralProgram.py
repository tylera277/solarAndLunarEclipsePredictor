import numpy as np

from EclipseCalculator import EclipseCalculator
from eclipsePlotter import EclipsePlotter


possibleSolarEclipseDates = EclipseCalculator(year=2023,
                                              month=10,
                                              minuteSteps=10).DetermineTimes()

#print(possibleSolarEclipseDates[10])

lat, lon = EclipsePlotter(possibleSolarEclipseDates, month=10).latANDlonFinder()
blurb = EclipsePlotter(possibleSolarEclipseDates, month=10).plotter(lat, lon)


