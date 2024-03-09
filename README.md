# Python Selenium Pytest Demo
This project showcases basic capabilities of Selenium with Pytest framework, using the [Restful Booker Platform](https://automationintesting.online/) as its target. It also implements [Allure](https://allurereport.org/) for dynamic reports and features parallel test execution, along with API requests for creating test data.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

### Page Object Pattern
This project utilizes the Page Object Pattern as its primary approach to code management. Each page of the application is represented as a corresponding class, which contains selectors for elements and methods covering specific actions across that page, available after initialization of the page object. All technical aspects of the Selenium framework, such as selector operations, explicit waits, or general actions across the entire application, are stored in one common parent class called BasePage. This pattern provides a clear separation between low-level "background" actions and high-level code used for creating tests.

An object-oriented approach has also been employed to store test data, such as accounts, bookings, messages, etc. Having templates for these common building blocks has resulted in better code readability and easier management of the data. API requests have also been designed as methods of one central class for clarity.

### Pytest fixtures, tags and parallel test execution
The pytest framework orchestrates the execution of test cases and provides a flexible platform for organizing, managing, and executing tests. It supports fixture injection to set up resources like the Selenium WebDriver instance, custom string files and other common test data. Additionally, pytest manages assertions for verifying expected behaviors at the end of each test case. Tags categorize tests into distinct roles such as admin and customer, aiding in clear organization and separation of test cases. Parallel test execution is implemented, significantly reducing test execution time by leveraging concurrent processing capabilities.

### Reporting with Allure
Allure provides elegant, 'business-friendly' reports containing various metrics such as test execution rate, pass rate, scenario and test suite duration, captured errors, etc. Allure decorators inside test files allow labeling tests with custom titles, descriptions, and other various data accessible inside the reports. Furthermore, this project leverages the ability to capture snapshots of the browser during failed scenarios and link them directly to Allure reports.

The report files are stored inside the project directory in the `reportallure` folder and are available after running `allure serve ./reportallure/` in the terminal after finishing tests. It's important to note that by default, the report files will be replaced each time you run the test suite, so ensure you archive the reports in a different directory for later access or change Allure configuration in pytest.ini to allow storing multiple test runs.

### API requests
API requests, provided by the popular Python "requests" library, were utilized to generate test data and further validate some of the application's behavior. Using API requests also adheres to the principle of test isolation, where each test operates on separate products of the application (e.g., accounts, orders). Additionally, in some cases where the environment might become quickly cluttered during the test suite itself, API requests can be part of a "cleanup" procedure, deleting unused test assets after the test has ended. This would come at the cost of losing some data useful for debugging the application and test cases themselves, but with excessive logging mechanisms and screenshot capture, that issue could be mitigated.

## Installation

1. Download or clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Ensure that your Chrome browser is installed and up to date.
5. Install [Allure](https://allurereport.org/docs/gettingstarted-installation/) and its dependencies (Java version 8 or above).

## Usage
### Running tests
Run `pytest` in project directory to launch the full test suite. By default, it will run tests in 2 parallel processes, in headless mode. 
Run `allure serve ./reportallure/` to generate Allure report after finished tests.

#### Using tags
`-m <tag name>` - Adding `-m customer` or `-m admin` will only launch tests specific to customer or admin.

#### Optional parameters
`-n <int>` - default `2`. Specifies the number of parallel test processes.

`--test-debug` - default `None`. Passing this argument will turn off headless mode and partially abort test cleanup, leaving the browser process opened. Used for debugging singular test cases.

`--lang <string>` - default `english`. Selects a file with language strings, for various assertions and checks. Strings for all code are stored in a single file, allowing running the same tests on different language versions of the tested application. For this demo English is the only available language.
