import pandas as pd

data = pd.read_excel('bmsagents.xlsx')

insert_statements = []
for index, row in data.iterrows():
    insert_statement = f"INSERT INTO BIMAS_MBS.BMS_AGENTS (ID, FIRST_NAME, MIDDLE_NAME, LAST_NAME, MSISDN, EMAIL, COUNTY_ID, BRANCH_ID, STATUS, DATE_CREATED, USERNAME, CREATED_BY, INTRASH, RESET_TOKEN, PROFILE_PIC, CBS_OFFICER_NAME, ASSINGED_GROUPS, IMEI) VALUES (BIMAS_MBS.BMS_AGENTS_SEQ.NEXTVAL, '{row['FIRST_NAME']}', '{row['MIDDLE_NAME']}', '{row['LAST_NAME']}', '{row['MSISDN']}', '{row['EMAIL']}', {row['COUNTY_ID']}, {row['BRANCH_ID']}, '{row['STATUS']}', TO_DATE('{row['DATE_CREATED']}', 'YYYY-MM-DD HH24:MI:SS'), '{row['USERNAME']}', '{row['CREATED_BY']}', '{row['INTRASH']}', '{row['RESET_TOKEN']}', '{row['PROFILE_PIC']}', '{row['CBS_OFFICER_NAME']}', '{row['ASSINGED_GROUPS']}', '{row['IMEI']}');"
    insert_statements.append(insert_statement)

#save 
with open('output.sql', 'w') as file:
    file.write("\n".join(insert_statements))

print("welcome")
