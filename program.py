import pandas as pd
import os
from frictionless import describe, validate, Package, Resource


def create_df(imported_file):
    if imported_file.endswith('csv'):
        dataframe_table = pd.read_csv(imported_file, delimiter="|")
        return dataframe_table
    else:
        raise TypeError("This file format isn't supported. Please try again.")


def create_data_package(clean_data, output_directory):
    metadata = describe(clean_data)
    resource = Resource.from_descriptor(metadata.to_dict())
    package = Package(resources=[resource])
    os.makedirs(output_directory, exist_ok=True)
    export_package = os.path.join(output_directory, 'datapackage.json')
    package.to_json(export_package)
    return package


def create_readme(output_directory):
    os.chdir(output_directory)
    path = os.path.join(output_directory, 'README.md')
    with open('README.md', 'x') as r_file:
        r_file.write("#README.md for frictionless data package\n")
        r_file.write("Enter documentation here.")
    return path


while True:

    while True:
        file = input("Please enter file name: ")
        try:
            create_df(file)
            break
        except FileNotFoundError:
            if not os.path.exists(file):
                print(f'The {file} file does not exist in this current directory.')

    df_creation = input(f'A DataFrame has been made of {file}. Would you like to see? (yes/no) ').lower()

    if df_creation == 'yes':
        df = create_df(file)
        print(df.to_markdown())
    elif df_creation == 'no':
        print("OK.")
    else:
        raise ValueError('Invalid input!')

    data_validation = input(f'Would you like to validate the data from {file}? (yes/no) ').lower()

    if data_validation == 'yes':
        report = validate(file)
        print(report)
        if report.valid:
            print('The data is valid.')
        else:
            print("The following errors were found: ", report.flatten(["rowNumber", "fieldNumber", "code", "message"]))
            check_errors = input(f'Would you like to fix them? (yes/no) ').lower()
            if check_errors == "no":
                print("OK.")
            else:
                print('The ability to clean raw data is unavailable in this program.')
    elif data_validation == 'no':
        print("OK.")
    else:
        raise ValueError("Invalid input!")

    frictionless_dp = input("Create a frictionless data package with metadata? (yes/no) ").lower()

    if frictionless_dp == 'yes':
        create_data_package(file, "./data-package")
        print(f"The frictionless data package has successfully been created.")
        readme_file = input("Would you like to generate a README.md file? (yes/no) ").lower()
        if readme_file == 'yes':
            readme_data = create_readme("./data-package")
            print("The 'README.md' file has been successfully created in directory.")
        elif readme_file == 'no':
            print("OK.")
        else:
            raise ValueError('Invalid input!')
    elif frictionless_dp == 'no':
        print("OK.")

    repeat_program = input("Do you want to enter another file? (yes/no) ").lower()
    if repeat_program == 'no':
        break
