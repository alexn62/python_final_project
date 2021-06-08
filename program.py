import math


# --- Function and variable definitions and tests ---#


# Constants
# Allowed max and min inputs.
MAX_NUMBER = 100
MIN_NUMBER = -100

# Define the maximum number of inputs permitted.
MAX_LENGTH = 20

# Error messages
POSITIVE_AND_WHOLE_ERROR_MESSAGE = 'Number has to be a positive and whole number.'
WHOLE_NUMBER_ONLY_ERROR_MESSAGE = 'Enter whole numbers only.'
RANGE_ERROR_MESSAGE = f'Number has to be between {MIN_NUMBER} and {MAX_NUMBER}.'
NOT_AN_ARRAY_ERROR_MESSAGE = 'The given input is not an array, or a value in the array is not an integer.'
EMPTY_ARRAY = 'The given array does not include any elements.'

# Alert messages
RESTART_PROMPT = 'Do you want to restart? (y/n) '
RETRY_MESSAGE = 'Please type \'y\' to try again, or \'n\' to quit. '           
GOOD_BYE_MESSAGE = 'Thank you and goodbye!'


def is_prime(num):
    """
    Checks if a number is a prime number, or not. Only accepts positive whole numbers as input.

    :param num: The number to check for prime.
    :type num: int
    :rtype bool
    :return:
    Returns True if the parameter is a prime number. Returns False if the parameter is not a prime number.

    >>> is_prime(3)
    True

    >>> is_prime(8)
    False

    >>> is_prime(0)
    False

    >>> is_prime(-7)
    Traceback (most recent call last):
        ...
    AssertionError: Number has to be a positive and whole number.

    >>> is_prime('foo')
    Traceback (most recent call last):
        ...
    AssertionError: Number has to be a positive and whole number.
    """
    
    assert type(num) == int and num >= 0, POSITIVE_AND_WHOLE_ERROR_MESSAGE
    # Returns True if the number is greater than 0 and smaller or equal to 3, as 1, 2, and 3 are all prime numbers.
    if 0 < num <= 3:
        return True

    # If a number is even, it is not a prime number, and we will thus return False.
    if num % 2 == 0:
        return False

    # Now we will check whether a number is divisible by an odd integer starting at 3, incrementing it by 2,
    #   since only even numbers would be divisible by other even numbers.
    # We will stop the loop after we hit the square root of a given number. 
    # This is for optimization purposes, to avoid running unnecessary iterations.
    # Explanation: One of the factors to make up a number has to be smaller than the square root, since otherwise, 
    #   the product would be greater than the original number. Therefore, we can stop checking after hitting
    #   the square root, since that would mean both factors are bigger than the square root, which is impossible.
    for i in range(3, math.ceil(math.sqrt(num)), 2):
        if num % i == 0:
            return False
    return True


number_array = []


def handle_input(raw_input):
    """
    :param raw_input: The input to check for errors.
    :type raw_input: str

    >>> handle_input('foo')
    Enter whole numbers only.

    >>> handle_input('')
    Enter whole numbers only.
    
    >>> handle_input(1.3)
    Traceback (most recent call last):
        ... 
    AssertionError: Enter whole numbers only.

    >>> handle_input(-101)
    Traceback (most recent call last):
        ... 
    AssertionError: Number has to be between -100 and 100.

    >>> handle_input(101)
    Traceback (most recent call last):
        ... 
    AssertionError: Number has to be between -100 and 100.

    >>> handle_input(100)
    You have entered ...

    >>> handle_input(0)
    You have entered ...

    >>> handle_input(-100)
    You have entered ...
    """

    try:
        number_input = int(raw_input)

        assert number_input == float(raw_input), WHOLE_NUMBER_ONLY_ERROR_MESSAGE
        assert -100 <= number_input <= 100, RANGE_ERROR_MESSAGE

        number_array.append(number_input)

        if len(number_array) < MAX_LENGTH:
            print(f'You have entered {len(number_array)} valid numbers, you can add {MAX_LENGTH - len(number_array)} more numbers.')
            print(f'So far, your numbers are: {number_array}')

    except ValueError:
        print(WHOLE_NUMBER_ONLY_ERROR_MESSAGE)


def compute_numbers(numbers):
    """
    Takes in an array an finds the prime numbers up to the max number of the array. Calculates the sum of numbers that a given prime number is 
        a factor of, and stores the values in a map.

    :param numbers: The array to check for prime numbers and the sum of prime factors.
    :type numbers: list
    :rtype dict
    :return:
    Returns a dictionary with the prime numbers as keys, and the sum of the numbers a prime is a factor of.

    >>> compute_numbers([4, 5, -2])
    {2: 2}

    >>> compute_numbers(3)
    The given input is not an array, or a value in the array is not an integer.
    
    >>> compute_numbers('foo')
    The given input is not an array, or a value in the array is not an integer.

    >>> compute_numbers((2,3))
    The given input is not an array, or a value in the array is not an integer.

    >>> compute_numbers([2, -1, 'foo'])
    The given input is not an array, or a value in the array is not an integer.
    
    >>> compute_numbers([2, -1, [1, 2]])
    The given input is not an array, or a value in the array is not an integer.
   
    >>> compute_numbers([])
    The given array does not include any elements.
    

    """
    # Create an empty map for the prime numbers The keys will be the primes, and the values will be the sum of numbers
    #   that the specific prime is a factor of.
    primes_and_sums = {}

    try:
        # Check that the input is an array, and the array is not empty.
        if len(numbers) == 0:
            raise ValueError
        if type(numbers) != list:
            raise TypeError
        # abs() will raise a TypeError is an element of the array is not an integer. The error will be caught, and we will output an error-message.
        abs_numbers = list(map(abs, numbers))

        for number in range(2, max(abs_numbers)):
            # Check each number between 2 and the max of the absolute numbers if it's a prime number.
            # A non-valid number or input will never reach the is_prime() function, because handle_input() checks all the user inputs for validity
            if is_prime(number):
                # If a given number is a prime, we will check whether it is a factor of one the original items in the numbers.
                for num in numbers:
                    if num % number == 0:
                        # If a number is a factor of one of the original numbers, we will check if the number is already registered in the map of the the primes and factor sums.
                        if number not in primes_and_sums:
                            # If the number is not registered, we will make a new entry with the prime number that we found and add the first value (num) to it.
                            primes_and_sums[number] = num
                        else:
                            # If the number is already registered, we do not want to create a new entry, but we want to add the number to the sum.
                            primes_and_sums[number] += num
        return primes_and_sums
    except TypeError:
        print(NOT_AN_ARRAY_ERROR_MESSAGE)
    except ValueError:
        print(EMPTY_ARRAY)


def restart_program_process(): 
    """
    Re-run program if desired. 'y' will re-run, 'n' will quit the program.
    Any other input will ask the question again.
    """   
    while True:
        try_again = input('You have not entered any valid numbers. ' + RETRY_MESSAGE)
        if try_again in ('y', 'n'):
            break
        else:
            print(RETRY_MESSAGE)

    if try_again == 'y':
        main_program()
    else:
        print(GOOD_BYE_MESSAGE)
        exit()


# Defining main_program as a function to establish re-running possibilities.
def main_program():

    # Making the variable global, because testing already mutates the original array. 
    global number_array 
    number_array = []

    # Let the user put in numbers until the max is reached or the user decides to move on. 
    while len(number_array) < MAX_LENGTH:
        raw_input = input(f'Please enter a whole number between {MIN_NUMBER} and {MAX_NUMBER}, or leave empty and press enter to continue: ')
        # Break out of the while loop when the user just hits enter (submits an empty string).
        if raw_input == '':
            break
        try:
            handle_input(raw_input)
        except AssertionError:
            continue
    
    if len(number_array) == 0:
        # Initialize restarting process.
        restart_program_process()

    # The array of numbers input by the user is forwarded to compute_numbers() and the return value is stored in a variable called 'primes'.
    primes = compute_numbers(number_array)
    
    # Print out the results.
    print(f'\nYour prime numbers and the sum of numbers of which the primes are factors of are: {primes}\n')

    # Initialize restarting process
    restart_program_process()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)

# Run program.
main_program()
