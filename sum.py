"""
Enter your full name here:



Enter your ID here:


"""


def prefix_sum(array):
    """
    Given a list called 'array', return a new list of prefix sums

    Input:
        array (list) - a list of integers

    Return:
        new_array (list) - a list of integers where new_array[i] is the sum
                           of first i elements of 'array'.

        So, new_array[i] = array[0] + array[1] + ... + array[i-1]
        Note that 'new_array' will always have 1 more element than 'array'

    Example: if array = [1, 2, 3, 4, 5],
    then you should return [0, 1, 3, 6, 10, 15]

    YOU SHOULD NOT CHANGE ANYTHING IN 'array', BUT INSTEAD
    DO ALL THE WORK ON 'new_array' AND RETURN IT
    """
    prefix_array = [0]


def segment_sum(array, left, right):
    """
    Return the sum of the 'array' from the 'left' index all the way until the
    'right' index. 'right' index needs to be included too.

    You MUST use prefix_sum

    Input:
        array (list) - a list of integers
        left (integer) - a non-negative integer, a valid index in the 'array'
        right (integer) - a non-negative integer, a valid index in the 'array'.
                          It can always be assumed that
                          left <= right

    Return:
        the sum of the elements of 'array' from the 'left' index until 'right'
        index, inluding it in the sum.

        In other words, you should return what
        array[left] + array[left + 1] + ... + array[right - 1] + array[right]
        would be equal to by using the array you get from prefix_sum

    Example:
        Inputs: array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], left = 2, right = 5
        Return: array[2] + array[3] + array[4] + array[5] = 18
    """
    prefix_array = prefix_sum(array)



def split_the_array(array):
    """
    Split the array into two parts such that the sum of each of them is equal.
    The concattenation of the two parts must be the same as the original 'array'

    You MUST use subsegment_sum

    Input:
        array (list) - a list of integers
    Return:
        array1, array2 (list) - two lists of integers such that the sum of the
                                elements of array1 is equal to the sum of
                                elements of array2, and

                                array = array1 + array2

        If two splittings exist, return the one for which array1 has the least
        amount of elements.

    For example, if array = [1, 2, 4, -1] you must return two arrays
    array1 = [1, 2], and array2 = [4, -1]
    """
    return array1, array2
