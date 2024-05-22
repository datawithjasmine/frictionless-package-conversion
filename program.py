# FRICTIONLESS-PACKAGE-CONVERSION PROGRAM created by JASMINE MITCHELL

#       This script turns '.csv' files into frictionless data packages
#                           --- COMMENTS ---


# 1. I IMPORTED THE FOLLOWING LIBRARIES
#   - Pandas: to create a DataFrame from the csv file.
#   - OS: to handle files and directories, especially to export file.
#   - Frictionless: to create metadata, check for errors, and create data package.
import pandas as pd
import os
from frictionless import describe, validate, Package, Resource

# 2. The CREATE_DF function is to create a DataFrame from the csv file.
#    I checked to see if the imported file ends in '.csv' first.
#    if so, then a DataFrame will be created. Otherwise, return a
#                           TypeError.


def create_df(imported_file):
    if imported_file.endswith('csv'):
        dataframe_table = pd.read_csv(imported_file, delimiter="|")
        return dataframe_table
    else:
        raise TypeError("This file format isn't supported. Please try again.")

# 3. The CREATE_DATA_PACKAGE function is to create the actual frictionless data package.
#    When you have clean data, the function will extract the metadata from it.
#    The contents of the metadata is now stored as a dictionary object and created as
#    a resource object. In order to turn this resource object into a data package,
#     'Package' takes the resource object and creates a list out of the metadata.
#   To create the folder, I used 'os.makedirs' then created output directory and name
#       of the package that is to be exported. Finally, I convert the actual package
#      into a JSON object, which is the common format for frictionless data packages.
#    Created a return statement, in case I wanted to see the contents of the package.


def create_data_package(clean_data, output_directory):
    metadata = describe(clean_data)
    resource = Resource.from_descriptor(metadata.to_dict())
    package = Package(resources=[resource])
    os.makedirs(output_directory, exist_ok=True)
    export_package = os.path.join(output_directory, 'datapackage.json')
    package.to_json(export_package)
    return package

# 4. The CREATE_README function is a function called after a user makes a frictionless
#     data package. A frictionless data package might include a 'README.md' file according
#                               to the Frictionless Framework.
#     I changed to the directory that holds the folder of the frictionless data package.
#       I define a path of the 'README.md' and create the file itself. I wrote some
#      comments that will be written to the file. Included a return statement to clarify
#                      the path of the newly created 'README.md' file.


def create_readme(output_directory):
    os.chdir(output_directory)
    path = os.path.join(output_directory, 'README.md')
    with open('README.md', 'x') as r_file:
        r_file.write("#README.md for frictionless data package\n")
        r_file.write("Enter documentation here.")
    return path

#   'while True' is added to the beginning so that the program repeats if
#                   more files need to be converted.


while True:

    # Allows user to enter the csv file name and checks if it exists in the
    # same directory as the program. I included it in a try/except statement
    # so that the user knows that it doesn't exist and prompts the user again.

    while True:
        file = input("Please enter the name of the csv file: ")
        try:
            create_df(file)
            break
        except FileNotFoundError:
            if not os.path.exists(file):
                print(f'The {file} file does not exist in this current directory.')

    #       Prompts the user if they want to see a DataFrame of the csv file. Calls the CREATE_DF function
    #                              with the file entered as its argument.
    # If user says no, it goes to the next prompt. If user enters something other than yes or no, it raises
    #                                          a ValueError.

    df_creation = input(f'A DataFrame has been made of {file}. Would you like to see? (yes/no) ').lower()

    if df_creation == 'yes':
        df = create_df(file)
        print(df.to_markdown())
    elif df_creation == 'no':
        print("OK.")
    else:
        raise ValueError('Invalid input!')

    #      Prompts the user if they want to see the csv file validated and to check for errors.
    #      if there are errors, the output will tell the user the errors. Then the user will be
    #                               prompted to fix those errors.
    #       I wanted to include a section of the program that will clean and transform the data
    #   if errors were found. I need to source raw data that has errors to properly determine common
    #                                            errors.
    #    that needs fixed. I will then use the DataFrame created to clean and export the clean data.
    #           if any input from the user is other than yes or no, a ValueError is raised.

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

    # Prompts the user if they want to create a frictionless data package and 'README.md'.
    # If user says yes, it calls CREATE_DATA_PACKAGE and CREATE_README with the output
    # directory of the current directory and a newly created folder called data-package in it.
    #               Any input other than yes or no raises a ValueError.

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

        # Prompts the user if they want to repeat the program. If user says no,
        #                       the program will end.

    repeat_program = input("Do you want to enter another file? (yes/no) ").lower()
    if repeat_program == 'no':
        break

