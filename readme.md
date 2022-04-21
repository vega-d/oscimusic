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

