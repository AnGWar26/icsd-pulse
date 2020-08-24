import pandas as pd

def process_emp(week,sheet_name=0):
    """
    This function is meant to process Table 4 of the Household Pulse Survey edu spreadsheets into clean, usable data. It takes the arguments:
    
    1. week(string) - The week of the data sheet to be processed
    2. sheet_name(str,int) - The sheet to be processed.
    
    """
    
    if int(week) in range(1,7):
        emp = pd.read_excel('../data/emp/employ1_week' + str(week) + '.xlsx', sheet_name=sheet_name, skip_rows=[0,1,2],
                            header=[3,4], index_col=0, nafilter=False, keep_default_na=False)

    else:
        emp = pd.read_excel('../data/emp/employ1_week' + str(week) + '.xlsx', sheet_name=sheet_name, skip_rows=[0,1,2],
                            header=[3,4], index_col=0, skipfooter=1, nafilter=False, keep_default_na=False)

    emp.rename(columns={'Unnamed: 1_level_1':'Total'},level=1,inplace=True)
    #whitespace in the index names from the spreadsheet make things hard to work with
    emp.index = emp.index.str.strip()
    
    if int(week) in range(1,7):
        emp.drop(['Age','Sex','Hispanic origin and Race','Education', 'Marital status' ,
                  'Presence of children under 18 years old', 'Health status','Household income'
         ], axis=0,inplace=True)
        emp.index = ['Total', '18 - 24', '25 - 39', '40 - 54', '55 - 64', '65 and above',
        'Male', 'Female', 'Hispanic or Latino (may be of any race)',
       'White alone, not Hispanic', 'Black alone, not Hispanic',
       'Asian alone, not Hispanic',
       'Two or more races + Other races, not Hispanic',
       'Less than high school', 'High school or GED',
       'Some college/associate’s degree', 'Bachelor’s degree or higher',
       'Married', 'Widowed', 'Divorced/separated', 'Never married',
       'Did not report marriage status',
       'Children in household', 'No children', 'Excellent', 'Very good',
       'Good', 'Fair', 'Poor', 'Did not report health status',
       'Less than \\$25,000', '\\$25,000 - \\$34,999',
       '\\$35,000 - \\$49,999', '\\$50,000 - \\$74,999', '\\$75,000 - \\$99,999',
       '\\$100,000 - \\$149,999', '\\$150,000 - \\$199,999', '\\$200,000 and above',
        'Did not report income']
    else:
        emp.drop(['Age','Sex','Hispanic origin and Race','Education', 'Marital status' ,
                  'Presence of children under 18 years old', 'Health status','Household income',
                  'Used in the last 7 days to meet spending needs*', 'Household size'
           ], axis=0,inplace=True)
        emp.index = ['Total', '18 - 24', '25 - 39', '40 - 54', '55 - 64', '65 and above',
        'Male', 'Female', 'Hispanic or Latino (may be of any race)',
       'White alone, not Hispanic', 'Black alone, not Hispanic',
       'Asian alone, not Hispanic',
       'Two or more races + Other races, not Hispanic',
       'Less than high school', 'High school or GED',
       'Some college/associate’s degree', 'Bachelor’s degree or higher',
       'Married', 'Widowed', 'Divorced/separated', 'Never married',
       'Did not report marriage status',
       '1 person in the household', '2 people in the household',
       '3 people in the household','4 people in the household',
       '5 people in the household','6 people in the household','7 or more people in the household',
       'Children in household', 'No children', 'Excellent', 'Very good',
       'Good', 'Fair', 'Poor', 'Did not report health status',
       'Less than \\$25,000', '\\$25,000 - \\$34,999',
       '\\$35,000 - \\$49,999', '\\$50,000 - \\$74,999', '\\$75,000 - \\$99,999',
       '\\$100,000 - \\$149,999', '\\$150,000 - \\$199,999', '\\$200,000 and above',
       'Did not report income', 'Regular income sources like those used before the pandemic',
       'Credit cards or loans', 'Money from savings or selling assets',
       'Borrowing from friends or family', 'Unemployment insurance (UI) benefit payments',
       'Stimulus (economic impact) payment', 'Money saved from deferred or forgiven payments (to meet spending needs)',
       'Did not report']
    # Applies to all dataframes
    emp.replace('-', 0,inplace=True) # replace values that are not ints
    #init the columns or else it errors
    emp['Total Experienced loss of employment income since March 13, 2020'] = 0
    emp['Total Expected loss of employment income in next 4-weeks'] = 0
    #calc looks ugly but do the job
    emp['Total Experienced loss of employment income since March 13, 2020'] = emp.Total.values - emp.iloc[:,3].to_numpy()
    emp['Total Expected loss of employment income in next 4-weeks'] = emp.Total.values - emp.iloc[:,3].to_numpy()
    
    col_list = emp.columns.tolist()
    for column in col_list[1:3]:
        emp['% ' + str(column)] = emp[column] / emp['Total Experienced loss of employment income since March 13, 2020']
    
    for column in col_list[4:6]:
        emp['% ' + str(column)] = emp[column] / emp['Total Expected loss of employment income in next 4-weeks']\
    
    return emp
    