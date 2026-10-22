# iam-user-access-auditor

## What it does:
Tool that reads a CSV of users (and respective roles, departments, and account status). 
Then performs 5 different checks to ensure there are no mistakes or excess privileges given to active users.

Flags problems such as duplicate accounts, disabled accounts that still have access, excess privileges, and more.

## How to run it:
- This project is run from the main project folder.
- Ensure you have a csv file in "iam-user-access-auditor/data".
- Run from your terminal using "python src/auditor.py".
- Edit rules as necessary in  "config/rules.json".
- Output will be written to output.txt in the main folder.

## What it checks for:
1. If there are matching results for different users in 'unique' fields (i.e., shared user id's, emails, etc.).

2. If there are inactive accounts that still hold privileges. (i.e., disabled account with admin privilege)

3. If there are missing values in 'required' fields (i.e., no user id)

4. If there are users with more than X roles. Where X has a default value of 4.

5. If there are users who hold privileges for departments they are not a part of (i.e., a Sales worker with Domain_Admin permissions)

## This is the output of the sample_users.csv when running this code:

```
No duplicate user_ids found.
Email 'maria.lopez@contoso-demo.com' shared by: U1004 and U1019

Inactive account(s) found with active permissions: U1008, U1015, U1022

User U1013 missing required field(s): email
User U1017 missing required field(s): department
User U1029 missing required field(s): account_status

U1026 has more than 4 roles, with 6 active roles.

User U1018 in Sales has excess role of: Admin
User U1023 in Sales has excess role of: Domain_Admin
User U1025 in HR has excess role of: Admin
User U1026 in IT has excess role of: Finance_Viewer
User U1026 in IT has excess role of: HR_Viewer
User U1026 in IT has excess role of: CRM_User
```

## Notes:
- All of the information within sample_users.csv is completely fake and for testing purposes
- For future features I would like to add a UI for easier manipulation of csv files, and move more hardcoded values out of the code and into '/rules.json'.

