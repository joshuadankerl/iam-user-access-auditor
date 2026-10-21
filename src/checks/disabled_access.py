import csv

'''
Function for checking if any disabled accounts have roles/permissions
'''
def inactive_roles(path):

    #   Opens CSV file in read-only mode
    with (open(
        path,
        "r"
    ) as csvFile):
        data = csv.DictReader(csvFile)


        inactiveAccounts = []   #   For accounts with disabled status
        blankAccounts = []  #   For accounts with no occupied status field

        #   Looping through each account_status
        for row in data:
            status = row["account_status"]

            if status.strip().lower() == "disabled" and row["roles"].strip():
                inactiveAccounts.append(row["user_id"].strip())

            elif not status.strip():
                blankAccounts.append(row["user_id"].strip())

        with open(
                "output.txt",
                "a"
        ) as outputFile:
            if inactiveAccounts:
                outputFile.write(
                    f"Inactive account(s) found with active permissions:\n{', '.join(inactiveAccounts)}\n\n"
                )
            elif blankAccounts:
                outputFile.write(
                    f"Account(s) found with no status:\n {', '.join(blankAccounts)}\n\n"
                )
            else:
                outputFile.write(f"No inactive account(s) found with permissions.\n\n")