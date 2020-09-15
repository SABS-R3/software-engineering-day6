# Intro

Today we are going to be looking at the topic of testing software. This covers basic 
testsing to check the correctness of a function or class, the tools that you can use to 
test Python code in particular, and how you integrate the testing process into an 
on-going software project that might involve just yourself, or a team of developers.

This lecture will cover the motivation behind testing, why it is important to test your 
code, and will introduce the different levels of testing that you might want to 
consider, from unit testing to end-to-end testing. It will also cover some of the 
terminology and concepts that you find in software testing, as some terms, such as 
fixtures and mocking, are quite non-obvious when you first come across them.

# Software testing in academia and industry

Software testing is a natural part of the software development lifecycle, while you are 
first writing your code you will often, at the very least, put in little checks such as 
print, assert or if statements to ensure that a particular variable has the value you 
want in it, or that the array is the correct size. In academic code this is typically 
taken further and if, for example, the code will generate results as part of a 
publication there are usually tests speific to the particular scientific field (e.g. 
convergence tests for numerical modelling) that are implemented and run to ensure the 
correct behaviour for the software. 

However, it is often the case in academia that this is as far as software testing goes. 
The paper is written, the code might be forgotton, or it might be continued to be 
developed as part of another publication, or as part of the software for that particular 
research group. But the tests that were written, both the very small print statements, 
or the more involved convergence studies, are typically not considered part of the 
software and are either removed, or forgotten for long enough that they quickly become 
out of date with the main codebase. 

An example of this, that has recently been highlighted in the UK due to the recent 
pandemic, is the COVID-19 microsimulation model developed by the MRC Centre for Global 
Infectious Disease Analysis at Imperial College in London. This is fairly old codebase 
that has been under development for the past decade, led by Professor Neil Ferguson. It 
is a large, relativly monolithic piece of software written in C, and by its nature its 
outputs are stochastic, making it quite difficult to test. Ferguson and his team have 
written a number of papers using the results of this code, at least four of which are 
listed on the published GitHub repository. These papers were, it is assumed, thoughorly 
peer reviewed, and there is absolutly no indication that the results produced by the 
covid-sim software were incorrect. On the contrairy, Professor Ferguson has had a long 
career in mathematical biology modelling and I am confident that he and his team 
rigerously verified the outputs of the software before each and every publication. 


https://github.com/mrc-ide/covid-sim/issues/181
https://github.com/mrc-ide/covid-sim/issues/165
https://github.com/mrc-ide/covid-sim/issues/166

However, when the covid-sim software was released to the public in May 2020, it came 
under quite a lot of criticism by software developers. This criticism mainly focused on 
the lack of testing, particularly detailed unit testing, in the repository. Unit testing 
focuses on detailed testing at the component level, testing individual functions and 
methods for correctness, and in industrial software development unit tests would be the 
bulk of any good test suite. In contrast, the covid-sim software only had a few 
regression tests, which test that the output of the software does not change over time, 
and which were added prior to release by an industry software engineer (from GitHub). 
The criticism that covid-sim received was probably quite unfair, as it neglects the 
substantial time that the academics put into verifying that the output of the software 
was correct prior to publication, and the peer review process itself. However, it serves 
to highlight the key difference between software testing in both academic and industry, 
with testing in industry focussed mainly on comprehensive, detailed, and most 
importantily continual testing of individual components and the interaction between 
them, whereas the focus in academia is on manual, labour intensive demonstration of 
system-level correctness at a single point in time (i.e. publication time). 
Unfortunately, while the academic strategy works well for generating plots for 
publication, it results in software that is unlikely to work in any other context than 
the original publication. It is also a collosal waste of time for those that developed 
the software. Testing is a complex and laborious task, and a useful rule of thumb is 
that you should have about as much testing code as you have actual functional code. 
However, in academia the work that goes into testing is effectvly thrown away soon after 
publication, leaving you with a complex, untested codebase that quickly becomes 
unmaintainable over time.

# Why we test software

Here are a few high level reasons as to why you should test your code:

The first and most obvious reason is "correctness", that your code does what you intend 
it to do. Note that this does not mean that the code is bug-free, but it does mean that 
you have written sufficiently comprehensive tests so that you have minimise the chances 
of meaningful bugs in your code (i.e. bugs that will significantly change the results), 
and that you have done so in a way that the tests can be performed automatically, giving 
you, and anyone else, confidence that your code is working one day to the next.

Another advantage of writing tests is that they can serve as a very low-level 
specification or documentation of how to use your code. Each test will setup the 
environment to use the particular function or method being tested, it will call the 
function, and then will verify that the output is what is expected. In fact, this is 
related to a particular style of software development known as Test-Driven Development, 
where you first write the test for a given component *before* you write the component 
itself. In this way the test acts as the spec for the component, then you write the 
component against that spec, that is, untill it passes the test.

One of the more important reasons for writing tests is that it is time-efficient. How 
many times have you sprinkled a bunch of `print` statements throughout your code to 
debug a bit of code, you then fix the bug and delete the `print` statements. Then, a 
week later another bug appears and you, once again, put in a whole bunch of print 
statements to try to track down where exactly the bug is occuring. A good testing suite 
will tell you immediately where a bug might be occuring by simply looking at the tests 
that have failed. And it will tell you where a bug is **not** occuring by looking at the 
passing tests. And once you have found the bug, you can then add a new test targeting 
that particular bug, allowing you to immmediately detect if it ever occurs again.

Writing tests is particularly important for software projects where you are working as 
part of a team. Each person will never have a perfect knowledge of the entire codebase 
as differnt parts were developed by different people. Even the code you have personally 
written will probably fade from your memory over time. It is very likely that a minor 
change you make in a component A will have follow-on effects on the other components B, 
C and D of the software, and a tests suite that tests all these different components 
together will pick up these effects without you having to be aware of them.

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


# Importance of automating testing

I've mentioned a few times already about the importance of automating your tests, and 
I'd like to repeat this again because its an important point. Software development 
(unlike publication) is an on-going, dynamic process, usually involving multiple 
software developers working on overlapping functionality. The particular software 
package that you are writing on often depends on multiple third-party libraries (and 
operating systems!) that are also changing over time. This flux of code both internal 
and external to your project naturally creates bugs in your code, from catestrophic 
failures to small, suble changes to the behaviour of your software. These changes over 
time must be detected as soon as they occur if you are to be confident in the 
reliability of your code from one day to the next. 

A comprehensive test suite that is run automatically following any addition to the 
codebase allows for the immediate the detection of introduced bugs, and this is an 
important part of what is known as *continuous integration* (CI). Most software 
repository platforms (such as GitHub) have in-built facilities or third-party services, 
that enable developers to setup continuous integration, which includes automated 
testing, on every commit or pull request that is added to the repo.

# Testing Pyramid

So now lets move beyond the motivations for testing and look at **what** you should 
actually be testing.

The tests that you write should aim to test the functionality of your software at a 
varietry of different *levels*. These levels are often depicted as a pyramid, where the 
width of the pyramid at each level corresponding to the number of tests that you would 
typically write within each scale. The different levels of the pyramid are in practice 
not distinct, and the lines between them are often blurred. Its not important that each 
test that you write is classified into a "unit test" or and "integration test", the 
important thing to take away from this diagram is that you should be testing your code 
at all these levels, not only at the system level or only at the unit testing level.

At the finest scale, the bottom of the pyramid, are the unit tests. These test each 
component of your code in isolation, where a component is a minimal software item such 
as a function or a class, or a specific behaviour of a function or class. The majority 
of your tests should be unit tests, and this has important implications on how you write 
your components, each of which should be sufficiently independent so that you can test 
it in isolation. If a component is hard to test, its not properly designed 
(https://cppcast.com/testing-oleg-rabaev/).

The next level can be called component, integration, or even interaction testing, where 
the aim is to write tests that verify that multiple different components work together 
and interact correctly. This might mean that you are testing the communication patterns 
between two separate classes, or that you are testing a higher-level component that uses 
multiple lower-level components to achieve its task. 

The top level, with the least number of tests, is the system or end-to-end testing. This 
is where you are testing all the components of your library/application together. So if 
you were writing a

Level of test	Area covered by test
Unit testing	smallest logical block of work (often < 10 lines of code)
Component/Integration testing	several logical blocks of work together
System/End-to-end testing	all components together / whole program

# Some useful testing vocabulary

fixture: input data to a test
component: a minimal software item (class, function) to be tested
expected result: the output that should be obtained
actual result: the output that is obtained
coverage: proportion of all possible paths in the code that the tests take
Branch coverage: branches give rise to an exponentially growing number of possible paths 
through your code, how many of these are tested?
if energy > 0:
    ! Do this 
else:
    ! Do that
Is there a test for both energy > 0 and energy <= 0?
continuous integration: the process of integrating new software into a code repository. 
Of pimary importance in CI is the automated running of all or a subset of the test 
suite, as well as other checks to verify the quality of the new code
stubbing and mocking: very handy for unit tests. Stubs and mocks are stand-ins for real 
methods or classes so that you can test one class/method *in isolation*



# Not a panacea
Trying to improve the quality of software by doing more testing is like trying to lose weight by weighting yourself more often.

- Steve McConnell
Testing won't corrrect a buggy code
Testing will tell you were the bugs are...
... if the test cases cover the bugs
