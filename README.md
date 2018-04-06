# br34k_1mg

#### WTF ?
1. Script to randomly change the hexa of a image to break it
2. basically it's equal to that pseudo-code --> img_hex[random] = random(00,FF)
3. Press Enter to change something 
4. Press "r" to reset the image

#### usage :
```$ python br34k_1mg.py filename.jpg output.jpg```

```ENTER ENTER ENTER ENTER ENTER ENTER r ENTER ENTER etc...```

#### Some points about it :
* only tested with jpeg
* it's dumb , doens't check if the offset is right , nor if will make the img crash .
* if crash , the code just reset it all
* the code is silly and ugly , but make nice results
* the "breaking" is different depending on the viewer / encoding ( yeah , it sucks )
* was done in 2 hours , so , please

# Example 
### Before :
![](http://i.imgur.com/gIsAVxU.jpg)
### After breaking the Enter key :
![](http://i.imgur.com/rlpBanx.jpg)
