# Intro to CS Tutorial Mock Exam
Dear students, this is the Mock Exam for your Intro to CS Tutorial. The actual Final exam will have the identical structure and the problems will be of similar level of difficulty.
<br><br>
The file that you need to work with is `rotate.py`. <b>DO NOT EDIT ANY OTHER FILE</b>. In every single task, except for Task 1, you will have to use a function you have written beforehand.
Note that **if you do not use a previous function** to solve the next task, points will be deducted up to my consideration. 

Additionally, **you are responsible** for the testing code to work properly. Reminder that to test your code, you need to go inside the **mock-exam** directory in terminal, and run <br>
```python3 -m pytest -xv```
<br> To navigate to that directory, you need to use the `cd` command in the terminal. For the terminal commands, I have provided a short tutorial with your exam.

## Cyclic Rotations

Given an array, we would like to cyclically rotate it a given number of times. Cyclic rotation is when every single element of the array is moved in the same direction by the same number of indices,
 and the elements at the end get moved to the beginning, like a cycle.
<br><br>
So, for example, given an array `[1, 2, 3, 555, 234, 44]`, cyclically rotating it right by 1 would result in `[44, 1, 2, 3, 555, 234]`. If we cyclically rotate this new array right by 4,
 we get `[2, 3 ,555 ,234 , 44, 1]`.
<br><br>
**Any sort of HARDCODING of test cases will be penalized with 0 on the exam**
You have to implement three functions:
<ol>
    <li>rotate_right_by_1 which takes an array and returns what it would look like if it were rotated right once </li>
    <li>rotate_right_by_k which takes an array, a non-negative integer k, and returns what it would look like if it were rotated right k times </li>
    <li>rotate_by_k which takes an array, an integer k(maybe positive, negative, or zero) and returns what the array would look like if it was rotate |k| times right if k positive and left if k is negative</li>
</ol>



## Testing

To test your entire code, please run ```python3 -m pytest -xv```, and if you want to test your functions separately, use
```python3 -m pytest -xvk ``` followed by the name of the function. For example, to test the first function separately,
run ```python3 -m pytest -xvk rotate_right_by_1```
