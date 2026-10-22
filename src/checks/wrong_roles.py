import csv

'''
Function for ensuring a user has the roles of only their department
'''
def find_wrong_roles(csvPath, departmentRoles):

    #   Opens csv data table in read-only mode
    with open(
            csvPath,
            "r",
    ) as csvFile:

        #   Loops through each row of data (for each user)
        for row in csv.DictReader(csvFile):

            allowedRoles = departmentRoles.get(row["department"]) #   Grabs the user's department
            roles = row["roles"].split(";") #   Makes a list of roles the user has

            #   For blank or mislabeled departments
            if allowedRoles is None:
                continue

            #   Comparing active roles to department-specific roles
            for role in roles:
                role = role.strip()

                #   For empty rows
                if not role:
                    continue

                #   In the case a role is not within their department
                if role not in allowedRoles:

                    with open(
                        "output.txt",
                        "a"
                    ) as outputFile:
                        outputFile.write(
                            f"User {row['user_id'].strip()} in {row["department"]} has excess role of: {role}\n"
                        )
    return





