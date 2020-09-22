---
title: "Mocking for Unit Testing"
teaching: 30
exercises: 10
questions:
- "How can we test components in isolation that depend on an external environment or 
  other components?"
objectives:
- "Describe how to use unittest.mock to replace either a remote call or a dependent 
  function"
- "Use mocking to complete the test suite for our inflammation example"
keypoints:
- "Mocking is useful for implementing unit tests that test each component in isolation."
- "Mocking can remove dependencies on external environment such as the internet, the 
  filesystem, or it can remove dependencies from other components"
- "Testing in isolation is essential as it gives you a test suite that can properly 
  identify where bugs are occuring"
---

Mocking is a testing term that means to replace a real object with a pretend object. One 
of the most common objections to unit testing is that it can be quite difficult to test 
each function or class method in isolation, because of the dependencies that exist in 
all but the simplest code. For example:

1. Your function/class might depend on a remote resource such as a website, FTP server 
   or a cloud-based API that you are calling
2. The function that you wish to tests, function A, might use another function B as part 
   of its work
3. The class you wish to test, class A, might contain an instance of another class B 
   that is difficult to construct (i.e. perhaps it depends on loading a large and 
   cumbersome dataset).

For example 1, you would like your tests to pass even if the computer in question has no 
internet. For example 2, ideally you would want to be able to write a test for function 
A that didn't depend on function B, so that if a bug occured in function B, your tests 
for function A would still pass. For example 3, it would be nice to be able to test 
class A without having to construct the difficult class B.

For all these reasons, and many others, you can use mocking libraries to make your unit 
tests easier to write. There are many such libraries/frameworks that exist for different 
languages, for example:

- **C**: [CMocka](https://cmocka.org/)
- **C++**: [googletest](https://github.com/google/googletest)
- **Python**: [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

# Recording calls with mock

This lesson demonstrates the use of `unittest.mock`. This is a mocking framework within 
the Python standard library, and is therefore quite convenient to use. This framework 
contains a class `Mock`, which is callable and records all the calls that are made to 
it. For example:

~~~
from unittest.mock import Mock
function = Mock(name="myroutine", return_value=2)
function(1)
~~~
{: .language-python}

~~~
2
~~~
{: .output}

~~~
function(5, "hello", a=True)
~~~
{: .language-python}

~~~
2
~~~
{: .output}

~~~
function.mock_calls
~~~
{: .language-python}

~~~
[call(1), call(5, 'hello', a=True)]
~~~
{: .output}

The arguments of each call can also be recovered

~~~
name, args, kwargs = function.mock_calls[1]
args, kwargs
~~~
{: .language-python}

~~~
((5, 'hello'), {'a': True})
~~~
{: .output}

Mock objects can also return different values for each call

~~~
function = Mock(name="myroutine", side_effect=[2, "xyz"])
function(1)
~~~
{: .language-python}

~~~
2
~~~
{: .output}

~~~
function(1, "hello", {'a': True})
~~~
{: .language-python}

~~~
'xyz'
~~~
{: .output}

We expect an error if there are no return values left in the list:

~~~
function()
~~~
{: .language-python}

~~~
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-10-2fcbbbc1fe81> in <module>()
----> 1 function()

C:\ProgramData\Anaconda3\lib\unittest\mock.py in __call__(_mock_self, *args, **kwargs)
    917         # in the signature
    918         _mock_self._mock_check_sig(*args, **kwargs)
--> 919         return _mock_self._mock_call(*args, **kwargs)
    920 
    921 

C:\ProgramData\Anaconda3\lib\unittest\mock.py in _mock_call(_mock_self, *args, **kwargs)
    976 
    977             if not _callable(effect):
--> 978                 result = next(effect)
    979                 if _is_exception(result):
    980                     raise result

StopIteration: 
~~~
{: .output}

# Using mocks to model test resources

Often we want to write tests for code which interacts with remote resources. (E.g. 
databases, the internet, or data files.)

We don't want to have our tests actually interact with the remote resource, as this 
would mean our tests failed due to lost internet connections, for example.

Instead, we can use mocks to assert that our code does the right thing in terms of the 
messages it sends: the parameters of the function calls it makes to the remote resource.

For example, consider the following code that downloads a map from the internet:

~~~
import requests

def map_at(lat, long, satellite=False, zoom=12, 
           size=(400, 400), sensor=False):

    base = "http://maps.googleapis.com/maps/api/staticmap?"
    
    params = dict(
        sensor = str(sensor).lower(),
        zoom = zoom,
        size = "x".join(map(str,size)),
        center = ",".join(map(str,(lat,long))),
        style = "feature:all|element:labels|visibility:off")
    
    if satellite:
        params["maptype"] = "satellite"
        
    return requests.get(base, params=params)

london_map = map_at(51.5073509, -0.1277583)
from IPython.display import Image
~~~
{: .language-python}

We would like to write a test to check that the `map_at` function is building the 
parameters correctly for the call to the google mapping API. We can do this by mocking 
the requests object. We need to temporarily replace a method in the library with a mock. 
We can use `unittest.mock.patch` to do this:

~~~
from unittest.mock import patch
with patch.object(requests,'get') as mock_get:
    london_map = map_at(51.5073509, -0.1277583)
    print(mock_get.mock_calls)
~~~
{: .language-python}

~~~
[call('http://maps.googleapis.com/maps/api/staticmap?', params={'center': '51.5073509,-0.1277583', 'sensor': 'false', 'style': 'feature:all|element:labels|visibility:off', 'size': '400x400', 'zoom': 12})]
~~~
{: .output}

Our test then looks like:

~~~
def test_build_default_params():
    with patch.object(requests,'get') as mock_get:
        default_map = map_at(51.0, 0.0)
        mock_get.assert_called_with(
        "http://maps.googleapis.com/maps/api/staticmap?",
        params={
            'sensor':'false',
            'zoom':12,
            'size':'400x400',
            'center':'51.0,0.0',
            'style':'feature:all|element:labels|visibility:off'
        }
    )
~~~
{: .language-python}

# Testing functions that call other functions

~~~
def partial_derivative(function, at, direction, delta=1.0):
    f_x = function(at)
    x_plus_delta = at[:]
    x_plus_delta[direction] += delta
    f_x_plus_delta = function(x_plus_delta)
    return (f_x_plus_delta - f_x) / delta
~~~
{: .language-python}

We want to test that the above function does the right thing. It is supposed to compute the derivative of a function of a vector in a particular direction.

E.g.:

~~~
partial_derivative(sum, [0,0,0], 1)
~~~
{: .language-python}

~~~
1.0
~~~
{: .output}

How do we assert that it is doing the right thing? With tests like this:

~~~
from unittest.mock import MagicMock

def test_derivative_2d_y_direction():
    func = MagicMock()
    partial_derivative(func, [0,0], 1)
    func.assert_any_call([0, 1.0])
    func.assert_any_call([0, 0])
    

test_derivative_2d_y_direction()
~~~
{: .language-python}


> ## Write some unit tests using mocking
>
> Write a couple of unit tests for the `load_csv` function in `inflammation/models.py`. 
> Use mocking to ensure the test is independent of any csv files that might exist on 
> your computer, and make sure to test for the two different behaviours of the function 
> which occur when the input filename is either absolute or relative.
>
> > ## Solution
> > 
> > ~~~
> > ...
> > def test_load_csv():
> > ...
> > ~~~
> > {: .language-python}
> {: .solution}
>
{: .challenge}



{% include links.md %}
