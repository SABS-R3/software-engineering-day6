---
title: "Continuous Integration"
teaching: 60
exercises: 120
questions:
- "How can I automate a variety of tasks on a repository to make my software more robust?"
objectives:
- "Describe the benefits of using Continuous Integration for further automation of testing and other tasks"
- "Enable GitHub Actions Continuous Integration for public open source (or private) repositories"
- "Be aware of alternatives to GitHub actions, such as Travis"
- "Use GitHub Actions to automatically run unit tests with multiple Python versions"
- "Use GitHub Actions to automatically run unit tests on multiple operating systems"
- "Use GitHub Actions and Codecov to automatically run and display coverage information"
- "Integrate Better Code Hub to give general insights into software quality"
- "Integrate Sphinx and Read the Docs to automatically generate and host software documentation"
keypoints:
- "Continuous Integration covers a whole range of tools and practices that can be applied to aid good software development."
- "CI can run tests automatically to verify changes as code develops."
- "CI can run tests on different architectures and different configurations, baking portability into software."
- "CI builds are typically triggered by commits pushed to a repository."
- "Third party services can be configured to listen for changes to your repository."
- "Use of CI is essential to software quality as it removes tedious manual tasks that will not otherwise be regularly performed."
---


## What is Continuous Integration?

The automated testing we've done so far only takes into account the state of the repository we have on our own machines.
In a software project involving multiple developers working and pushing changes to a repository, it would be great to know holistically how all these changes are affecting our codebase, without everyone having to pull down all the changes and test them.
If we also take into account the testing required on different target user platforms for our software (e.g. different versions of Python, different operating systems, different compilers, ...) and the changes being made to many repository branches, the effort required to conduct testing at this scale can quickly become intractable for a research project to sustain.

Continuous Integration (CI) aims to reduce this burden by further automation, and automation - wherever possible - helps us to reduce errors and makes predictable processes more efficient.
The idea is that when a new change is committed to a repository, CI clones the repository, builds it if necessary, and performs certain tasks such as running tests, performing static analysis, or building documentation.
Once complete, it presents a report to let you see what happened.

There are many CI infrastructures and services, free and paid for, and subject to change as they evolve their features.
This afternoon we will be using GitHub Actions, which unsurprisingly is available as part of GitHub.
There are other free options, for instance [Travis CI](https://travis-ci.com/) and [AppVeyor](https://www.appveyor.com/).
All three of these make use of common features across many CI implementations, and you are certainly advised to look at the options to see some of the commonalities and differences in how features are typically provided.


## This afternoon

This will be a hands-on session where you will all set up CI for a small Python project, and see some of its benefits in action.
Each section below has a suggested start time, a brief description, a YouTube video lecture, and a list of tasks to perform after watching the video.

Don't worry if you don't keep to the suggested start times.
If you get stuck on something, please reach out to the demonstrators.
If you want to explore a particular aspect more fully, that's fine - these resources will remain online for the foreseeable future.
If you get through everything quickly and have time left at the end of the day, I would suggest that you either look at performing some of the same integrations using a different CI service, or that you investigate some of the GitHub Actions features in more depth.


## 14:10 - Getting set up with the repository

This will be a hands-on afternoon where you will all set up CI for a small Python project, and see some of its benefits in action.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Vh-DNTvYgsY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- Some instructions
- on what to do


## 14:30 - Getting started with GitHub actions

Default set up using the GitHub actions wizard to create a workflow file that tests with multiple versions of Python.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/O-91cuGP24U" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- Some instructions
- on what to do


## 15:00 - Testing on multiple operating systems

To ensure good portability between all potential users, we should be testing on Windows, Linux and macOS.
We can do that using GitHub actions.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/eIf1KxNpn68" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- Some instructions
- on what to do

## 15:15 - Coffee break

Take a break!


## 15:30 Testing code coverage

Introduction to coverage testing, why it's important, and how we can visualise the results using Codecov, for public repositories.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/yc7hnL04fYs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- Some instructions
- on what to do


## 16:15 Integrating third party tools: Better Code Hub

Better Code Hub is a service that provides a broad overview of your software's architecture, giving a useful indication of guidelines you ought to be aware of.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ZIJPVD5C0UA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- Some instructions
- on what to do


## 16:30 - Coffee break

Take a break!


## 16:45 Integrating third party tools: Read the Docs

Read the Docs is a free place to host documentation for open source software projects.
In this section we will use a tool called Sphinx to generate documentation for our Python library, and have that documentation hosted and updated automatically on Read the Docs.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/3kDdPtg3pwU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- Some instructions
- on what to do


## Wrapping up

- Some instructions
- on what to do





<!-- So far we've been manually running our tests as we require. So once we've made a change, or add a new feature with accompanying tests, we can re-run our tests, giving ourselves (and others who wish to run them) increased confidence that everything is working as expected. Now we're going to take further advantage of automation in a way that helps testing scale across a development team with very little overhead, using Continuous Integration.


## What is Continuous Integration?

The automated testing we've done so far only taking into account the state of the repository we have on our own machines. In a software project involving multiple developers working and pushing changes on a repository, it would be great to know holistically how all these changes are affecting our codebase without everyone having to pull down all the changes and test them. If we also take into account the testing required on different target user plaforms for our software and the changes being made to many repository branches, the effort required to conduct testing at this scale can quickly become intractable for a research project to sustain.

Continuous Integration (CI) aims to reduce this burden by further automation, and automation - wherever possible - helps us to reduce errors and makes predictable processes more efficient. The idea is that when a new change is committed to a repository, CI clones the repository, builds it if necessary, and runs any tests. Once complete, it presents a report to let you see what happened.

There are many CI infrastructures and services, free and paid for, and subject to change as they evolve their features. We'll be looking at two free ones, GitHub Actions - which unsurprisingly is available as part of GitHub - and a third party one called Travis. Both of these make use of common features across many CI implementations, and looking at both will illustrate some of the commonalities and differences in how such features are typically provided.


## Continuous Integration with GitHub Actions

With a GitHub repository there's a really easy way we can set up CI to run our tests when we make a change, simply by adding a new file to our repository whilst on the `test-suite` branch. First, create the new directories `.github/workflows`:
 
~~~
$ mkdir -p .github/workflows
~~~
{: .language-bash}

This directory is used specifically for GitHub Actions, allowing us to specify any number of workflows that can be run under a variety of conditions. Next, add a file called `main.yml` within that directory:

~~~
name: CI

# We can specify which GitHub events will trigger a CI build
on: [push, pull_request]

# Next we define a single job 'build', but we could add more
jobs:

  build:

    # We can also specify which operating systems we want to test on
    runs-on: ubuntu-latest

    # A job is made up of a sequence of steps
    steps:

    # Next we need to checkout out repository, and set up Python
    # A 'name' is just an optional label shown in the log - helpful to clarify progress - and can be anything
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.7

    # We can use 'run' to execute commands
    - name: Install Python dependencies
      run: |
        pip install -r requirements.txt
        pip install -e .

    - name: Test with PyTest
      run: |
        pytest --cov=inflammation.models tests/test_stats.py
~~~
{: .language-bash}

### Triggering a build on GitHub Actions

Now if we commit and push this change a CI run will be triggered:

~~~
$ git add .github
$ git commit -m "Add GitHub Actions configuration" .github
$ git push
~~~
{: .language-bash}

Since we are only committing the GitHub Actions configuration file to the `test-suite` branch for the moment, only the contents of this branch will be used for CI. We can pass this file upstream into other branches (i.e. via merges) when we're happy it works, which will then allow the process to run automatically on these other branches. This again highlights the usefulness of the feature-branch model - we can work in isolation on a feature until it's ready to be passed upstream without disrupting development on other branches, and in the case of CI, we're starting to see its scaling benefits across a larger scale development team working across potentially many branches.


### Checking build progress and reports

Handily, we can see the progress of the build from our repository on GitHub by selecting the `test-suite` branch and then selecting `commits`.

FIXME: add screenshot of branches page with build in progress

You'll see a list of commits for this branch, and likely see an orange marker next to the latest commit (clicking on it yields `Some checks haven’t completed yet`) meaning the build is still in progress. This is a useful view, as over time, it will give you a history of commits, who did them, and whether the commit resulted in a successful build or not.

Hopefully after a while, the marker will turn green indicating a successful build. Selecting it gives you even more information about the build, and selecting `Details` link takes you to a complete log of the build and its output. The logs are actually truncated; selecting the arrows next to the entries - which are the `name` labels we specified in the `main.yml` file - will expand them with more detail, including the output from the actions performed.

GitHub Actions offers these continuous integration features as a free service with 2000 Actions/minutes a month on as many public repositories that you like, although paid levels are available.


## Continuous Integration with an external CI service

Now let's take a look at Travis-CI, another free continuous integration service provided by a third-party. You'll notice many similarities between how Travis does it with GitHub Actions, but it should be pointed out that Travis did it first!

The first thing we need to do is let Travis install its GitHub App to GitHub:

1. Log into [https://travis-ci.com/]() with your GitHub account
2. Select your profile picture in the top right and select 'Activate & Migrate' under 'GitHub Apps Integration'
3. From the permissions window, select 'Only select repositories', and add the `swc-intermediate-template` repository
4. Select `Approve and install` to install the Travis application to GitHub

FIXME: add screenshot of permissions dialogue

Once we've done this, all we need to do now - whilst still on the `test-suite` branch - is add a `.travis.yml` file to the root of the repository, commit, and push it. For example:

~~~
language: python

python:
    - "3.7"

install:
    - pip install -r requirements.txt
    - pip install -e .

script:
    - pytest --cov=inflammation.models tests/test_stats.py
~~~
{: .language-bash}

Here, we are informing Travis that the software assumes a Python 3.7 environment (which will be built and provided for the CI run), and the script to execute. We already have our software dependencies in our `requirements.txt` file, and Travis will automatically use this to install these dependencies prior to running the script command.

### Triggering a build on Travis

As with GitHub Actions, we know that once a commit is pushed Travis will attempt to run a build, so if we commit and push this change a CI run will be triggered:

~~~
$ git add .travis.yml
$ git commit -m "Add Travis CI configuration" .travis.yml
$ git push
~~~
{: .language-bash}

Again, since we're only committing this to the `test-suite` branch, it will only build from that branch until we merge this file into upstream branches.

### Checking build progress and reports

The process of checking build progress is again similar to GitHub Actions, with Travis feeding back progress to GitHub - go to our repository on GitHub and select the `test-suite` branch and then `commits`. Notice that there are now *two* build indicators when you select one of the build icons, one each for GitHub Actions and Travis, that are running simultaneously. Selecting one of these gives us more details about the build, and shows it alongside details of the GitHub Actions build.

FIXME: add screenshot of Travis build log

Note that travis-ci.com also offers continuous integration as a free service, but with unlimited builds on as many open source (i.e. public) repositories that you have. But a key limitation is that only 5 concurrent build jobs may run at one time. Again, paid options are available.


## Scaling up testing using build matrices

Now we have our CI configured and building, we can use a feature called **build matrices** which really shows the value of using CI to test at scale. 

Suppose the intended users of our software use either Ubuntu, Mac OS, or Windows, and either have Python version 3.7 or 3.8 installed, and we want to support all of these. Assuming we have a suitable test suite, it would take a considerable amount of time to set up testing platforms to run our tests across all these platform combinations. Fortunately, CI can do the hard work for us very easily.

Using a build matrix we can specify testing environments and parameters (such as operating system, Python version, etc.) and new jobs will be created that run our tests for each permutation of these.

Let's see how this is done using GitHub Actions (similar support for build matrices exists in Travis). To support this, change `.github/workflow/main.yml` to the following:

~~~
...
    runs-on: {% raw %}${{ matrix.os }}{% endraw %}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: [3.7, 3.8]

    steps:

    - name: Checkout repository
      uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: {% raw %}${{ matrix.python-version }}{% endraw %}
...
~~~
{: .language-bash}

Here, we are specifying a build strategy as a matrix of operating systems and Python versions, and using `matrix.os` and `matrix.python-version` to reference these configuration possibilities instead of using hardcoded values. The `{% raw %}${{ }}{% endraw %}` are used as a means to reference these configurations.

Let's commit and push this change and see what happens:

~~~
$ git add .github/workflows/main.yml
$ git commit -m "Add GA build matrix for os and Python version" .
$ git push
~~~
{: .language-bash}

If we go to our GitHub build now, we can see that a new job has been created for each permutation. Note all jobs running in parallel (up to the limit allowed by our account) which potentially saves us a lot of time waiting for testing results. Overall, this approach allows us to massively scale our automated testing across platforms we wish to test.


## Merging back to dev

Now we're happy with our test suite, we can merge this work (which currently only exist on our `test-suite` branch) with our parent `develop` branch. Again, this reflects us working with impunity on a logical unit of work, involving multiple commits, on a separate feature branch until it's ready to be escalated to the develop branch:

~~~
$ git checkout develop
$ git merge test-suite
~~~
{: .language-bash}

Then, assuming no conflicts we can push these changes back to the remote repository as we've done before:

~~~
$ git push origin develop
~~~
{: .language-bash}

Now these changes have migrated to our parent `develop` branch, `develop` will also inherit the configuration to run CI builds, so these will run automatically on this branch as well.

This highlights a big benefit of CI when you perform merges (and apply pull requests). As new branch code is merged into upstream branches like `dev` and `master` this newly integrated code changes are automatically tested *together* with existing code - which of course may also have changed in the meantime! -->


{% include links.md %}
