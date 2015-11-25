---
layout: blogpost
title: Blog
desc: Read about our day-to-day activities
post_title: ECT Research Featured in The Atlantic
author: Shariq Iqbal
category: blog
---

The Atlantic recently did a cool [feature](http://www.theatlantic.com/magazine/archive/2015/12/the-return-of-electroshock-therapy/413179/) on Dr. Sarah (Holly) Lisanby that highlights some of the work she has done over the course of her career regarding ECT (Electro-Convulsive Therapy).  The article is really well done, and I would recommend checking it out.  As with anything on the internet though, avoid the comments. 

Dr. Lisanby is the P.I. on a study concerning the effectiveness of ECT in depressed elders that we have been doing some analysis for over the past couple of months.  The goal of our analysis is to be able to predict outcomes (most importantly, remission status), from the rest of the data. The data set has been collected across seven hospitals and consists of hundreds of separate treatments of over one hundred patients. For a clinical data set, this is pretty large-scale, but, as with any clinical data, there are certain limitations.

For one, some of the fields contain numerous missing values, but our analyses can't use them. As a result, we have drop missing values while balancing between keeping as many different variables in the data and keeping as many subjects as possible. Luckily the pandas library in Python allows for easy management of missing values along with compatibility with the modeling package we use for basic regression and classification, scikit-learn.

We're most interested in predicting variables like remission status, as well as scores from cognitive tasks like the [Stroop Test](https://en.wikipedia.org/wiki/Stroop_effect) that are measured in the study. The models that we run are capable of finding complex relationships between our data and our target variables, and they can greatly improve the accuracy of prediction when used correctly. The key however, is using them correctly. These models can just as easily pick up on false signal in the data that is not useful.  For example, a model may rely on a variable that records how responsive a subject is to their last treatment to predict remission status, but we do not know the result of last treatment at the time that we want to predict whether the treatment will be effective. As a result, including such variables in our model, which we can't actually use for predictive purposes, is not particularly useful.

There are many challenges when it comes to predictive modeling on a clinical data set, but we are optimistic that we will be able to find insights that can benefit the use of ECT in the future!