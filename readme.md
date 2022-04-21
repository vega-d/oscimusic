# OsciMusic

this project is my crapshot at making a workable music player for viewing oscilloscope music files.
It isn't particularily good at anything, but it works quite well and uses OpenGL to render the lines, so performance is pretty good.

Required libraries can be installed throguh the `requirements.txt` file, and the script has integrated file selector so just put your .wav alongside the script in the same directory and run. 

Quick command for installing all dependencies: 
```commandline
pip3 install pygame pyopengl scipy numpy
```

it never turned out to be lightweight, at least on my machine I have python use 200mb of ram while playing "Jerobeam Fenderson - 06 Planets".

Unfortunately it doesn't play the sound alongside the visuals, and the speed can be off, but if you have any idea how to play raw tones with python, feel free to open an issue or a pull request.

![image](https://user-images.githubusercontent.com/35414314/164499666-c8a82fc8-a703-4ad6-9795-8c031228ab26.png)
![image](https://user-images.githubusercontent.com/35414314/164500516-10b23995-bb23-45aa-8c05-4b0bc43d3dd1.png)
![image](https://user-images.githubusercontent.com/35414314/164500766-70c14eac-a169-4d2d-889f-c5eaec83d960.png)
