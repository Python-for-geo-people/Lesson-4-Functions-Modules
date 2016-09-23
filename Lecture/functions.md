# Functions

## What is a function?

Function is a block of organized, reusable code that can make your code more effective, clearer to read and easier to handle. 
You can think functions as little self-contained programs that can perform a specific task which you can use repeatedly in your code. 
One of the basic principles in good programming is "not to repeat yourself", i.e. you shouldn't have
duplicate lines of code in your script. Functions are a way to avoid such situations and they can save you a lot of time and effort as you don't need to
retell the computer what to do every time it does a common task, such as converting temperatures from Fahrenheits to Celsius. 
During the course we have already used some functions such as `print()` command which is actually a built-in function in Python.

## Anatomy of a function

Let's consider the task from the first week when we converted temperatures from Fahrenheits to Celsius. Such an operation is a fairly common task 
when dealing with temperatures. Thus we might need to repeat such calculations quite frequently when analysing or comparing e.g. weather or 
climate changes between US and Europe.

Let's define our first function called `celsius_to_fahr`:

  ```python
  >>> def celsius_to_fahr(temp):
  ...    return 9/5 * temp + 32
  ```
  
<img src="https://github.com/Python-for-geo-people/Functions-and-libraries/blob/master/img/Function_anatomy.png" width="400">

The function definition opens with the keyword def followed by the name of the function and a parenthesized list of parameter names. 
The body of the function — the statements that are executed when it runs — is indented below the definition line.

When we call the function, the values we pass to it are assigned to those variables so that we can use them inside the function. 
Inside the function, we use a return statement to send a result back to whoever asked for it.

## Using functions

Let’s try running our function. Calling our own function is no different from calling any other function such as `print()`. 
You need to call it with its name and send your value to the required parameter(s) inside the parentheses:  
  
```python
>>> freezing_point =  celsius_to_fahr(0)
>>> print('Freezing point of water in Fahrenheits:', freezing_point)
Freezing point of water in Fahrenheits: 32.0
>>> print('Boiling point of water in Fahrenheits:', celsius_to_fahr(100))
Boiling point of water in Fahrenheits: 212.0
```

Now as we know how to create a function to convert Celsius to Fahrenheits, let's create another function called `kelvin_to_celsius`:
  
```python
>>> def kelvin_to_celsius(temp_k):
...    return temp_k - 273.15
```

And let's use it in a similar way as the earlier one:

```python
>>> absolute_zero = kelvin_to_celsius(temp_k=0)
>>> print('Absolute zero in Celsius:', absolute_zero)
Absolute zero in Celsius: -273.15
```

What about converting Kelvin to Fahrenheits? We could write out an own formula for it, but we don’t need to. Instead, we can compose it by using the two functions we have already created and 
calling the other functions inside the function we are now creating: 
    
```python
>>> def kelvin_to_fahrenheit(temp_k):
...    # Kelvin in celsius
...    temp_c = kelvin_to_celsius(temp_k)
...    # Celsius in Fahrenheit
...    temp_f = celsius_to_fahr(temp_c)
...    # Return the result
...    return temp_f
```  

Let's use the function:
  
```python
>>> absolute_zero_f = kelvin_to_fahrenheit(temp_k=0)
>>> print('Absolute zero in Fahrenheit:', absolute_zero_f)
Absolute zero in Fahrenheit: -459.66999999999996
```


## Importing functions from a script

Functions such as the ones we just created can also be called from another script.

### 1. Saving functions into a script file
 
Before we can import our functions we need to create a new script file and save the functions that we just created into a Python file called _temp_converter.py_ \[0\].   

We can take advantage of the _History log_ -tab where we should be able to find all of the commands that we wrote to IPython console:
 
<img src="https://github.com/Python-for-geo-people/Functions-and-libraries/blob/master/img/history_log.PNG" width="400">

Copy and paste the functions from the History log -tab and save them into the temp_converter.py -script. 
It should look like following:

<img src="https://github.com/Python-for-geo-people/Functions-and-libraries/blob/master/img/temp_converter.PNG" width="400">
 
### 2. Using functions from another script file



\[0\] See [earlier materials concerning Spyder](spyder.md) if you don't remember how to save a new script file from Spyder. 



**TODO**

- Explain different parts of function
- Create a simple function
- Create a py-file with functions
- import those functions from the file and use them from another file.