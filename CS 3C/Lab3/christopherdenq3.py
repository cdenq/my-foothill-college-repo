""" An object-oriented program that utilizes the Stack class to balance
arithmetic symbols.

This is the test driver.

Benchmark times:
1: 1.2999999999999123e-05
2: 1.5700000000000436e-05
3: 1.7900000000001248e-05
Avg: 1.5533333333333604e-05

Space/Time Complexity: O(n)

Worst case is O(n) for BOTH. If the entire symbol is "balanced", so you
will need to both create the Stack that is and loop through the Stack
for the entire length of symbols into the Stack object.

Best case is O(1) for BOTH. You instantly get a symbol that fails, and
thus, you just immediately return.

Normally when you report time complexity, you report the worst case.

Christopher Denq
CS 3C, 2022
Lab 3
"""


from christopherdenqstack import *
import timeit

# Create benchmark variable
benchmark_times = []

# Delimiters
open_delimiters = ["(", "[", "{"]
closed_delimiters = [")", "]", "}"]


def check_balanced_timed(symbols: str):
    """ Runs the Test Driver and Algorithm, but timed.
    """
    start_time = timeit.default_timer()
    result = check_balanced(symbols)
    end_time = timeit.default_timer()
    benchmark_times.append(end_time - start_time)
    return result


def check_balanced(symbols: str):
    """ Runs the Test Driver and Algorithm.
    """
    # Create Stack object
    test = Stack.create_stack()

    # Used to check for matching delimiters
    index_of_added = 0
    index_of_popped = 0

    # Run main
    for i in range(len(symbols)):
        if symbols[i] in open_delimiters:
            index_of_added = open_delimiters.index(symbols[i])
            test.push(symbols[i])
        elif symbols[i] in closed_delimiters and test.is_empty():
            print("List is empty, so cannot pop!")
            return False
        elif symbols[i] in closed_delimiters:
            # If close delimiter and stack not empty
            index_of_added = closed_delimiters.index(symbols[i])
            popped_value = test.peek()
            test.pop()

            # Checking to see if popped value was the correct open delimiter
            if popped_value in open_delimiters:
                index_of_popped = open_delimiters.index(popped_value)
                if index_of_added != index_of_popped:
                    # Popped open delimiter doesn't match our given closing one
                    return False
                else:
                    # Else, popped value was the correct open delimiter
                    continue
            else:
                # Else, popped value wasn't an open delimiter at all
                return False
    if test.head is None:
        return True
    else:
        # After all the symbols, the Stack object has at least one
        # "unpaired" symbol, and thus is not balanced.
        return False


def main():
    # Welcome to interactive section
    print("Welcome to Chris's Stack Balancer!")
    print("")  # Add another newline for spacing

    # Run interactive section
    print("Output 1:", check_balanced_timed("([|)]"))
    print("Output 2:", check_balanced_timed("()(()[()])"))
    print("Output 3:", check_balanced_timed("{{([][])}()}"))
    print("Output 4:", check_balanced_timed("("))
    print("")  # Add another newline for spacing

    # Show benchmarks
    print("Benchmark times:")
    for i in range(len(benchmark_times)):
        print(f"{i+1}: {benchmark_times[i]}")
    print(f"Avg: {sum(benchmark_times)/len(benchmark_times)}")
    print("")  # Add another newline for spacing

    # Closing to interactive section
    print("Thank you for using Chris's Stack Balancer!")
    print("Bye!")
    return


if __name__ == "__main__":
    main()


r"""
----sample run----
Welcome to Chris's Stack Balancer!

Output 1: False
Output 2: True
Output 3: True
Output 4: False

Benchmark times:
1: 1.3699999999998436e-05
2: 1.5999999999995185e-05
3: 1.7699999999995497e-05
4: 2.9000000000001247e-06
Avg: 1.257499999999731e-05

Thank you for using Chris's Stack Balancer!
Bye!

"""