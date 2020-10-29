"""
Imagine a school that children attend for years. In each year, there are a certain number of groups started, marked with the letters. So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the last year, the groups are 7a, 7b, 7c, 7d.

Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

Examples:

csSchoolYearsAndGroups(years = 7, groups = 4) ➞ "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"

Notes:

1 <= years <= 10
1 <= groups <=26
[execution time limit] 4 seconds (py3)

[input] integer years

[input] integer groups

[output] string
"""

import string 

def csSchoolYearsAndGroups(years, groups):
    letter_groups = string.ascii_lowercase[0: groups]
    i = 1
    classes = []
    while i <= years:
        groups_list = [f"{i}{g}" for g in letter_groups]
        string_groups_list = ', '.join([str(item) for item in groups_list ])
        classes.append(string_groups_list)
        i += 1
    string_classes = ', '.join([str(item) for item in classes ])

    return string_classes
    
print(csSchoolYearsAndGroups(years = 7, groups = 4))
print(csSchoolYearsAndGroups(years = 10, groups = 7))
print(csSchoolYearsAndGroups(years = 7, groups = 18))
print(csSchoolYearsAndGroups(years = 4, groups = 25))
print(csSchoolYearsAndGroups(years = 6, groups = 26))
