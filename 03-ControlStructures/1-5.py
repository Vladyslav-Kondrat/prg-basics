###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20 * 0.5
tasks_ok = int( input('Test result: '))
test_passed = False

if tasks_ok >= total_tasks :
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')