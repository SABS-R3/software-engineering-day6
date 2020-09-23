# Intro

Today we are going to be looking at the topic of testing software. This lecture will 
cover the motivation behind testing, why it is important to test your code, and will 
introduce the different levels of testing that you might want to consider, from unit 
testing to end-to-end testing. It will also cover some of the terminology and concepts 
that you find in software testing, as some terms, such as fixtures and mocking, are 
quite non-obvious when you first come across them.

# Why we test software

Here are a few high level reasons for why you should test your code:

The first is obviously "correctness", that your code does what you intend it to do. Note 
that this does not mean that the code is bug-free, but it does mean that you have 
written sufficiently comprehensive tests so that you have minimise the chances of 
meaningful bugs in your code (i.e. bugs that will significantly change the results), and 
that you have done so in a way that the tests can be performed automatically, giving 
you, and anyone else, confidence that your code is working from one day to the next.

Another advantage of writing tests is that they can serve as a low-level specification 
or documentation of how to use the code that you have written. Each test will setup the 
environment to use the particular function or method being tested, it will call the 
function, and then verify that the output is correct, effectivly providing a small self 
contained example of how to use your code.

Writing tests also tends to be more time-efficient in the longer term. How many times 
have you sprinkled a bunch of `print` statements throughout your code to debug a bit of 
code. Then, you then fix the bug and delete the `print` statements. A week later another 
bug appears and once again, you put in a whole bunch of print statements to try to track 
down where exactly the new bug is occuring. A good testing suite will tell you 
immediately where a bug might be occuring by simply looking at the tests that have 
failed. And it will tell you where a bug is **not** occuring by looking at the passing 
tests.

Teamwork and large codebases also benifit from having a good test suite. Each person on 
the team will never have a perfect knowledge of the entire project. Even the code you 
have personally written will probably fade from your memory over time. It is very likely 
that a minor change you make in a particular component  will have follow-on effects on 
other components. Having a comprehensive test suite means that it will pick up these 
effects and follow-on bugs without you having to be aware of them.

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
it in isolation. If a component is hard to test, its not properly designed.
(https://cppcast.com/testing-oleg-rabaev/).

The next level can be called functional, component, integration, or even interaction 
testing, where the aim is to write tests that verify that multiple different components 
work together correctly. This could mean that you are testing the communication patterns 
between two separate classes, or that you are testing a higher-level component that uses 
multiple lower-level components to achieve its task. 

The top level, with the least number of tests, is the system or end-to-end testing. This 
is where you are testing all the components of your library/application together. These 
types of test are closely releated to your original goals for writing the software in 
the first place. It is tempting to focus soely on this level for your testing because 
this is the part of your code that the world "sees",  but should you wish to ever re-use 
any of the software that you have writen, or wish to continue editing and improving the 
individual components of your software, then it is essential to also work at the lower 
levels of the pyramid.

The different levels of the pyramid are in practice not distinct, and the lines between 
them are often blurred. Its not important that each test that you write is classified 
into a "unit test" or and "integration test", the important thing to take away from this 
diagram is that you should be testing your code at all these levels, not only at the 
system level or only at the unit testing level.

# Some useful testing vocabulary

There are a lot of terminology associated with software testing, here are a few of the 
more common that your might come across:

Component: This is a minimal software item, for example a class method, a function, or 
even a certain behaviour of a function or class, to be tested. It should represent a 
small amount of code (on the order of 10 lines of code)

Fixture: A class or function needs either a dataset to process,  or a certain 
environment to run in, which must be setup before the test can run. This is known as a 
test fixture. 

Stubbing and Mocking: The important feature of unit testing is that you test each 
component in isolation. This can be difficult to do, especially if your component 
depends on other components, or on some external environment, to operate. For example, 
if you have a class that needs to download a file from a given url. Stubs and mocks are 
stand-ins for real methods or classes so that you can test one component in isolution, 
and in an environment that you can reliably control. There are many mocking libraries 
for different languages, for example the 
[`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html) library for 
Python.

Coverage: Proportion of all possible lines of code that your whole test-suite executes. 
This value is often used as a metric to ensure that the tests "cover" a sufficient 
amount of the codebase. This sufficient threshold can vary from project to project, but 
is typically 90-99%.

Decision/Branch/Edge coverage: There are many definitions of coverage, and the one given 
previously is the most commonly used because it is relativly easy to satisfy. Truely 
exhaustive testing of your code would need to test all the possible combination of 
control flow paths through your program. For example, if you program consisted of 3 
sequential if statements you would need to test all 8 possible routes through the 
program. This is generally unfeasable to do for any practical codebase, so is rarely 
used.

Continuous Integration, or CI, is the process of integrating new software into a code 
repository. Of pimary importance in CI is the automated running of all or a subset of 
the test suite, as well as other checks to verify the quality of the new code. This 
ensures that every change to the code is validated against the test suite and other 
metrics, and blocked from being added unless all the checks are satisfied.

Test-Driven Development: This is a style of software development where the test for a 
given component is written *before* the component itself is written. Once the tests are 
in place, the developer works on writing the component, and once the tests pass the work 
is complete. 


# Not a panacea

Finally, it is worth noting that software testing is not the final solution to software 
quality and reliability. Steve McConnell, author of Code Complete, has this to say about 
testing:

"Trying to improve the quality of software by doing more testing is like trying to lose 
weight by weighing yourself more often."

It is easy to get caught up in reaching 100% code coverage, at the expense of stoping to 
think about things like the quality and design of the code itself, wether the tests will 
cover all the important situations that the code must operate in, and whether the tests 
are approprate for the particular goals of the project. 

