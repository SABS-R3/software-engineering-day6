---
title: "Diagnosing Issues and Improving Robustness"
teaching: 30
exercises: 15
questions:
- "Once we know our program has errors, how can we identify where they are?"
- "How can we make our programs more resilient to failure?"
objectives:
- "Use a debugger to explore behaviour of a running program"
- "Describe and identify edge and corner test cases and explain why they are important"
- "Apply error handling and defensive programming techniques to improve robustness of a program"
keypoints:
- "Unit testing is good to show us what doesn't work, but does not help us locate problems."
- "We can use a **debugger** to help us locate problems in our program."
- "A debugger allows us to pause a program and examine it's state by adding **breakpoints** to lines in code."
- "We can use **preconditions**, **postconditions* and **invariants** to ensure correct behaviour in our programs."
- "We must ensure our unit tests cater for **edge** and **corner cases** sufficiently."
---

## Finding faults in software

Unit testing can tell us something's wrong and give a rough idea of where the error is 
by what test(s) are failing. But it doesn't tell us exactly where the problem is (i.e. 
what line), or how it came about. We can do things like output program state at various 
points, perhaps using print statements to output the contents of variables, maybe even 
use a logging capability to output the state of everything as the program progresses, or 
look at intermediately generated files to give us an idea of what went wrong.

But such approaches only go so far and often these are time consuming and aren't enough. In complex programs like simulation codes, sometimes we need to get inside the code as it's running and explore. This is where using a **debugger** can be useful.

## Normalising patient data

We wish to add a new function to our inflammation example, one that will normalise a 
given inflammation data array so that all the entries lie between 0 and 1.

Add a new function to `model.py` called `patient_normalise()`, and copy the following 
code:

~~~
def patient_normalise(data):
    """Normalise patient data between 0 and 1 of a 2D inflammation data array."""
    max = np.max(data, axis=0)
    return data / max[:, np.newaxis]
~~~
{: .language-python}

So here we're attempting to normalise each patient's inflammation data by the maximum 
inflammation experienced by that patient, so that the final values are between 0 and 1. 
We find the maximum value for a patient, and using NumPy's elementwise division, divide 
each value by that maximum. In order to prevent an unwanted feature of NumPy called 
broadcasting, we need to add a blank axis to our array of patient maximums. Note there 
is also an assumption in this calculation that the minimum value we want is always zero. 
This is a sensible assumption for this particular application, since the zero value is a 
special case indicating that a patient experiences no inflammation on that day.

Now add a new test in `tests/test_models.py`, to check that the normalisation function 
is correct for some test data.

~~~
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.66, 1], [0.66, 0.83, 1], [0.77, 0.88, 1]])
    ])
def test_patient_normalise(test, expected):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    npt.assert_almost_equal(np.array(expected), patient_normalise(np.array(test)), decimal=2)
~~~
{: .language-python}

Note the assumption here that a test accuracy of two decimal places is sufficient!

Run the tests again using `pytest tests/test_model.py` and you will note that the new 
test is failing, with an error message that doesn't give many clues as to what is wrong

~~~
E       AssertionError:
E       Arrays are not almost equal to 2 decimals
E
E       Mismatched elements: 6 / 9 (66.7%)
E       Max absolute difference: 0.57142857
E       Max relative difference: 1.33333333
E        x: array([[0.33, 0.66, 1.  ],
E              [0.66, 0.83, 1.  ],
E              [0.77, 0.88, 1.  ]])
E        y: array([[0.14, 0.29, 0.43],
E              [0.5 , 0.62, 0.75],
E              [0.78, 0.89, 1.  ]])

tests/test_models.py:53: AssertionError
~~~
{: .output}

## Pytest and debugging in VSCode

Let's use a debugger to see what's going on and why the function failed. Think of it like performing exploratory surgery - on code! Debuggers allow us to peer at the internal workings of a program, such as variables and other state, as it performs its functions.

First we will setup VSCode to run and debug our tests. If you havn't done so already, 
you will first need to enable the PyTest framework in VSCode. You can do this by 
selecting the `Python: Configure Tests` command in the Command Palette (Ctrl+Shift+P). 
This will then prompt you to select a test framework (`Pytest`), and a directory 
containing the tests (`tests`). You should then see the Test view, shown as a beaker, in 
the left hand activity sidebar. Select this and you should see the list of tests, along 
with our new test `test_patient_normalise`. If you select this test you should see some 
icons to the right that either run, debug or open the `test_patient_normalise` test. You 
can see what this looks like in the screenshot below.


![Patient normalise tests in VSCode](/fig/testsInVSCode.jpg)

Click on the "run" button next to `test_patient_normalise`, and you will be able to see 
that VSCode runs the function, and the same `AssertionError` that we say before. 

Now we want to use the debugger to investigate what is happening inside the 
`patient_normalise` function. To do this we will add a *breakpoint* in the code. 
Navigate to the `models.py` file and move you mouse to the return statement of the 
`patient_normalise` function. Click to the left of the line number for that line and a 
small red dot will appear, indicating that you have placed a breakpoint on that line. 
Now if you debug `test_patient_normalise`, you will notice that execution will be paused 
at the return statement of `patient_normalise`, and we can investigate the exact state 
of the program at it is executing this line of code. Navigate to the Run view, and you 
will be able to see the local and global variables currently in memory, the call stack 
(i.e. what functions are currently running), and the current list of breakpoints. In the 
local variables section you will be able to see the `data` array that is input to the 
`patient_normalise` function, as well as the `max` local array that was created to hold 
the maximum inflammation values for each patient. See below for a screenshot.

![Debugging function in VSCode](/fig/debugInVSCode.jpg)

In the Watch section of the Run view you can write any expression you want the debugger 
to calculate, this is useful if you want to view a particular combination of variables, 
or perhaps a single element or slice of an array. Try putting in the expression `max[:, 
np.newaxis]` into the Watch section, and you will be able to see the column vector that 
we are dividing `data` by in the return line of the function. You can also open the 
Debug Console and type in `max[:, np.newaxis]` to see the same result.

Looking at the `max` variable, we can see that something looks wrong, as the maximum 
values for each patient do no correspond to the `data` array. Recall that the input 
`data` array we are using for the function is

~~~
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
~~~
{: .language-python}

so the maximum inflammation for each patient should be `[3, 6, 9]`, whereas the debugger 
shows `[7, 8, 9]`. You can see that the latter corresponds exactly to the last column of 
`data`, and we can immediately conclude that we took the maximum along the wrong axis of 
`data`. So to fix the function we can change `axis=0` in the first line to `axis=1`. 
With this fix in place, running the tests again will result in a passing test, and a 
nice green tick next to the test in the VSCode IDE.

## Corner or Edge Cases



FIXME: importance of corner/edge cases. Externalising your cognition/understanding about 
your code into tests. Insufficiency of our current tests. Add 0 and 1 tests:

~~~
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.66, 1], [0.66, 0.83, 1], [0.77, 0.88, 1]])
    ])
~~~
{: .language-python}

FIXME: 0's fail due to nan's (division by zero). How do we deal with this?

~~~
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
~~~
{: .language-python}

> ## Exploring tests for edge cases
>
> Think of some more suitable edge cases to test our `patient_normalise()` function and add them to the parametrised tests.
>
> > ## Solution
> > ~~~
> > ...
> > 
> > ...
> > ~~~
> > 
> > This one has forced me to think about whether this is behaviour I want to allow or not.
> > {: .language-python}
> {: .solution}
>
{: .challenge}

FIXME: show debugger with more complex example, stepping through code. Step over, step into. Resume program

FIXME: add something about debugging on command line?


## Defensive programming to avoid potential errors


FIXME: preconditions (protect your functions from bad data. This adheres to fail fast), postconditions (does out output make sense), invariants (these things should never happen, or should always be true). Don't take it too far and try to code for every conceivable eventuality. State the assumptions and limitations of your code for others. Where possible codify your assumptions

FIXME: add precondition of no values below zero (as per assumption), add assert postconditions of no values below 0 or above 1


## What about the other failed test?

FIXME: introduce TDD for next lesson



{% include links.md %}
