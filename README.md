# solarAndLunarEclipsePredictor

This is a program which I made which tries to predict when solar and lunar eclipses will happen on earth. My model predicts for 2021, (in the form of year, month,day, and hour)
<img width="303" alt="inputToSolver" src="https://user-images.githubusercontent.com/37377528/120257038-6d834a80-c25d-11eb-89b9-f3c9041ab5ee.png">

And compare this to what the actual dates are,
<p align="center">
  <img width="600" height="200" src="https://user-images.githubusercontent.com/37377528/120106565-7b38b300-c12b-11eb-8ca0-3bb82728881f.png">
</p>

Which is highly accurate. And then to look at the specific times for, lets say, May 26, the actual times are 
<p align="center">
  <img width="600" height="200" src="https://user-images.githubusercontent.com/37377528/120106615-cb177a00-c12b-11eb-8eee-521c8a0482eb.png">
</p>

And for June 10th,
<p align="center">
  <img width="600" height="200" src="https://user-images.githubusercontent.com/37377528/120106770-61e43680-c12c-11eb-9775-695575f3b16e.png">
</p>

November 19th, 
<p align="center">
  <img width="600" height="200" src="https://user-images.githubusercontent.com/37377528/120106785-732d4300-c12c-11eb-8c0b-f94b8ed80d35.png">
</p>
And lastly December 4th,
<p align="center">
  <img width="600" height="200" src="https://user-images.githubusercontent.com/37377528/120106799-7de7d800-c12c-11eb-844b-fbdae84fa211.png">
</p>

Admittedly, not all of the years I run through my model are always this accurate. 

**5/26/2021 update:** I changed the criteria to identify a solar and lunar eclipse by having four lines projecting from center of the sun to the two horizontal and two vertical edges of the moon, and then checking to see if those lines angles fell within the range of the earth's angular size. I originally had it so only a single line was going from sun to the center of moon, and this change has dramatically increased my accuracy at predicting the hours an eclipse takes place. Some of the penumbra lunar eclipses are causing some issues though.

