from checks.duplicates import find_duplicate
from checks.disabled_access import inactive_roles
from checks.required_fields import required_fields
from checks.too_many_roles import excess_roles
from checks.wrong_roles import find_wrong_roles
import json

outputPath = "output.txt"
jsonPath = "config/rules.json"
csvPath = "data/sample_users.csv"

#   Simple function for adding newlines between rules
def end_space():
    with open(
        outputPath,
        "a"
) as outputFile:
        outputFile.write("\n")

#   Clear the output file at the start of the test
with (open(
        outputPath,
        "w"
) as outputFile):
    pass



'''
Test 1: Testing for the same results in unique fields (i.e., email, user ID, etc).
'''
#   Opening the json file
with open(jsonPath, "r") as jsonFile:
    jsonData = json.load(jsonFile)  #   Assigns json file to a dictionary

    #   Checks for duplicate in each field defined in the JSON
    for field in jsonData["no_duplicate_fields"]:
        find_duplicate(field, csvPath)
end_space()

'''
Test 2: Testing for accounts with which are inactive but still have access.
'''

inactive_roles(csvPath)
end_space()
'''
Test 3: Testing for missing values in required fields (i.e., a blank user id).
'''
for field in jsonData["required_fields"]:
    required_fields(field,csvPath)
end_space()

'''
Test 4: Testing for users with more than X roles, where X is defined in the JSON.
'''
maxRoles = jsonData["max_roles"]
excess_roles(csvPath, maxRoles)
end_space()
'''
Test 5: Testing for users with roles outside of their department
'''


find_wrong_roles(csvPath, jsonData["department_roles"])
end_space()


