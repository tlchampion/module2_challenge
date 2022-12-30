# Loan Qualifier Application

This project provides an automated means to compare the attributes of a potential borrower to the loan offerings of a set of banks. The potential borrowers monthly debt to income ratio and the loan to value ratio are displayed along with a notification of how many qualifying loans exist in the provided list of banks.
The user is then provided the option to save the list to a CSV file at a user-specified location.

---

## Technologies

This software is written in the Python programming language (version 3.9.15). While the application may work in other versions of python, no guarantees of such are made.

Additional Python libraries necessary for this software include:
* questionary
* fire

An environment.yml file is included listing all packages that should be included in the python environment prior to using this software.

---

## Installation Guide

If obtained in a zip archive, the contents must first be unzipped.
All files can be moved to any desired location on your hard drive, being sure to retain the established directory structure. See below for the required directory structure:
```
|-- app.py
|
|-- qualifier
		|
		|-- filters
		|	 |-- credit_score.py
		|	 |-- debt_to_income.py
		|	 |-- loan_to_value.py
		|	 |-- max_loan_size.py
		|
		|-- utils
			 |-- calculators.py
			 |-- fileio.py
```

It is recommended to install a new python environment in which to run the application. If using conda, a new environment including all required packages can be created using the supplied environment.yml file as follows:

```
conda env create -f environment.yml
```
Alternatively, the required packages can be installed using pip into a python environment of your choosing:

```
pip install questionary
pip install fire
```


---

## Usage

Prior to using the application you will need to have the following items available:
1. a csv file with the following information, in the listed order, on potential lenders:
    ```
        Lender,Max Loan Amount,Max LTV,Max DTI,Min Credit Score,Interest Rate
    ```
2. The following information related to the potential borrower
   * credit score
   * current monthly debt
   * current monthly income
   * amount of desired loan
   * current value of home

Once all required information is available the application can be run in a terminal from within the root directory of the application:

```
python app.py
```
At each prompt provide the requested information. After the potential lenders, if any, are determined you will be notified of how many potential lenders exist and then provided with the opportunity to save the lender information into a separate csv file. If so desired, provide the requested directory path and file name for the new csv file.

Please see below for a sample run showing all prompts and requesting to have the lender information saved to a csv file.

```
> python app.py
? Enter a file path to a rate-sheet (.csv): ./data/daily_rate_sheet.csv
? What's your credit score? 750
? What's your current amount of monthly debt? 5000
? What's your total monthly income? 35000
? What's your desired loan amount? 5000
? What's your home value? 800000
The monthly debt to income ratio is 0.14
The loan to value ratio is 0.01.
Found 15 qualifying loans
? Would you like to save the list of qualifying loans to a csv file? Yes
? Would you like to save the file in the default location? (./qualifying_loans.csv) No
? Please enter the filepath, including both directory path and file name,
   where you would like to save the loan information.
   Either absolute or relative filepaths may be used. ./qualifying_loans.csv
File successfully saved


Thank you for using the application.

```

---

## Contributors

Initial code segments provided by FinTech bootcamp.
Code completion by Thomas L. Champion (thomas@thomaschampion.net)

---

## License

Please refer to the LICENSE file for details on the license this application is made available under.
