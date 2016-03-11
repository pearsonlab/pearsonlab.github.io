---
layout: blogpost
title: Blog
desc: Read about our day-to-day activities
post_title: Eye Tracking and Art
author: Shariq Iqbal and John Pearson
category: blog
---

As a lab, we're interested in natural behaviors. This can mean a lot of things, but in particular, it means attempting to study human and animal behavior the way it occurs outside the lab. Many of the tools we build harness modern computing to enable us to do this with the precision and rigor of traditional lab experiments.

In our [previous attempts](https://pearsonlab.github.io/blog/2015/11/06/eye_tracking_tech.html) at extracting gaze location from a dynamic video and mapping it back to static objects, we were fairly conservative in that we did not attempt to view the target object from a skewed angle, and we ensured that the entire object was in the video frame at all times. It's a fairly simple application that nonetheless touches on some fairly clever pieces of computer vision.

More recently, though, we've been exploring a new use case that raises all sorts of intriguing complexities: the act of viewing a work of art.

When we look at a painting, for example, we are typically "doing more" than what we might do when recognizing an image of a platypus or a car on a computer screen. Lots of writing in the humanities tries to understand what this "doing more" entails, but at the very least, it encompasses our patterns of gaze (what we look at and in what order) and the dynamics of our bodies in space (where we stand and the perspective from which we look). What's more, artists themselves have long contemplated these same aspects of the viewing process and created works designed to interact with, engage, and surprise us as we look.

So if works of art are objects meant to provoke rich and unique patterns of looking, why not study this process?

In collaboration with [Zab Johnson](https://dibs.duke.edu/scholars/elizabeth-johnson)'s lab and with curator Marianne Wardle of Duke's [Nasher Museum](http://emuseum.nasher.duke.edu/), we've been doing just that. Thanks to our eye tracking glasses, we're able to let people view works in the Nasher's galleries while we track where they're looking. But unlike most lab experiments that have people look at static images, we're able to let them explore the works in the way they naturally would &mdash; approaching the work from across the room, leaning in close to study details, studying from all angles.

Yet we needed to make sure that we could still map gaze points from close up and extreme angles back to a static image of the piece of art. And this presents an additional challenge, since only a portion of the work is visible in the eye tracker's camera at any moment.

So how'd we do? An example of our technique applied to a single frame:

{% include blog_image.html url="http://people.duke.edu/~sni/mutu1.jpg" description="Wangechi Mutu, Family Tree, 2012. One of 13 mixed-media collages on paper, 14 1/8 × 10 3/16 in. (35.9 × 25.9 cm). Collection of the Nasher Museum. Museum purchase with additional funds provided by Trent Carmichael (T’88, P’17), Blake Byrne (T'57), Marjorie and Michael Levine (T’84, P’16, P’19, P’19), Stefanie and Douglas Kahn (P’11, P’13), and Christen and Derek Wilson (T'86, B'90, P'15). c Wangechi Mutu." %}

We take a match image like this one and try to find it in a video frame.

{% include blog_image.html url="http://people.duke.edu/~sni/video_frame.png" %}

We then select a box from that video frame to transform to the match image's dimensions.

{% include blog_image.html url="http://people.duke.edu/~sni/transformed.png" %}

The perspective transform is important because we also apply that same transformation to gaze location points in order to get the gaze location on the static image.

With this technique, we can now use traditional analysis methods from eye tracking to compare viewing patterns across individuals by first mapping back to the reference image. We can also begin to think about the role viewing angle and space play in these gaze patterns by using camera angles and zoom to calculate distance from the works as patrons explored.

More on this to come. In the meantime, check out the results when we apply this to a full video:

<div class="video-container">
<iframe width="730" height="410" src="https://www.youtube.com/embed/fSl6FiyHTes?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
</div>
<br>

Links to pages on the Nasher Museum site for the works included:

- [Wangechi Mutu, Family Tree, 2012](http://emuseum.nasher.duke.edu/view/objects/asitem/items$0040:18231)
- [Jeff Sonhouse, Decompositioning, 2010](http://emuseum.nasher.duke.edu/view/objects/asitem/items$0040:14671)
