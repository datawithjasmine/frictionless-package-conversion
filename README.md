# frictionless-package-conversion

## Table of Contents

[Project Overview](#project-overview)\
[Frictionless Data](#frictionless-data)\
[Limitations](#limitations)\
[Future Implementations](#future-implementations)\
[References](#references)

### Project Overview

I built a python script that creates a frictionless data package from a data file, commonly in .csv format. The result is a folder that contains the data package file and a 'README.md' file for further instructions.

### Frictionless Data

According to [frictionless data](frictionlessdata.io), a data package file is a collection of data files that aim to describe and package the dataset. It helps with reducing workflow issues in data, thus the name 'frictionless'. The ``` frictionless ``` library is imported so that users can describe, validate, transform data and many other cases. This allows users to use these packages without the hassle of dealing with bad data. 

### Limitations

While the program allows you to find errors, the functionality to properly clean the data is not available at the current moment. 

### Future Implementations

I plan to include different functionalities such as the inclusion of other data files and the ability to clean data before packaging it.

### References

(https://frictionlessdata.io/) \
(https://framework.frictionlessdata.io/) \
(https://framework.frictionlessdata.io/docs/framework/package.html)

