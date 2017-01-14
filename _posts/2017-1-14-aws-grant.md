---
layout: blogpost
title: Blog
desc: Read about our day-to-day activities
post_title: New funding from Amazon
author: John Pearson
category: blog
---
We just got word yesterday that P[&lambda;]ab has received a grant through Amazon's [Cloud Credits for Research](https://aws.amazon.com/research-credits/) program to further our work on large-scale analysis of electrocorticography (ECoG) data.

In collaboration with Duke neurologists and neurosurgeons, we've been collecting data from patients in the epilepsy monitoring unit at Duke Hospital. As part of their treatment, these patients have on the order of 100 separate sensors placed directly onto the surface of the brain to record neural activity. Data from these sensors are used to help surgeons better locate the brain tissue generating seizures and remove it without damaging speech or fine motor control.

Our goal is to use that same data to examine changes in communication between brain regions over long time scales, from seconds to minutes to hours. We use Amazon Web Services as a platform for storing our (deidentified) data and performing large-scale analysis using tools like [Spark](http://spark.apache.org/) and [Thunder](http://thunder-project.org/).

Thanks again to Amazon and all the patient volunteers who make this work possible.
