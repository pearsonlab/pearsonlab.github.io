---
layout: default
title: Current Projects
desc: Check out what we're working on
nav: Research
---

# Real-time analysis of neural data

Together with [Eva Naumann's](https://www.neuro.duke.edu/research/faculty-labs/naumann-lab) lab, we've developed *[improv](https://github.com/pearsonlab/improv)* ([paper](https://www.biorxiv.org/content/10.1101/2021.02.22.432006v1)), a software platform for designing and orchestrating adaptive experiments. By analyzing data in real time, we can measure, model, and manipulate neural activity in response to new data. We've shown how these tools, in conjunction with holographic photostimulation, could in principle map functional connectivity of large circuits in a few hours ([paper](https://proceedings.nips.cc/paper/2020/file/531d29a813ef9471aad0a5558d449a73-Paper.pdf), [expanded version](https://arxiv.org/abs/2007.13911)). More recently, we've worked on methods for fast dimensionality reduction and modeling of neural populations in real time ([paper](https://arxiv.org/abs/2108.13941)).
<div class="row">
    <figure>
        <img src="https://dibs-web01.vm.duke.edu/pearson/assets/images/zebrafish/colorFish.png" class="img-responsive">
        <figcaption>
            A whole zebrafish brain activity map, showing the distribution of motion-sensitive neurons, color-coded to show the preferred motion direction.
        </figcaption>
    </figure>
</div>
<div class="row">
    <figure>
        <img src="https://dibs-web01.vm.duke.edu/pearson/assets/images/zebrafish/pipelineNewpng3.png" class="img-responsive">
        <figcaption>
            Concept for the closed-loop pipeline. Neural data from the zebrafish are collected in the form of images, preprocessed, and analyzed in real-time. Targets for optical stimulation are then chosen based on the results of this analysis, creating adaptive experiments that test causal hypotheses.
        </figcaption>
    </figure>
</div>

# Animal vocalizations

Vocalization is a complex behavior that underlies vocal communication and vocal learning, and is important for the study of humans' underlying linguistic competency and musicality. Despite its prominence in a wide range of disciplines, vocalizations are often quantified in an ad-hoc and species-specific manner. Fortunately, recent advances in machine learning have resulted in techniques that allow high-dimensional data to be compressed in a data-dependent manner, resulting in low-dimensional encodings that minimize information loss. We use one such method, the variational Bayesian autoencoder (VAE), to perform dimensionality reduction of the vocalizations and vocal learning behavior of several model organisms: laboratory mice, zebra finches, and marmosets. Together with [Richard Mooney's lab](https://www.neuro.duke.edu/mooney-lab) we use latent representations of these species' vocal behavior to reproduce and extend existing results in a species-agnostic manner, offering a unified view of vocal variability and learning on timescales ranging from individual syllables of millisecond duration to across days ([paper](https://elifesciences.org/articles/67855), [paper](https://elifesciences.org/articles/63493)).

<div class="row">
    <figure>
        <img src="https://dibs-web01.vm.duke.edu/pearson/assets/images/vocal/vae_finch.png" class="img-responsive">
        <figcaption>
            a. Syllable VAE: Segmented syllables from adult Zebra Finch song are projected to a low-dimensional space, then reconstructed from that space using a VAE. b. Shotgun VAE: The VAE is trained on 20ms segments of adult Zebra Finch song to model variability on a millisecond duration. Visualized are songs projected into the latent space using these shorter segments.
        </figcaption>
    </figure>
</div>

# Efficient coding in the retina
How does the retina, which receives roughly one gigabit per second of visual information, compress that into something small enough to transmit down an optic nerve with a capacity of one megabit per second &mdash; three orders of magnitude lower? One answer, proposed by Horace Barlow half a century ago, is that the nervous system attempts to minimize redundancy, maximizing mutual information between the world and the brain's representation of it while minimizing metabolic costs. This theory makes a number of testable predictions, including the well-known fact that retinal ganglion cells should be active only in response to either increases or decreases in light levels at within small regions of visual space &mdash; their receptive fields.

Working together with [Greg Field's lab](https://www.neuro.duke.edu/research/faculty-labs/field-lab), we've shown that patterns of alignment between different collections of receptive fields can also be explained using efficient coding theory. This was based on findings from Field lab ([paper](https://www.nature.com/articles/s41586-021-03317-5)), which led to surprising further theoretical results ([paper](https://www.nature.com/articles/s41586-021-03317-5)). In short, the most information-efficient receptive field arrangements are determined both by levels of noise in the system and the statistics of natural images. 

Most recently, we've looked at what happens to mosaics as the number of neurons available for coding changes. There, [we found](https://www.biorxiv.org/content/10.1101/2022.08.29.505726v2) that greater numbers of available neurons leads to greater diversity in functionally defined cell types, starting with small temporally smoothing receptive fields and progressing toward larger temporally "differentiating" receptive fields.

# Autoencoding whole-brain dynamics
Brain functional magnetic imaging data (fMRI) is one of the most popular modalities in human and clinical neuroscience as it allows researchers to investigate relationships between high-level cognitive functions, brain activity patterns and experimental variables of interest. Traditional fMRI analysis methods utilize a mass univariate approach, wherein a General Linear Model (GLM) is fit to each small volume pixel ("voxel") independently and researchers correct for an inflated false positive rate post hoc. This method has been widely adopted due to its simplicity and ability to produce separate spatial brain maps, capturing the inferred effects of experimental variables on brain-wide activity. However, it fails to account for the rich spatial and temporal information inherent to this modality.
In recent work, we've explored the idea of using variational autoencoder (VAE) methods nested inside a Generalized Additive Modeling (GAM) framework to model entire brain volumes together ([paper](https://static1.squarespace.com/static/59d5ac1780bd5ef9c396eda6/t/61080b1bcadb042a79974faf)). This approach better accounts for the spatial dependencies of fMRI data and generates separate, interpretable spatial maps capturing the inferred effects of experimental variables on whole-brain dynamics. In collaboration with [Kevin LaBar's lab](http://www.labarlab.com), we're working to expand on this work with the goal of characterizing brain spatio-temporal dynamics underlying transitions between emotional states in health and in disease.

<div class="row">
    <figure>
        <img src="https://dibs-web01.vm.duke.edu/pearson/assets/images/fmri/website_VAEGAM_fig.png" class="img-responsive">
        <figcaption>
            A) VAE-GAM Model Schematic: brain volumes with signal of interest are compressed to a lower dimensional representation using encoder network. Sampled latents are then fed through decoder network to yield a base map and separate spatial effect maps. Each effect map is scaled by a potentially non-linear gain modelled using a Gaussian Process. Variance is modeled separately on a per voxel basis. B) Sample Effect Maps for VAE-GAM and GLM: effect maps for a visual stimulation task dataset analysed using the proposed VAE-GAM approach (top) vs. the tranditional (GLM) approach. 
        </figcaption>
    </figure>
</div>
