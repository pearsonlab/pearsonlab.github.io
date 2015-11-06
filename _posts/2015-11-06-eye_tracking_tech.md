---
layout: blogpost
title: Blog
desc: Read about our day-to-day activities
post_title: Tools for Eye Tracking
author: Shariq Iqbal
category: blog
date: 2015-11-06 16:11:00
---

In the P[&lambda;]ab, one of our main research focuses is eye-tracking. We have a collaboration with [faculty](/people.html) in the Psychiatry department looking at [pupillometry](https://github.com/pearsonlab/pupil) and its relationship to fear. Currently we're using screen based eye-tracking devices that provide gaze coordinates in terms of where on the screen you are looking. Recently, we obtained some brand new [Tobii](http://www.tobii.com/) Eye-Tracking Glasses that can allow us to expand beyond screen-based experiments, and in the last couple weeks we seen some exciting developments that will allow us to do really cool research!

{% include blog_image.html url="https://upload.wikimedia.org/wikipedia/commons/6/67/Tobii_Glasses_2_Eye_Tracker_Wearable_System_Tobii_I.jpg" description="The Tobii Glasses" %}

First though, we needed to make sure we could still track gaze location on a screen, since the Tobii glasses only provide gaze coordinates in reference to the camera on the front of the glasses.  In order to track what is being viewed on a screen while wearing the glasses, we need to be able to translate from glasses-camera-cooordinates to monitor-coordinates. We did this by implementing a computer vision algorithm using [OpenCV](http://opencv.org/) (a popular framework for computer vision with Python bindings) that finds the screen in the camera's coordinates.

The first step was to create a basic task in [PsychoPy](http://www.psychopy.org/) (Python environment for designing/running psych studies) that displayed a video with a green border on the edge of the screen. This green border is used in a manner similar to Hollywood green-screen technology to find the edges of the screen. Once we have the edges, we can find the corners and map them to screen coordinates, and our job is complete. We can now track what objects are being viewed on screen with close to the same accuracy as the monitor-based eye tracking solution.

{% include blog_image.html url="http://people.duke.edu/~sni/green_screen.jpg" description="Screen with green border" %}

After completing the first step, we decided to try something ambitious that would really push the limits of what is capable with the new technology. What if we could simply take a picture of an object, and track eye position over the object based on information from the glasses video and eye tracking? This would open up a whole new realm of research possibilities.

{% include blog_image.html url="http://people.duke.edu/~sni/sidebyside_org.jpg" description="Image and video frame to search for image" %}

We needed to confirm that we could find the desired object inside a movie frame. I recorded a video with the glasses on while picking up and looking at a bottle of honey. I then took a picture of the bottle to use as a reference. Using OpenCV (once again) we devised a method to find the honey bottle within the glasses video. Once we accomplished this, it simply became a matter of translating glasses-coordinates to object-coordinates, which we did in the last step. Now, we can track gaze position over objects, simply by taking a picture of the object!

Check out this video for a visual demonstration.

<div class="video-container">
<iframe width="730" height="410" src="https://www.youtube.com/embed/E6c9Z0Mkc-E?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
</div>
<br>

For the future, we are interested in using face-tracking technology to track eye movements over a *dynamic* object (more difficult than tracking the honey bottle because faces are constantly changing shape), so that we can run studies involving competitive tasks (e.g. simplified poker) and plot gaze points over a face. We are optimistic that this is possible, and we'll post any updates in this space!