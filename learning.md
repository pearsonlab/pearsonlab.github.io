---
layout: default
title: Getting up to speed # header at the top of the page
nav: Learning # what shows up in the navbar at the top (do not define if you don't want page in the navbar)
---
# How do I get started?
I'm frequently asked by students, especially neuroscience students, how they should go about improving their {programming, computing, statistics} skills. This page is partly an answer to that. It's mostly my opinions, with no claim to being comprehensive. The wonderful upside of learning to program in the internet age is that there is so much information and so many options that you don't have to go with my recommendations.

# Contents
{:no_toc}

1. Contents seed
{:toc}


# Learning to program
## General comments
- My advice here pertains to scientific programming. If you want to learn web development or build device drivers, this may not be for you.
- [StackOverflow](https://stackoverflow.com/). If you have ever used a search engine to look up a programming question, you have probably run across StackOverflow. The site uses a question-and-answer format, with accepted answers clearly marked and the best answers upvoted. The site can be a bit intimidating to use ([there are a lot of guidelines for posting a good question](https://stackoverflow.com/help/how-to-ask)), but it's probably the best programming resource on the internet for passive search. If you're completely new to programming, it won't teach you, but for fixing well-defined problems, there's no substitute.[^sof_os]
## Choosing your first language
- Use whatever the people around you are using. It's frustrating enough to learn programming; take advantage of local expertise to help you. If you're struggling to learn functions and `if` statements, that can be done in pretty much any modern language, and the concepts will carry over to most others.
- That said, here's my order of preference:
    1. **Python**: Because everything. Python is used for scripting, building and scraping websites, and pretty much anything else where performance isn't critical. It is also the *de facto* standard in data science and machine learning. It's also comparatively easy to learn. Python is the new BASIC. What's more, Python skills actually help on a resume. I'll talk more about recommended packages/setup [below](#pydata)
    1. **Julia**: This is mostly idiosyncratic to me. As I've written [elsewhere](../blog/2016/07/13/investing-in-julia.html), I think Julia has a very bright future in scientific computing, though at the time of this writing (June 2018), it's still in development. Why Julia? Because it has the ease of use of interpreted languages like Python with a performance closer to C or FORTRAN. The downside is that the ecosystem of packages and other niceties surrounding the language is newer and thus comparatively weaker than you might find with Python or R.
    1. **R**: I use R a lot for data analysis. I use R the language only in passing. The R ecosystem is fantastic, and statisticians code, think, and publish in R. If you're using anything else, the statistical methods available to you take a big hit. Plotting and data wrangling are also top-notch. I recommend [RStudio](https://www.rstudio.com/) plus [everything](https://www.tidyverse.org/) [by](http://r4ds.had.co.nz/) [Hadley Wickham](http://adv-r.had.co.nz/).
    1. **Matlab**: If you must. Matlab is pervasive in neuroscience and engineering, and it provides a decent ecosystem (professionally supported toolboxes, a decent IDE and debugger) out of the box. Provided, that is, your institution pays the substantial price tag. My complaints about Matlab mostly center on: (a) its painful ergonomics as a programming language[^matlab_woes] (I just don't find it fun to use); and (b) its absence in the software and data science industries (Matlab skills don't mean much when applying to those jobs).

## Learning your first language
I'll be vague here for one reason: there are two many choices, and none is a clear winner. All you really want at this initial phase is an acquaintance with basic programming: variables, control flow, functions, etc.

Some people prefer books here, but in the cases of Python and R there are also lots of free video series and online courses. Which you choose doesn't matter so long as:
- You devote serious time to learning. Programming is a skill and cannot be crammed.
- You actually write code. This is a bit like learning a foreign language: you have to speak to get better. No passive learning. It really helps to have a project here, even a side project, so you have something to work toward.

## In addition
- For Python, once you've gotten a basic acquaintance with the language, and after you've worked on your [scientific programming](#pydata) skills, it's worth going back to invest in more advanced aspects of the language. This pays dividends both in understanding others' code and in writing reusable libraries of your own. For Python, I particularly recommend [Fluent Python](http://shop.oreilly.com/product/0636920032519.do).

# Python for Data Science<a name="pydata"></a>
Most programming material online is targeted at students learning their first programming language or professionals learning a new tool for app programming, web development, or some other software project. However, programming for science &mdash; writing code that runs, simulates, or analyzes experiments &mdash; carries its own set of unique challenges, and is distinct from general-purpose programming. That's why learning to program Python is distinct from learning "scientific Python," the suite of packages, tools, and practices that surround Python as used in (data) science.

This is why I make every new student in my lab read (cover-to-cover) Jake Vanderplas's [Python Data Science Handbook](http://shop.oreilly.com/product/0636920034919.do). The book covers exactly the toolset we use, including IPython, Jupyter, NumPy, SciPy, Pandas, Matplotlib, and Scikit-Learn. I don't know of a better, more comprehensive introduction to modern scientific Python.

# Statistics
**Professional disclaimer:** I recommend a good grounding in statistical theory. It's worth the investment.

But we're all busy people. What I usually end up recommending to students:
- [Data Analysis Using Regression and Multilevel/Hierarchical Models](http://www.stat.columbia.edu/~gelman/arm/). This was my first introduction to applied Bayesian analysis. Surprisingly readable for students without much statistical background and teaches an approach to modeling data that I like and advocate. As a bonus, covers Markov Chain Monte Carlo sampling tools like [Stan](http://mc-stan.org/) that are necessary in practice.
- [A First Course in Bayesian Statistical Methods](https://www.stat.washington.edu/people/pdhoff/book.php). This is the book they use for the intro Bayesian class at Duke. This is really for students who are investing in serious stats education. Finishing this one may not leave you quite ready to tackle your real data, but you will have a solid foundation to build on.
- [All of Statistics](https://www.amazon.com/All-Statistics-Statistical-Inference-Springer/dp/0387402721/ref=sr_1_1?ie=UTF8&qid=1249141007&sr=8-1). A really nice single-volume introduction to statistics. A bit of a steep learning curve for the less mathematically inclined, but worth a mention.
- For Duke students interested in the problem of actually implementing statistical models and methods in code, I highly recommend Cliburn Chan's [STA 663](https://github.com/cliburn/sta-663-2018), typically offered each spring. Teaches all the same software tools my lab uses.

# Machine Learning: Classic
There are lots of great references. The current deep learning phase notwithstanding, machine learning is actually a very broad field, and what is old now will eventually be new again. Some references worth checking out:
- [Elements of Statistical Learning](http://web.stanford.edu/~hastie/ElemStatLearn/) (free pdf)
- [Pattern Recognition and Machine Learning](https://www.springer.com/us/book/9780387310732) ([pdf](http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf))
- [Machine Learning: A Probabilistic Perspective](https://www.cs.ubc.ca/~murphyk/MLbook/) (Duke uses this for its intro ML class)

# Machine Learning: Deep Learning
So Deep Learning (aka neural networks) is eating the world. Briefly:
- Read the [Deep Learning Book](http://www.deeplearningbook.org/). It's even free online from the website. The field is moving incredibly rapidly, but this is now the standard introduction.
- For online classes, we've had students take the [Stanford convnets class](http://cs231n.stanford.edu/) and Coursera's [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning). These are pretty basic but nice for people getting started.[^online_dl_classes]
- We use [TensorFlow](https://www.tensorflow.org/) in house for a few reasons:
    - [TensorBoard](https://www.tensorflow.org/programmers_guide/summaries_and_tensorboard)
    - Support for compiling and deploying models to production. (This is a minor but important consideration for us, as we are not doing pure machine learning research. We have models we might want to deploy to others who aren't going to install TF.)
    - Educational support. TF is used as the tool of choice by Coursera's [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning), among others.
    - We had legacy [Theano](http://www.deeplearning.net/software/theano/) code to port, and Theano and TF have the same design philosophy and vocabulary.
    - In the future, TF will better support imperative programming with [eager mode](https://www.tensorflow.org/programmers_guide/eager). [Swift for TensorFlow](https://www.tensorflow.org/api_docs/swift/) is also interesting but early-stage.
- If I were a young graduate student doing ML research, I would opt for [PyTorch](https://pytorch.org/) which allows imperative programming and is thus much easier to use and debug than TensorFlow. However, TF is rapidly catching up in this area (see last point above).

# Notes


[^sof_os]: Note that information on StackOverflow tends to be proportional to the popularity of a given tool. So information on R and Python is extensive, while Matlab has comparatively less support.
[^matlab_woes]: To be fair, Matlab is now an old language and was designed to ease the burden of engineers who were coding C and FORTRAN for a living. By those standards, it is highly successful, and new features are being added to the language all the time.
[^online_dl_classes]: Keep in mind that these classes are great for learning basics, but they tend to be very light on theory and more focused on simple applications. While they're a great starting point for high school students, undergraduates, or graduate students in other fields, students interested in machine learning research will be expected to engage with these ideas at a much higher mathematical level.
