import csv

def excess_roles(csvPath, maxRoles):
    with open(
        csvPath,
        "r"
    ) as csvFile:


        users = {}  #   Creates dictionary for UID and num of roles
        for row in csv.DictReader(csvFile): #   Creates dictionary for CSV data

            roles = row["roles"].split(";") #   Seperate roles by semicolon

            #   If more roles than the max
            if len(roles) > maxRoles:
                users[row["user_id"].strip()] = len(roles)  #   Assigns UID and num roles into dictionary

        #   If user is found with more than X roles
        if users:
            with open(
                    "output.txt",
                    "a"
            ) as outputFile:
                #   Writes the UID and num roles to output txt
                outputFile.write(
                    f"\n{row["user_id"]} has more than {maxRoles} roles\n"
                )
    return



