import pandas as pd

def process_edu(week,sheet_name=0):
    """
    This function is meant to process Table 4 of the Household Pulse Survey edu spreadsheets into clean, usable data. It takes the arguments:
    
    1. week(string) - The week of the data sheet to be processed
    2. sheet_name(str,int) - The sheet to be processed.
    
    """
    edu = pd.read_excel('../data/edu/educ4_week' + str(week) + '.xlsx', sheet_name=sheet_name, skip_rows=[0,1,2], header=[5], index_col=0,skipfooter=1, nafilter=False, keep_default_na=False)
    edu.index = edu.index.str.strip()
    
    edu.rename(columns={'Unnamed: 1' : 'Total',
                    'Unnamed: 2' : 'Provided by the children’s school or school district to use outside of school(device)',
                    'Unnamed: 3':'Provided by someone in the household or family, or it is the child’s(device)',
                    'Unnamed: 4' : 'Provided by another source(device)','Unnamed: 5' : 'Did not report(device)',
                    'Unnamed: 6' : 'Paid for by the children’s school or school district(internet)',
                    'Unnamed: 7' : 'Paid for by someone in the household or family(internet)',
                    'Unnamed: 8' : 'Paid for by another source(internet)', 'Unnamed: 9' : 'Did not report(internet)'},
                     level=0,inplace=True)
    edu.drop(['Age','Sex','Hispanic origin and Race','Education', 'Marital status' , 'Presence of children under 18 years old',
                  'Respondent or household member experienced loss of employment income',
                  'Respondent currently employed','Food sufficiency for households prior to March 13, 2020','Household income'                 ], axis=0,inplace=True)
    #  Jupyter thinks the double $ signals a MathJax equation. Escape them with \
    edu.index = ['Total', '18 - 24', '25 - 39', '40 - 54', '55 - 64', '65 and above',
                   'Male', 'Female', 'Hispanic or Latino (may be of any race)',
                   'White alone, not Hispanic', 'Black alone, not Hispanic',
                   'Asian alone, not Hispanic',
                   'Two or more races + Other races, not Hispanic',
                   'Less than high school', 'High school or GED',
                   'Some college/associate’s degree', 'Bachelor’s degree or higher',
                   'Married', 'Widowed', 'Divorced/separated', 'Never married',
                   'Did not report marriage status', 'Children in household', 'No children', 'Respondent or household member experienced loss of employment income : Yes',
                   'Respondent or household member experienced loss of employment income : No','Did not report loss of employment income',
                   'Currently employed: Yes', 'Currently employed: No',
                   'Did not report employment status', 'Enough of the types of food wanted(prior to March 13, 2020)',
                   'Enough food, but not always the types wanted(prior to March 13, 2020)',
                   'Sometimes not enough to eat(prior to March 13, 2020)', 'Often not enough to eat(prior to March 13, 2020)',
                   'Did not report food sufficiency', 'Less than \\$25,000', '\\$25,000 - \\$34,999',
                   '\\$35,000 - \\$49,999', '\\$50,000 - \\$74,999', '\\$75,000 - \\$99,999',
                   '\\$100,000 - \\$149,999', '\\$150,000 - \\$199,999', '\\$200,000 and above',
                   'Did not report income']
    
    edu.replace('-', 0,inplace=True) # replace values that are not ints
    edu['Total device(not including DNR)'] = edu['Total'].astype(int) - edu.iloc[:,4].astype(int)
    edu['Total internet(not including DNR)'] = edu['Total'].astype(int) - edu.iloc[:,8].astype(int)

    
    # calculate percentages for relevant column
    col_list = edu.columns.tolist()
    for column in col_list[1:4]:
        edu['% ' + column] = edu[column] / edu['Total device(not including DNR)']
    
    for column in col_list[5:8]:
        edu['% ' + column] = edu[column] / edu['Total internet(not including DNR)']
        
    #  Modify the column ordering so that the graphs are consistent and pretty
    edu = edu[['Total',
               'Provided by the children’s school or school district to use outside of school(device)',
               'Provided by someone in the household or family, or it is the child’s(device)',
               'Provided by another source(device)',
               'Did not report(device)',
               'Paid for by the children’s school or school district(internet)',
               'Paid for by someone in the household or family(internet)',
               'Paid for by another source(internet)',
               'Did not report(internet)',
               'Total device(not including DNR)',
               'Total internet(not including DNR)',
               '% Provided by someone in the household or family, or it is the child’s(device)',
               '% Provided by the children’s school or school district to use outside of school(device)',
               '% Provided by another source(device)',
               '% Paid for by someone in the household or family(internet)',
               '% Paid for by the children’s school or school district(internet)',
               '% Paid for by another source(internet)']]


    return edu
