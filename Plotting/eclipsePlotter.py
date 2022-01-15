
from IPython.display import Image

class EclipsePlotter:

    def __init__(self, solarEclipseDates, month):
        self.solarEclipseDates = solarEclipseDates
        self.month = month

    def latANDlonFinder(self):
        """
        Function which finds the latitude and longitude on Earth, at the times of the solar eclipses
        that I have predicted, where the altitude and azimuth of the sun and moon are nearly exactly the
        same, within a very small margin.
        """
        import ephem
        import pandas as pd
        import matplotlib.pyplot as plt

        solarEclipseLat = []
        solarEclipseLon = []




        for i in range(len(self.solarEclipseDates[self.month])):


            if (self.solarEclipseDates[self.month][i] == 0):
                break

            moon = ephem.Moon()
            sun = ephem.Sun()
            obsPosition = ephem.Observer()
            #time = pd.to_datetime(self.solarEclipseDates[self.month][i], unit='D', origin='julian')
            time = self.solarEclipseDates[self.month][i]


            for lat1 in range(-90, 90, 1):
                for lon1 in range(-180, 180, 1):

                    obsPosition.lat = "{}".format(lat1)
                    obsPosition.long = "{}".format(lon1)
                    obsPosition.date = "{}".format(time)

                    sun.compute(obsPosition)
                    moon.compute(obsPosition)

                    moonAz = float(moon.az)
                    moonAlt = float(moon.alt)

                    sunAz = float(sun.az)
                    sunAlt = float(sun.alt)

                    if ((abs(sunAlt - moonAlt) < 0.0005) and ((abs(sunAz - moonAz) < 0.0005))):
                    #if((abs(sunAlt - moonAlt) < 0.003) and ((abs(sunAz - moonAz) < 0.003))):

                        # Gets rid of those points that were crossing through the earth.
                        # Positive altitude is above the viewable horizon
                        if (sunAlt and moonAlt) >= 0:
                            # print('car')
                            solarEclipseLat.append(lat1)
                            solarEclipseLon.append(lon1)


        return solarEclipseLat, solarEclipseLon

    def plotter(self, lat, lon):
        """
        Function which plots the points of latitude and longitude from the
        function above onto a map.
        """

        import plotly.express as px
        import pandas as pd


        df = pd.DataFrame(lat)
        df.columns = ['lat']
        df['lon'] = lon
        df['color_column'] = pd.Series([1 for x in range(len(df))])




        fig = px.scatter_geo(df, lat='lat', lon='lon', color='color_column')
        fig = fig.update(layout_coloraxis_showscale=False)
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        fig.write_image('generated_plot.png')
        #fig.update_layout(title='5/29/1919 Solar Eclipse Path', title_x=0.5)
        #fig.show()
