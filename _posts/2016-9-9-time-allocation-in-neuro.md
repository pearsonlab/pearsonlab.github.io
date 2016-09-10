---
layout: blogpost
title: Blog
desc: Read about our day-to-day activities
post_title: Time allocation in neuroscience research
author: John Pearson
category: blog
jscripts:
- js/time_alloc.js
jsexternals:
- https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js
- https://cdn.plot.ly/plotly-latest.min.js
---
### The Setup
A couple of weeks ago, as I was preparing to teach our incoming graduate students about data analysis, I ran across the following assertion in my notes: neuroscientists spend more time on data analysis than any other research activity.

I had zero proof for this, but it felt truthy.

So I did a little experiment. I asked my colleagues in the [Center for Cognitive Neuroscience](http://www.mind.duke.edu) and the [Department of Neurobiology](https://www.neuro.duke.edu/) to fill out a short, one-question survey:

<img src="http://www.duke.edu/~jmp33/assets/qualtrics.png" width="500">

By the way, that link is still up. If you haven't taken the survey but work in neuroscience, [go take it now](https://duke.qualtrics.com/SE/?SID=SV_4SLoFFC7fLr7j9z).

### The results:

**Indeed, data analysis is the single most time-consuming activity in the research process**

This based on about 95 responses.

As we see in the plot, the median time spent on data analysis, at 26%, just edges out data collection at 24%. It could also be noted that these are the two most variable allocations.

But there's also a lot of variability overall. My intuition is that subfields like neuroimaging require less time to gather data (but more to analyze it) than, say, molecular neuroscience.

<div id="boxplot"></div>


### Some correlations:
Even though I didn't ask respondents to report their subfields, I was curious whether the data were perhaps multimodal, suggesting clusters of responses, but the [violin plot](https://en.wikipedia.org/wiki/Violin_plot) didn't bear that out. However it's still interesting to ask how correlated the allocations were with each other:

------
<style>
th, td {
    padding: 5px;
}
tr:hover {background-color: #f5f5f5}
</style>

|| Experimental Design |Piloting|Data Collection|Data Analysis|Writing Results
 :--- | ---: | ---: | ---: | ---: | ---: | ---:
**Piloting** |0.07||||
**Data Collection** |-0.38|-0.15|||
**Data Analysis** |-0.38|-0.10|-0.23||
**Writing Results** |-0.05|-0.36|-0.44|-0.19|
**Review Process** |0.12|-0.24|-0.38|-0.38|0.36

-----

So, even though all these numbers are required to add to 1, and so we expect a negative correlation between them (roughly -14% based on a uniform Dirichlet prior with K=6), we still notice a couple of interesting features:

- There's a strong positive correlation between how long it takes you to write the results and the time spent on the review process. Are these capturing a single underlying feature &mdash; the intrinsic ambiguity of the result?
- There's a stronger than expected negative correlation between the time spent collecting and analyzing the data and the time spent designing the experiment. This may be spurious, but it suggests a "measure twice, cut once" principle may be in play: better-designed experiments theoretically should save time in the collection and analysis phases.

{% for js in page.jsexternals %}
<script type="text/javascript" src="{{ js }}"></script>
{% endfor %}
{% for js in page.jscripts %}
 <script type="text/javascript">
 {% include {{ js }} %}
 </script>
{% endfor %}
