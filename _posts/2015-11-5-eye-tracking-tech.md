---
layout: blogpost
title: Blog
desc: Read about our day-to-day activities
post_title: Tools for Eye Tracking
author: Shariq Iqbal
category: blog
---

The past couple of weeks of messing around with our brand new [Tobii](http://www.tobii.com/) Eye-Tracking Glasses have seen some exciting developments that will allow us to do some really cool research! First though, we needed to make sure what we already had working was possible. Our previous eye-tracking studies used a monitor-based system which provides gaze coordinates relative to the monitor, but the glasses only provide coordinates relative to the camera on the front of the glasses.

In order to track what is being viewed on a screen while wearing the glasses, we need to be able to translate from glasses-camera-cooordinates to monitor-coordinates. We did this by implementing a computer vision algorithm using [OpenCV](http://opencv.org/) (a popular framework for computer vision with Python bindings) that finds the screen in the camera's coordinates. The first step was to create a basic task in [PsychoPy](http://www.psychopy.org/) (Python environment for designing/running psych studies) that displayed a video with a green border on the edge of the screen. This green border is used in a manner similar to Hollywood green-screen technology to find the edges of the screen. Once we have the edges, we can find the corners and map them to screen coordinates, and our job is complete. We can now track what objects are being viewed on screen with close to the same accuracy as the monitor-based eye tracking solution.

We did not purchase these glasses to do what we could already do, though. After completing the first step, we decided to try something ambitious. We wanted to be able to track *any* object using the glasses, not just a computer screen. This would open up a whole new can of worms for research possibilities.

In order to get started, we needed to confirm that we could find an object inside a movie frame. I recorded a video with the glasses on while picking up and looking at a bottle of honey. I then took a picture of the bottle to use as a reference. Using OpenCV (once again) we devised a method to find the honey bottle within the glasses video. Once we accomplished this, it simply became a matter of translating glasses-coordinates to object-coordinates, which we did in the last step. Now, we can track gaze position over objects, simply by taking a picture of the object!

Check out our results in this video

<div class="video-container">
<iframe width="730" height="410" src="https://www.youtube.com/embed/E6c9Z0Mkc-E?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
</div>