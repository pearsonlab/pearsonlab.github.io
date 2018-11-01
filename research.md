---
layout: default
title: Current Projects
desc: Check out what we're working on
nav: Research
---

# How do neurons see the world?

Typical neuroscience experiments start by assuming we know the set of variables that drive neural activity. But what if neurons are tuned to variables we would never have guessed? What if, as with social interaction, the stimulus set is too complex to be boiled down to a few dimensions. With [Jeff Beck](https://www.neuro.duke.edu/research/faculty-labs/beck-lab), we're [developing models](http://arxiv.org/abs/1512.01408) that infer stimulus categories *directly from data*, allowing us to "tag" images and movies based on neural responses.
<div class="row">
    <figure>
        <img src="https://web.duke.edu/mind/level2/faculty/pearson/assets/images/website/cbp_model.svg" class="img-responsive">
        <figcaption>
            Neural responses are sums of sensitivities to binary image "tags."
        </figcaption>
    </figure>
    <br>    
    <figure>
        <img src="https://web.duke.edu/mind/level2/faculty/pearson/assets/images/website/imgclust_web.svg" class="img-responsive">
        <figcaption>
            In an example dataset, the model correctly tagged monkey faces, whole monkeys, and monkey body parts.
        </figcaption>
    </figure>
</div>

# Strategic social decision-making

Most neuroscience experiments begin by stripping away as much of the complexity of the real world as they can afford to. But when the phenomena of interest are our social interactions &mdash; who we trust, who we fight with, who we love &mdash; there's only so much complexity you can remove. In P[&lambda;]ab, we're studying the ways in which humans and other primates make strategic social decisions in *real time* by recording from the brain as pairs of individuals play dynamic games.
<div class="row">
    <figure>
        <div class="video-container">
            <iframe width="600" height="410" src="https://web.duke.edu/mind/level2/faculty/pearson/assets/videos/penaltyshot/sess130_new.mp4" frameborder="0" allowfullscreen></iframe>
        </div>
        <figcaption>
            The "penalty shot" task. The goalie (red) attempts to block the puck (blue).
        </figcaption>
    </figure>
</div>
By modeling these interactions, we're able to generate realistic samples of actual play, as well as characterize players' strategies.
<div class="row">
  <div class="col-md-4">
    <figure>
        <img src="https://web.duke.edu/mind/level2/faculty/pearson/assets/images/penaltyshot/paper_figs/real_traces.svg" class="img-responsive">
        <figcaption>
            Real puck trajectories.
        </figcaption>
    </figure>
  </div>
  <div class="col-md-4">
    <figure>
        <img src="https://web.duke.edu/mind/level2/faculty/pearson/assets/images/penaltyshot/paper_figs/gen_traces.svg" class="img-responsive">
        <figcaption>
            Generated puck trajectories.
        </figcaption>
    </figure>
  </div>
  <div class="col-md-4">
    <figure>
        <div class="video-container">
            <iframe width="600" height="410" src="https://web.duke.edu/mind/level2/faculty/pearson/assets/videos/penaltyshot/real_trial_value.mp4" frameborder="0" allowfullscreen></iframe>
        </div>
        <figcaption>
            A "potential energy" function explains player dynamics.
        </figcaption>
    </figure>
  </div>
</div>

# Work in progress: Real-time analysis of neural data

Thanks to advances in microscopy and calcium indicators, it's now possible to collect terabytes of data in a single experiment. But that increase in data volume comes at the cost of increased processing time. Yet recent work on [preprocessing algorithms](https://www.biorxiv.org/content/biorxiv/early/2018/06/05/339564.full.pdf) for imaging data, along with methods for characterizing cell responses and inferring the functional relationships between them, has made it possible to envision a *real-time* pipeline for neural data analysis.

Together with [Eva Naumann's](https://www.neuro.duke.edu/research/faculty-labs/naumann-lab) lab, we're working to develop a *fully-integrated* online analysis platform that will facilitate closed-loop, all-optical control in the larval zebrafish. This is work in progress, so stay tuned!
<div class="row">
    <figure>
        <img src="https://web.duke.edu/mind/level2/faculty/pearson/assets/images/zebrafish/colorFish.png" class="img-responsive">
        <figcaption>
            A whole zebrafish brain activity map, showing the distribution of motion-sensitive neurons, color-coded to show the preferred motion direction.
        </figcaption>
    </figure>
</div>
<div class="row">
    <figure>
        <img src="https://web.duke.edu/mind/level2/faculty/pearson/assets/images/zebrafish/pipelineNewpng3.png" class="img-responsive">
        <figcaption>
            Concept for the closed-loop pipeline. Neural data from the zebrafish are collected in the form of images, preprocessed, and analyzed in real-time. Targets for optical stimulation are then chosen based on the results of this analysis, creating adaptive experiments that test causal hypotheses.
        </figcaption>
    </figure>
</div>

# Eye tracking unplugged

Where we look speaks volumes about what we're thinking. For over a century, psychologists and neurobiologists have used the movements of the eyes and measurements of pupil size to study the mind, but the need for experimental control has limited our ability to study eye movements in naturalistic settings. In P[&lambda;]ab, we are pairing new advances in [eye tracking](http://www.tobiipro.com/product-listing/tobii-pro-glasses-2/) technology with methods in [computer vision](blog/2015/11/06/eye_tracking_tech.html) and machine learning to tackle the challenge of studying eye movements in real-world settings, with applications ranging from treatment of acute fear to how we view art.

<div class="row">
  <div class="col-md-4">
    <figure>
        <div class="video-container">
            <iframe width="730" height="410" src="https://www.youtube.com/embed/E6c9Z0Mkc-E?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
        </div>
        <figcaption>
            Mapping gaze between three and two dimensions.
        </figcaption>
    </figure>
  </div>
  <div class="col-md-4">
    <figure>
        <div class="video-container">
            <iframe width="730" height="410" src="https://www.youtube.com/embed/fSl6FiyHTes?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
        </div>
        <figcaption>
            Gaze mapping free viewing of art.
        </figcaption>
    </figure>
  </div>
  <div class="col-md-4" style="padding: 0 0 0 0">
    <figure>
        <a href="http://jeffmacinnes.com/research/gazeMapping/sonhouse3D/index.html">
            <img src="https://web.duke.edu/mind/level2/faculty/pearson/assets/images/website/dynamicGaze.png" class="img-responsive" style="margin: 7 0 7 0">
        </a>
        <figcaption>
            Three dimensional reconstruction of viewer position.
        </figcaption>
    </figure>
  </div>
</div>
