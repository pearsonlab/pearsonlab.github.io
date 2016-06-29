---
layout: blogpost
title: Blog
desc: Read about our day-to-day activities
post_title: Distributing OpenCV and FFMPEG
author: Shariq Iqbal
category: blog
---

For some of our [previous](https://pearsonlab.github.io/blog/2015/11/06/eye_tracking_tech.html) [work](https://pearsonlab.github.io/blog/2016/03/10/nasher_eye_tracking.html) on eye tracking, we needed to be able to generate videos in way that could be linked into an automated analysis pipeline. For this, we use OpenCV, a tool for advanced frame-by-frame image analysis. Unfortunately, OpenCV's ability to write movies in common output formats relies on OpenCV being linked to FFMPEG (a video codec library) and compiled manually, so you can't just install the necessary software with a package manager. The build process can be tricky, with various unique issues arising on different systems. However, with the help of modern containerization services like Docker, we can bundle a working version of OpenCV into a container and deploy it across platforms. After that, all it takes is two lines at a command prompt to get a working version up and running on any system.

Before deciding on Docker, we considered a few different options for distribution. The first idea was to simply precompile the library with links to FFMPEG enabled and distribute it as a package for Anaconda. Unfortunately, this does not work, as OpenCV has to find FFMPEG on the given system at compile time and generate links. There is no easy way to prebuild OpenCV and have it work with any FFMPEG install. Since we are building tools in-house using OpenCV and FFMPEG that we want other labs to use, it is critical that we have an easy and robust solution for distributing this toolchain. As a result, we settled on [Docker](https://www.docker.com) containers as our method for doing so.

Docker images are, in a way, lighter versions of virtual machines that allow applications to be configured and deployed on various systems. Using Docker, we only need to build OpenCV once, save it as an image, and it will be ready to be used on any system.

But while Docker is a great solution for running OpenCV with FFMPEG support on your local machine without the hassle, what if you want to run a large job in the cloud? That requires a slightly different solution: Amazon AMI's.

An AMI (Amazon Machine Image) is a snapshot of a system that you can boot up on a cloud server using Amazon's EC2 service. This is ideal for large batch processing jobs where you want to start something and forget about it until it's done. AMIs follow a build-and-save procedure similar to Docker.

So how do you get one of these solutions running?

To launch our preconfigured Docker container with OpenCV and FFMPEG:

1. [Install Docker](https://docs.docker.com/engine/installation/)
1. Run `docker pull shariqiqbal2810/opencv-conda` in a command line to pull the image to your local machine. Make sure you have around 5 GB of free hard drive space.
1. To run the image in a container, use `docker run -i -t shariqiqbal2810/opencv-conda /bin/bash`

In order to start up a server with our lab's OpenCV and FFMPEG AMI:

1. Make an Amazon Web Services account
1. Follow the instructions [here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html), making sure to use "ami-0b616161" as the AMI-ID.

And finallly, to compile OpenCV on your own with conda-build (Note: This is simply what I had to do to get it running, and I can not guarantee the same steps will work for everyone. Expect to do some troubleshooting):

1. Clone the necessary conda recipes: `git clone https://github.com/conda/conda-recipes.git` and `git clone https://github.com/menpo/conda-opencv3.git`
1. Go into the conda-recipes repository and run: `conda build x264` and `conda build ffmpeg`.
1. Switch to the conda-opencv3 directory.
1. Add the flag `-DPKG_CONFIG_PATH=${PREFIX}/lib/pkgconfig` to the `cmake` command and switch on the `-DWITH-FFMPEG` flag in conda/build.sh
1. Append your conda library directory (likely ~/anaconda/lib) to the file /etc/ld.so.conf and run the command `ldconfig`. This makes ffmpeg accessible as a shared library.
1. Run `conda build conda`
1. To install everything run `conda install --use-local ffmpeg`, `conda install --use-local x264`, and `conda install --use-local opencv3`

If everything worked correctly, you should be able to generate web-friendly H.264 encoded mp4 videos with OpenCV, like below. (Generated from Penaltykick task data, which we will have more to discuss about in the near future!)

<video width="320" height="240" controls>
  <source src="http://people.duke.edu/~sni/penaltykick_videos/sess1trial1.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
