from checks.duplicates import find_duplicate
from checks.disabled_access import inactive_roles
from checks.required_fields import required_fields
from checks.excessive_privilege import excess_roles
import json


csvPath = "data/sample_users.csv"

# Clear the output file at the start of the test
with (open(
        "output.txt",
        "w"
) as outputFile):
    pass



'''
Test 1: Testing for the same results in unique fields (i.e., email, user ID, etc).
'''
#   Opening the json file
with open("config/rules.json", "r") as jsonFile:
    jsonData = json.load(jsonFile)  #   Assigns json file to a dictionary

    #   Checks for duplicate in each field defined in the JSON
    for field in jsonData["no_duplicate_fields"]:
        find_duplicate(field, csvPath)


'''
Test 2: Testing for accounts with which are inactive but still have access.
'''

inactive_roles(csvPath)

'''
Test 3: Testing for missing values in required fields (i.e., a blank user id).
'''
for field in jsonData["required_fields"]:
    required_fields(field,csvPath)


'''
Test 4: Testing for users with more than X roles, where X is defined in the JSON.
'''
maxRoles = jsonData["max_roles"]
excess_roles(csvPath, maxRoles)


jsonFile.close()
outputFile.close()
