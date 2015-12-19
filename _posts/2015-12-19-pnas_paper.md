---
layout: blogpost
title: Blog
desc: Read about our day-to-day activities
post_title: New paper on social decision-making in PNAS
author: John Pearson
category: blog
---

This week, new work from the P[&lambda;]ab investigating neural mechanisms underlying social decisions went live (open access) on [PNAS](http://www.pnas.org/content/early/2015/12/09/1514761112.abstract). This work, led by the [Chang](http://changlab.net/) and [Platt](http://www.upenn.edu/pennnews/news/michael-platt-appointed-penn-integrates-knowledge-professor) labs, builds on a series of elegant experiments Steve Chang began when he and John were postdocs together in Platt Lab at Duke. In this most recent paper, we report that single neurons in the [amygdala](https://en.wikipedia.org/wiki/Amygdala) respond differently depending on who benefits from rewarding outcomes, and that administering the chemical [oxytocin](https://en.wikipedia.org/wiki/Oxytocin), which plays a role in birth and bonding, altered the decisions animals made when choosing between rewards to themselves alone or themselves and a partner (they got more generous).

John's contribution to the paper was on the data analysis and modeling end. One of the difficulties of analyzing datasets collected in experiments like these is that very rarely do two neurons respond to a stimulus in exactly the same way. Instead, much like people, neurons tend to have a range of responses to a given stimulus, and this diversity is often ignored. And the situation gets even more complicated when neurons respond in different ways to different types of stimuli.

So what we did was use a tool from the statistics literature called mixed effects or hierarchical modeling (see [here](http://www.amazon.com/Analysis-Regression-Multilevel-Hierarchical-Models/dp/052168689X/) for John's favorite introduction). These models correctly treat uncertainty across both individual nerve cells and the population, and are easy to build with modeling tools like [Stan](http://mc-stan.org/). To the best of John's knowledge, this is one of the first times that this kind of analysis has been used to derive honest *population effects* in a study of individual neurons.

Finally, for those who want all the gory details (as well as links to the raw data for their own exploration), those are available on [GitHub](https://github.com/jmxpearson/chang_et_al_2015/blob/master/README.md).
