# Intro to CS Tutorial Final Exam
<br><br>
The file that you need to work with is `sum.py`. <b>DO NOT EDIT ANY OTHER FILE</b>. In every single task, except for Task 1, you will have to use a function you have written beforehand.
Note that **if you do not use a previous function** to solve the next task, points will be deducted up to my consideration. 

Additionally, **you are responsible** for the testing code to work properly. Reminder that to test your code, you need to go inside the **mock-exam** directory in terminal, and run <br>
```python3 -m pytest -xv```
<br> To navigate to that directory, you need to use the `cd` command in the terminal. For the terminal commands, I have provided a short tutorial with your exam.

## Split the Array

Given an `array`, we would like to split it into two parts, `array1` and `array2` such that `array = array1 + array2`, so that the sum of elements of `array1` is equal to the sum of elements of `array2`
<br><br>
**Any sort of HARDCODING of test cases will be penalized with 0 on the exam**
You have to implement three functions:
<ol>
    <li>prefix_sum which takes an array and returns a new array of prefix sums </li>
    <li>segment_sum which takes an array, a non-negative integer left, and a non-negative integer right, and returns the sum of the segment of the array starting at index left and ending(including) the index right </li>
    <li>split_the_array which takes an array, and returns two arrays array1 and array2 which is the correct splitting of the array.</li>
</ol>



## Testing

To test your entire code, please run ```python3 -m pytest -xv```, and if you want to test your functions separately, use
```python3 -m pytest -xvk ``` followed by the name of the function. For example, to test the first function separately,
run ```python3 -m pytest -xvk prefix_sum```
