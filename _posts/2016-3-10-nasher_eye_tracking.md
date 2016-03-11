---
layout: blogpost
title: Blog
desc: Read about our day-to-day activities
post_title: Eye Tracking and Art
author: Shariq Iqbal
category: #blog
---

In our [previous attempts](https://pearsonlab.github.io/blog/2015/11/06/eye_tracking_tech.html) at tracking gaze location from a dynamic video over static objects, we were fairly conservative in that we did not attempt to view the target object from a skewed angle, and we ensured that the entire object was in the video frame at all times. Recently though, we encountered a use case that would test the limits of our technology.

In collaboration with [Zab Johnson](https://dibs.duke.edu/scholars/elizabeth-johnson)'s lab, we have been exploring the use of eye tracking in art exhibits, which presents a new challenge for us. We wanted people to be able to view the art in the most natural way possible, with the ability to get up close and turn their head if they wanted to, so we needed to make sure that we could still map gaze points from close up and extreme angles back to a static image of the piece of art. An example of our technique applied to a single frame is below.

{% include blog_image.html url="http://people.duke.edu/~sni/mutu1.jpg" %}
 
We take a match image such as this and try to find it in a video frame.

{% include blog_image.html url="http://people.duke.edu/~sni/video_frame.png" %}

We then select a box from that video frame to transform to the match image's dimensions.

{% include blog_image.html url="http://people.duke.edu/~sni/transformed.png" %}

The perspective transform is important because we also apply that same transformation to gaze location points, in order to get the gaze location on the static image. Check out the results when we apply this to a full video:

<div class="video-container">
<iframe width="730" height="410" src="https://www.youtube.com/embed/fSl6FiyHTes?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
</div>
<br>

