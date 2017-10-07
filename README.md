# python_selenium_parallel_tests
python selenium parallel tests in same browser or different browsers like Chrome, Firefox, Safari etc


check requirements.txt to see the necessary packages. To install all the packages in requirements.txt run this command

    pip install -r requirements.txt



Steps to run tests in Parallel in One Browser Eg - all tests in Chrome:

open terminal
navigate to the project folder

    pytest -n 5 #there are 5 tests in this project

or

    nosetests --processes=5

5 browsers will open and all the tests will run in parallel


Steps to run tests in Parallel in Different Browsers:

Open the project test files in an editor and change the "browserName" in each file under setUp method
Eg:
test_one.py - "browserName": "chrome"
test_two.py - "browserName": "firefox"
test_parallel.py - "browserName": "safari"

Save the files

open terminal
navigate to the project folder

    pytest -n 5 #there are 5 tests in this project

or

    nosetests --processes=5