Netflix-automatic-resume
========================

Automatizes clicking the resume button of netflixes automatic pause that happens after few episodes of TV-Series

Automatically clicks the "resume playing" button when this happens:
![screenshot](http://i.imgur.com/MpCxPl2.jpg)

### installation:
```
pip install -r requirements.txt
```
After that just run the main.py when you start watching netflix


### Version 0.1
* Only works with windows (uses win32api, don't have way to code linux or macOS right now since I can't test it)
* Only works with 1080p and 720p resolutions. (New resolutions can be added by adding the position of ![play_icon](http://i.imgur.com/RR3cTl7.png) icon at your pause screen to config.cfg (No programming needed)



