import csv

def required_fields(field, csvPath):

    #   Open CSV file in read-only
    with open(
            csvPath,
            "r"
    ) as csvFile:
        csvData = csv.DictReader(csvFile)  #   Assigns csv data to dictionary

        #   Cycles through each row of data
        for row in csvData:

            #   Statement for finding blank fields (which are required)
            if not row[field].strip():  # If row is blank or only spaces
                with open(
                        "output.txt",
                        "a"
                ) as outputFile:

                    #   Print of required fields found missing
                    outputFile.write(
                        f"User {row['user_id'].strip()} missing required field(s): {field}\n"
                    )
    return
