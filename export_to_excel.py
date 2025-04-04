import pandas as pd

def export_to_excel(test_cases, filename='test_cases.xlsx'):
    """
    Exports a list of test case objects to an Excel sheet.

    :param test_cases: List of test case objects.
    :param filename: Name of the Excel file to save the data.
    """
    data_list = [
        {
            'Test Case ID': case.test_case_id,
            'Test Title': case.test_title,
            'Description': case.description,
            'Preconditions': case.preconditions,
            'Test Steps': case.test_steps,
            'Test Data': case.test_data,
            'Expected Result': case.expected_result,
            'Actual Result' : '',
             'Status':'',
            'Comments': case.comments
        }
        for case in test_cases
    ]

    df = pd.DataFrame(data_list)
    df.to_excel(filename, index=False)
    print(f"Test cases exported to {filename}")