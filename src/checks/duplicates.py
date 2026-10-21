import csv

'''
Function for comparing values in the same column of a CSV file
'''
def find_duplicate(columnValue, csvPath):

        #   Open the CSV File in read-only mode
        with open(
                csvPath,
                "r"
        ) as csvFile:

            #   Assign csv data to dictionary
            data = csv.DictReader(csvFile)
            values = []
            ids_by_value = {}

            #   Append each item to 'values'
            for row in data:
                item = row[columnValue].strip() #   Strips whitespace

                if item:   #   Skips empty strings
                    values.append(item)
                    ids_by_value.setdefault(item, []).append(row["user_id"].strip())




        #   Sort the values for comparison
        values = sorted(values)
        duplicates = {}


        #   Comparing values to find a duplicate
        for i in range(len(values) - 1):
            if values[i].lower() == values[i + 1].lower():  #   Compares both values to check if the same
                duplicates[values[i]] = ids_by_value[values[i]]     #   Assigns the duplicate to my dictionary containing the Uid


        #   Record test results into output.txt
        with open(
                "output.txt",
                "a"
        ) as outputFile:

            #   Records duplicates found
            if duplicates:  #   If duplicate found
                for value, ids in duplicates.items():   #   grabs email, and user_id(s)
                    outputFile.write(
                        f"{columnValue.title()} '{value}' shared by: {', '.join(ids)}\n\n"
                    )
            else:   #   If no duplicate is found
                outputFile.write(f"No duplicate {columnValue}s found.\n\n")

        csvFile.close()
        outputFile.close()
        return


