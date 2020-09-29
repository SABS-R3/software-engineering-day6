# Intro

Hello everybody, today we are going to be looking at the topic of testing software. This 
lecture will cover the motivation behind testing, why it is important to test your code, 
and will introduce the different levels of testing that you might want to consider, from 
unit testing to end-to-end testing. It will also cover some of the terminology and 
concepts that you find in software testing, as some terms, such as fixtures and mocking, 
are quite non-obvious when you first come across them.

# Software testing in academia

Software testing is a natural part of the software development lifecycle, while you are 
first writing your code you will often, at the very least, put in little checks such as 
print, assert or if statements to ensure that a particular variable has the value you 
want in it, or that the array is the correct size. In academic code this is typically 
taken further and if, for example, the code will generate results as part of a 
publication you will add systems-level tests that are specific to that particular field 
(e.g. convergence tests for numerical modelling) in order to demonstrate correct 
behaviour for your software. 

However, it is often the case in academia that this is as far as software testing goes. 
The paper is written, the code might be forgotton, or it might be continued to be 
developed as part of another publication, or as part of the software toolkit for that 
particular research group. But the tests that were written, both the print statements, 
or the more involved convergence studies, are typically not considered part of the 
software and are either removed, or alternativly, forgotten for long enough that they 
quickly become out of date with the main codebase. 

The goals of the lesson today is to show you how to write automated tests in such a way 
that they can demonstrate correctness at both a systems-level and individual 
component-level, that can be maintained and there be useful over the entire lifecycle of 
your software, to publication and beyond.

# Why we test software

Here are a few high level reasons for why you should test your code:

The first is obviously "correctness", that your code does what you intend it to do. Note 
that this does not mean that the code is bug-free, but it does mean that you have 
written sufficiently comprehensive tests to satisfy yourself, and everyone else, that 
your code is doing what you expect it to do from one day to the next.

Another advantage of writing tests is that they can serve as a low-level specification 
or documentation of how to use the code that you have written. Each test will setup the 
environment to use the particular function or method being tested, it will call the 
function, and then verify that the output is correct, effectivly providing a small self 
contained example of how to use your code.

Writing tests also tends to be more time-efficient in the longer term. How many times 
have you worked hard to track down a bug in your code, adding print statements or 
breakpoints all throughout your code to track down and finally fixing the problem. Then, 
a week later another bug appears and once again, you spend hours tracking through your 
code, adding print statements and breakpoints again to try to find it. A good test suite 
will assist you in this process, telling you in what area you should be looking and what 
exactly is failing. It will also tell you where a bug is **not** occuring by looking at 
the tests that have passed.

Teamwork and large codebases also benifit a lot from having a good test suite. Each 
person on the team will never have a perfect knowledge of the entire project. Even the 
code you have personally written will probably fade from your memory over time. It is 
very likely that a minor change you make in a particular component  will have follow-on 
effects throughout your software, often in unexpected places. Having a comprehensive 
test suite means that it will pick up these effects and identify follow-on bugs without 
you having to be aware of them.

Finally, and most importantly, testing gives you relaxation and peace of mind. Having a 
comprehensive test suite means you can always check that your software works correctly, 
just run the tests!  Software development can be a frustratingly convoluted task, any 
codebase will only get bigger and more complex over the life of the project. Being able 
to run your tests and get a big green tick allows you to push your work, close your 
laptop, and go outside into the sunshine!


- **correctness**: the code we are currently writing is correct, does what we intend
  - put in pictues of a bunch of scientific retractions here: 
    https://github.com/softwaresaved/useful-references/blob/master/badcode.bib
- **specificiation/documentation**: tests are similar to a specification, how your code 
  *should* work. Can be useful as documentation as they show how to use your code
- **time-efficiency**: A bit more code, a lot less debugging later on (reminder: print 
  statement story)
- **teamwork**:  You never  have perfect knowlege of your entire codebase (memory, part 
  of a team, new developer). A minor change in one part of the code-base can cuase 
  errors somewhere else. A test suite will check that you are not producing unexpected 
  bugs.
- **reliability and peace of mind**: have a test suite means you can always check that 
  your software works correctly, just run the tests!  Software development can be a 
  frustratingly convoluted task, any codebase will only get bigger and more complex over 
  the life of the project. Being able to run your tests and get a big green tick allows 
  you to push your work, close your laptop, and go outside into the sunshine.


# Testing Pyramid

Now lets look at **what** you should actually be testing.

The tests that you write should aim to test the functionality of your software at a 
varietry of different *levels*, which are often depicted as a pyramid structure. The 
width of the pyramid at each level corresponds to the number of tests that you would 
typically write within that level. 

At the finest scale, the bottom of the pyramid, are the unit tests. These test each 
component of your code in isolation, where a component is a minimal software item such 
as a function or a class, or a specific behaviour of a function or class. The majority 
of your tests should be unit tests, and this has important implications on how you write 
your components, each of which should be sufficiently independent so that you can test 
each in isolation. If a component is hard to test, its probably not properly designed.

The next level can be called either functional, component, integration, or even 
interaction testing, where the aim is to write tests that verify that multiple different 
components work together correctly. This could mean that you are testing the 
communication patterns between two separate classes, or that you are testing a 
higher-level component that uses multiple lower-level components to achieve its task. 

The top level, with the least number of tests, is the system or end-to-end testing. This 
is where you are testing all the components of your library/application together. These 
types of test are closely releated to your original goals for writing the software in 
the first place. It is tempting to focus soely on this level because this is the part of 
your code that the world "sees", but should you wish to ever re-use any of the software 
that you have writen, or wish to continue editing and improving the individual 
components of your software, then it is essential that you also work at the lower levels 
of this pyramid.

The different levels shown here are in practice not distinct, and the lines between them 
are often blurred. Its not important that each test that you write is classified into a 
"unit test" or and "integration test", the important thing to take away from this 
diagram is that you should be testing your code at all these levels, not only at the 
system level or only at the unit testing level.

# Some useful testing vocabulary

There are a lot of terminology associated with software testing which might be 
unfamiliar at first. Here I'll try and cover a few of the most common terms that you 
might come across:

Component: This is a minimal software item, for example a class method, a function, or 
even a certain behaviour of a function or class, to be tested. It should represent a 
small amount of code (on the order of 10 lines of code)

Fixture: A class or function needs either a dataset to process, or a certain environment 
to run in, which must be setup before the test can run. This is known as a test fixture. 

Stubbing and Mocking: The most important feature of unit testing is that you test each 
component in isolation. This can be difficult to do, especially if your component 
depends on other components, or on some external environment. For example, you might 
have a function that needs to download a file as part of its normal operation. Stubs and 
mocks are very userful because they can act as replacements for real methods or classes, 
alleviating one of the main challenges in writing unit tests.

Coverage: This is often defined as the percentage of all possible lines of code that 
your test-suite executes. This value is often used as a metric to ensure that the tests 
"cover" a sufficient amount of the codebase. This "sufficient" threshold can vary from 
project to project, but is typically 80-99%.

Continuous Integration, or CI, is the process of integrating new software into a code 
repository. Of primary importance in CI is the automated running of all or a subset of 
the test suite, as well as other checks to verify the quality of the new code. This 
ensures that every change to the code is validated against the test suite and other 
metrics, and typically blocked from being added unless all the checks are satisfied.

Test-Driven Development: This is a style of software development where the test for a 
given component is written *before* the component itself is written. Once the tests are 
in place, the developer works on writing the component, and once the tests pass the work 
is complete. In practice, I often find it is useful to write some tests initially in 
order to verify the basic functionality of what I'm writing. I then tend to fill in the 
test behind me to make sure I've crossed all the t's and dotted the i's. 

# Not a panacea

Finally, it is worth noting that software testing is not the final solution to software 
quality and reliability.

It is very easy to get caught up in reaching 100% code coverage, at the expense of 
stoping to think about things like the quality and design of the code itself, wether the 
tests will cover all the important situations that the code must operate in, and whether 
the tests are approprate for the particular goals of your project. Remember that tests 
must be maintained as well as the rest of your code, and you don't want to be spending 
so much time writing and re-writing your tests, such that it eliminates the advantages 
of writing tests in the first place.

# The end


Ok, so this should have given you some understanding of why you should be testing your 
code, the different sorts of tests you should be thinking of writing and some basic 
terminology. After this lecture you should start going through the online material, 
which will start you off with actually writing some of your own unit tests within an 
example Python project, using a commonly used testing framework called PyTest.

