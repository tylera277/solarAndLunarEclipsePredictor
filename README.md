# solarAndLunarEclipsePredictor

This is a program which I made which tries to predict when solar and lunar eclipses will happen on earth. My model predicts for 2021,![2021UpdatedPredictions](https://user-images.githubusercontent.com/37377528/120257038-6d834a80-c25d-11eb-89b9-f3c9041ab5ee.png)

And compare this to what the actual dates are,
![actualEclipses2021](https://user-images.githubusercontent.com/37377528/120106565-7b38b300-c12b-11eb-8ca0-3bb82728881f.png)
Which is highly accurate. And then to look at the specific times for, lets say, May 26, the actual times are 
![may26-2021EclipseTimes](https://user-images.githubusercontent.com/37377528/120106615-cb177a00-c12b-11eb-8eee-521c8a0482eb.png)
And for June 10th,
![june10Eclipse](https://user-images.githubusercontent.com/37377528/120106770-61e43680-c12c-11eb-9775-695575f3b16e.png)
November 19th, 
![nov19Eclipse](https://user-images.githubusercontent.com/37377528/120106785-732d4300-c12c-11eb-8c0b-f94b8ed80d35.png)
And lastly December 4th,
![dec4Eclipse](https://user-images.githubusercontent.com/37377528/120106799-7de7d800-c12c-11eb-844b-fbdae84fa211.png)

Admittedly, not all of the years I run through my model are always this accurate. One shortcoming of this program is that it does not model where the eclipse is seen on planet earth, as I was stuck on how to do this and plus I wanted to start learning how to program in the object-oriented paradigm, as I've realized my programs are incredibly messy and would be hard to follow for other eyes. I may come back to this and add it later, Im not sure.

**5/26/2021 update:** I changed the criteria to identify a solar and lunar eclipse by having four lines projecting from center of the sun to the two horizontal and two vertical edges of the moon, and then checking to see if those lines angles fell within the range of the earth's angular size. I originally had it so only a single line was going from sun to the center of moon, and this change has dramatically increased my accuracy at predicting the hours an eclipse takes place. Some of the penumbra lunar eclipses are causing some issues maybe, but I dont care as those arent that cool anyways.

