"""
Test code for Split Array

Sardor Gulyamov 2022
"""

import json
import os
import sys

import pytest

import sum

# Handle the fact that the grading code may not
# be in the same directory as rotate.py
sys.path.append(os.getcwd())

# Get the name of the directory that holds the grading code.
BASE_DIR = os.path.dirname(__file__)
TEST_DIR = os.path.join(BASE_DIR, "tests")


def read_config_file(filename):
    """
    Load the test cases from a JSON file.

    Inputs:
      filename (string): the name of the test configuration file.

    Returns: (list) test cases
    """

    with open(os.path.join(TEST_DIR, filename)) as f:
        return json.load(f)


def gen_none_error(recreate_msg):
    """
    Generate the error message for an unexpected return value of None.

    Inputs:
      recreate_msg (string): a string with the information needed to
        rerun the test in ipython.

    Returns (string): error message
    """

    msg = "The function returned None."
    msg += " Did you forget to include a return statement?\n"
    return msg + recreate_msg + "\n"


def gen_type_error(recreate_msg, expected, actual):
    """
    Generate the error message for a return value of the wrong type

    Inputs:
      recreate_msg (string): a string with the information needed to
        rerun the test in ipython.

    Returns (string): error message
    """

    msg = "The function returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n"
    msg += "  Actual return type: {}.\n"
    msg += recreate_msg + "\n"
    return msg.format(type(expected), type(actual))


def gen_mismatch_error(recreate_msg, expected, actual):
    """
    Generate the error message for the case whether the expected and
    actual values do not match.

    Inputs:
      recreate_msg (string): a string with the information needed to
        rerun the test in ipython.

    Returns (string): error message
    """

    msg = "Actual ({}) and expected ({}) values do not match.\n"
    msg += recreate_msg + "\n"
    return msg.format(actual, expected)



@pytest.mark.parametrize(
    "params",
    read_config_file("prefix_sum.json"))
def test_prefix_sum(params):
    """
    Test harness for prefix_sum function.

    Inputs:
      params (dictionary): the test parameters:
        array and the expected prefix array
    """

    actual_prefix = sum.prefix_sum(params["array"])

    recreate_msg = "To recreate this test in python3 run:\n"
    recreate_msg += f'  sum.prefix_sum({params["array"]})'

    assert actual_prefix is not None, \
        gen_none_error(recreate_msg)

    expected_prefix = params["expected"]
    assert isinstance(actual_prefix, type(expected_prefix)), \
        gen_type_error(recreate_msg,
                       expected_prefix,
                       actual_prefix)

    assert actual_prefix == expected_prefix, \
        gen_mismatch_error(recreate_msg,
                           expected_prefix,
                           actual_prefix)




@pytest.mark.parametrize(
    "params",
    read_config_file("segment_sum.json"))
def test_rotate_right_by_k(params):
    """
    Test harness for rotate_right_by_k function.

    Inputs:
      params (dictionary): the test parameters:
        array, k, and the expected array
    """

    actual_array = sum.segment_sum(params["array"], params["left"], params["right"])

    recreate_msg = "To recreate this test in python3 run:\n" \
                   f'  sum.segment_sum({params["array"]}, {params["left"]}, {params["right"]})'

    assert actual_array is not None, \
        gen_none_error(recreate_msg)

    expected_array = params["expected"]
    assert isinstance(actual_array, type(expected_array)), \
        gen_type_error(recreate_msg,
                       expected_array,
                       actual_array)

    assert actual_array == expected_array, \
        gen_mismatch_error(recreate_msg,
                           expected_array,
                           actual_array)


@pytest.mark.parametrize(
    "params",
    read_config_file("split_array.json"))
def test_rotate_by_k(params):
    """
    Test harness for rotate_by_k function.

    Inputs:
      params (dictionary): the test parameters:
        array, k, and the expected array
    """

    array1, array2 = sum.split_the_array(params["array"])

    recreate_msg = "To recreate this test in python3 run:\n" \
                   f'  sum.split_array({params["array"]})'

    assert array1 is not None and array2 is not None, \
        gen_none_error(recreate_msg)

    expected_array1 = params["expected_1"]
    expected_array2 = params["expected_2"]
    assert isinstance(array1, type(expected_array1)), \
        gen_type_error(recreate_msg,
                       expected_array1,
                       array1)
    assert isinstance(array2, type(expected_array2)), \
        gen_type_error(recreate_msg,
                       expected_array2,
                       array2)

    assert array1 == expected_array1, \
        gen_mismatch_error(recreate_msg,
                           expected_array1,
                           array1)
    assert array2 == expected_array2, \
        gen_mismatch_error(recreate_msg,
                           expected_array2,
                           array2)
