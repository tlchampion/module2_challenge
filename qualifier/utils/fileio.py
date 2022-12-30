# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import os


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(qualifying_loans, csvpath='./qualifying_loans.csv'):
    """
    saves qualifying loans to a CSV file

    Args:
    qualifying_loans: the list of qualifying bank loans
    csvpath: path and filename where qualifying loans should be saved
    """

    header = ["Lender", "Max Loan Amount", "Max LTV",
            "Max DTI", "Min Credit Score", "Interest Rate"]

    # if directory does not exist, create it
    os.makedirs(os.path.dirname(csvpath), exist_ok=True)
    # catch any file writing errors so a user-friendly warning message can be shown
    # return True if file save has no errors, False if there is an error
    try:
        with open(csvpath, 'w') as csvfile:
            try:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(header)
                for loan in qualifying_loans:
                    csvwriter.writerow(loan)
            except (IOError, OSError):
                return False
    except (FileNotFoundError, PermissionError, OSError):
        return False

    return True
