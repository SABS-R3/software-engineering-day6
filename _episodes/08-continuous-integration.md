---
title: "Continuous Integration"
teaching: 60
exercises: 120
questions:
- "How can I automate a variety of tasks on a repository to make my software more robust?"
objectives:
- "Describe the benefits of using Continuous Integration for further automation of testing and other tasks"
- "Enable GitHub Actions Continuous Integration for public open source (or private) repositories"
- "Be aware of alternatives to GitHub Actions, such as Travis"
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
This afternoon you will be using GitHub Actions, which unsurprisingly is available as part of GitHub.
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

In this section, you will set up your own personal version of the SABS CI Course python project, and check that you can configure it on your own machine.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Vh-DNTvYgsY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. The repository is at [https://github.com/SABS-R3/2020-software-engineering-ci](https://github.com/SABS-R3/2020-software-engineering-ci).
1. Import (not fork) to your own GitHub account.
1. Clone your imported version locally.
1. Set up a Python3 virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
1. Install the project:
```bash
pip install --upgrade pip setuptools wheel
pip install -e .[dev,docs]
```
1. Check that the unit tests run and pass:
```bash
python -m unittest
```


## 14:30 - Getting started with GitHub Actions

With a GitHub repository there's a very easy way to set up CI that runs when your repository changes: simply add a file to your repository in the directory `.github/workflows`.
Each file in this directory will, when triggered, spin up a virtual machine and run the sequence of commands in the file.

Information about the specifications of these VMs can be found [here](https://docs.github.com/en/free-pro-team@latest/actions/reference/specifications-for-github-hosted-runners).
At the time of writing, each VM will have a 2-core CPU, 7GB of RAM and 14 GB of SSD space available, and each workflow can run for up to 6 hours.
These resources are all free for public repositories, and for private repositories you have a monthly quota of VM-minutes before any payment is required.

In this section you will create two workflows by using the wizard and built-in editor on the GitHub website.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/O-91cuGP24U" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Create a basic workflow from your repository's "Actions" tab, and verify that it runs and executes correctly.
1. Create a workflow based on the default "Python package" workflow, editing the contents as required for this project:
   - Remove the unnecessary dependency of `pytest`
   - Change `flake8` to __not__ treat errors as warnings
   - Run the tests with `python -m unittest`, rather than `pytest`
1. Check that the four runners start, and watch them fail.
1. On your machine, fix the errors that `flake8` found, and commit and push those changes. Make sure the CI now passes.
   - Remember to pull the changes you made on GitHub before commiting your fixes
1. Read the contents of the `.flake8` file in your repository. What is it doing?
1. \[optional\] read more about [GitHub's hosted runners](https://docs.github.com/en/free-pro-team@latest/actions/reference/specifications-for-github-hosted-runners).
1. \[optional\] read more about the [syntax for GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions).
1. \[optional, after completing exercises\] set up a similar workflow using [Travis CI](https://travis-ci.com/).


## 15:00 - Testing on multiple operating systems

To ensure good portability of software for all potential users, you should ideally be testing on Windows, Linux and macOS.
You can do that using GitHub Actions.

Information about the operating systems that GitHub Actions supports can be found [in their documentation](https://docs.github.com/en/free-pro-team@latest/actions/reference/specifications-for-github-hosted-runners#supported-runners-and-hardware-resources).
At the time of writing, you can access virtual machines running Windows Server 2019, Ubuntu 20.04, Ubuntu 18.04, Ubuntu 16.04, and macOS Catalina 10.15.

While not covered in this course, you can also use GitHub Actions with [Docker](https://www.docker.com/), allowing you to test on many other environments than the defaults.
You can also add [self hosted runners](https://docs.github.com/en/free-pro-team@latest/actions/hosting-your-own-runners/adding-self-hosted-runners) if you need to run your CI on specific hardware that you own, or if you need to use software (such as Matlab) that you have local licenses for.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/eIf1KxNpn68" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Remove the basic workflow file.  You don't need that any more.
1. Add a status badge to your repository's `README.md` file.
1. Create a new workflow file to test your repository on Windows, Linux and macOS. Use a build matrix with the following:
```yml
os: [windows-latest, macos-latest, ubuntu-latest]
```
1. Add a status badge for your new workflow.
1. \[optional, after completing exercises\] set up a similar workflow using [Travis CI](https://travis-ci.com/).

## 15:20 - Coffee break

Take a break!


## 15:30 Testing code coverage

Code coverage is a metric used to describe how much code in a software project is hit when the unit tests are run.
In its simplest form, this is the proportion of the lines of code that get executed when you run the unit tests.

Code coverage is no guarantee that the unit tests are any good. But, nevertheless, code coverage is an important metric for helping to assess how well tested a codebase is.

In this section, you are going to calculate the code coverage of your Python project, which you will then visualise using a third party tool called [Codecov](https://codecov.io/).
Codecov is free for public repositories.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/yc7hnL04fYs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Go to [https://codecov.io/](https://codecov.io/), log in with your GitHub account, and configure your project.
1. Copy the token, and set it as a secret in your repository, with the name `CODECOV_TOKEN`.
1. Create a new GitHub Actions workflow for running coverage.
   - You will need to add the following Python dependencies to your YAML file:
```
coverage codecov
```
   - Run coverage with the following block in your YAML file:
{% raw %}
    ```yaml
    - name: Run coverage
      run: |
        coverage run -m unittest
    ```
{% endraw %}
   - Run codecov with the following block in your YAML file:
{% raw %}
    ```yaml
    - name: Run codecov
      if: success()
      env:
        CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
      run: |
        codecov
    ```
{% endraw %}
1. Find the status badge from [https://codecov.io/](https://codecov.io/) to display in your `README.md`.
1. Add a unit test to cover the remaining line in `functionality.py`, and check that your coverage goes up to 100%.
1. Read the contents of the `.coveragerc` file in your repository. What is it doing?
1. \[optional\] Read about [branch coverage](https://coverage.readthedocs.io/en/v4.5.x/branch.html). Turn branch coverage on in your coverage workflow. Check whether you have 100% branch coverage and, if not, fix it.
1. \[optional\] Read more about [encrypted secrets](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets) in GitHub Actions.
1. \[optional\] Read more about [environment variables](https://docs.github.com/en/free-pro-team@latest/actions/reference/environment-variables) in GitHub Actions.


## 16:15 Integrating third party tools: Better Code Hub

[Better Code Hub](https://bettercodehub.com/) is a service that provides a broad overview of aspects of your software's quality. It uses a number of useful guidelines to score your software out of 10.

Better Code Hub is one of a number of services that can add to your continuous integration set up without you writing a single line of code: no workflow is necessary, you just link the service to your GitHub repository and it will watch for changes.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ZIJPVD5C0UA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Go to [https://bettercodehub.com/](https://bettercodehub.com/) and analyse your repository.
2. Read through the guidelines to get an idea of what checks are being made.
3. Add a status badge from [Better Code Hub](https://bettercodehub.com/) to your `README.md`.
4. \[optional\] Read about how you can [configure Better Code Hub](https://bettercodehub.com/docs/configuration-manual) by adding a YAML file to your repository.

## 16:30 - Coffee break

Take a break!


## 16:45 Integrating third party tools: Read the Docs

[Read the Docs](https://readthedocs.org/) is a free place to host documentation for open source software projects.
In this section you will use a tool called [Sphinx](https://www.sphinx-doc.org/en/master/) to generate documentation for your repository, and host that documentation automatically on Read the Docs.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/3kDdPtg3pwU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Create a directory called `docs` and run the `sphinx-quickstart`.
1. Edit `conf.py` to remove the empty `_static` directory from the configuration. The final line should end up as:
    ```
    html_static_path = []
    ```
1. Commit and push those files to GitHub.
1. Go to [https://readthedocs.org/](https://readthedocs.org/) and import your repository.
1. Check that it builds correctly. Find a status badge to add to your `README.md`.
1. Add a quickstart guide to your documentation. Push the changes, and check that they go live.
2. Read the contents of the `.readthedocs.yml` file in your repository. What is it doing?
3. \[optional\] Read more about [Sphinx](https://www.sphinx-doc.org/en/master/) and [Read the Docs](https://readthedocs.org/).


## Wrapping up

Continuous integration is an essential tool to improve software quality and reliability.
It drastically increases the chances of catching problems at an early stage, preventing significant effort correcting problems later once they have become entrenched.
On top of that, there are many free services that you can take advantage of for your open source projects.

I would encourage you to look at some examples of repositories using sophisticated continuous integration in production, to see what it can look like for large projects.
I would suggest looking at [PINTS](https://github.com/pints-team/pints).
If you look at any of the open pull requests, you can see each commit pushed to GitHub has a tick or a cross, telling code reviewers at a glance whether all the checks passed.

Getting a good CI pipeline set up early in a project will pay back your time investment many times over.



{% include links.md %}
