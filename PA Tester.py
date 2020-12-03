# <FIXME: PA Tester block, if used in final program, REMOVE before submitting your program>
def tester(tests, output):
    for test in range(len(tests)):
        # if output of test cases == expected output in output, pass the test
        if tests[test] == output[test]:
            continue
        # otherwise return failure at the failed test
        else:
            return "Error at test " + str(test+1) + ".\nGot: " + str(tests[test]) + "\nExpected: " + str(output[test])
    return "All tests passed!"
# Example variables

# Test cases
tests = [

]
# Outputs of test cases (must be in same order as test cases to work properly)
output = [

]
print(tester(tests, output))
# </FIXME: PA Tester block, if used in final program, REMOVE before submitting your program>
