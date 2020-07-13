#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def process_food(data,sheet_name=0):
    """
    This function is meant to process Table 4 of the Household Pulse Survey food spreadsheets into clean, usable data. It takes the arguments:
    
    1. data(str) - The spreadhseet to be processed.
    2. sheet_name(str,int) - The sheet to be processed.
    
    Once it is necessary to analyze the data temporally, this function will determine what week the data is from by the spreadsheet name and run the appropriate code.
    
    """
    food = pd.read_excel('../data/' + data +'.xlsx', sheet_name=sheet_name, skip_rows=[0,1,2], header=[4], index_col=0,skipfooter=1, nafilter=False, keep_default_na=False)
    food = food.iloc[:, :5]
    food.index = food.index.str.strip()
    food.drop(['','Food Sufficiency before Mar 13, 2020','Reason for recent food insufficiency *','Free groceries or free meal in last 7 days','Provider of free groceries or free meal *',
           'Food-at-home', 'Food-away-from-home', 'Confidence in being able to afford food next four weeks',
           'Health status','Frequency of feeling nervous, anxious, on edge','Frequency of not being able to stop or control worrying',
           'Frequency of having little interest or pleasure in doing things', 'Used in the last 7 days to meet spending needs*',], axis=0,inplace=True)
    food.index = ['Total', 'Enough of the types of food wanted(before Mar 13, 2020)',
       'Enough food, but not always the types wanted(before Mar 13, 2020)',
       'Sometimes not enough to eat(before Mar 13, 2020)', 'Often not enough to eat(before Mar 13, 2020)',
       'Did not report food sufficiency prior to Mar 13', 'Couldn’t afford to buy more food',
       'Couldn’t get out to buy food',
       'Afraid to go or didn’t want to go out to buy food',
       'Couldn’t get groceries or meals delivered to me',
       'The stores didn’t have the food I wanted', 'Did not report reason for recent food insufficency', 'Free groceries/meals: Yes',
       'Free groceries/meals: No', 'Did not report free groceries or meals', 'School or other programs aimed at children',
       'Food pantry or food bank',
       'Home-delivered meal service like Meals on Wheels',
       'Church, synagogue, temple, mosque or other religious organization',
       'Shelter or soup kitchen', 'Other community program',
       'Family, friends, or neighbors', 'Did not report provider of free grocieries/meals',
       'Food-at-home(Mean amount dollars)', 'Did not report food-at-home spending',
       'Food-away-from-home(Mean amount dollars)', 'Did not report food-away-from-home spending', 'Not at all confident',
       'Somewhat confident', 'Moderately confident', 'Very confident',
       'Did not report confidence in being able to afford food for the next four weeks', 'Excellent', 'Very good', 'Good', 'Fair', 'Poor',
       'Did not report health status', 'Not at all', 'Several days',
       'More than half the days', 'Nearly every day', 'Did not report frequency of feeling nervous, anxious, on edge',
       'Not at all', 'Several days', 'More than half the days',
       'Nearly every day', 'Did not report frequency of not being able to stop or control worrying', 'Not at all', 'Several days',
       'More than half the days', 'Nearly every day', 'Did not report frequency of having little interest or pleasure in doing things',
       'Regular income sources like those used before the pandemic',
       'Credit cards or loans', 'Money from savings or selling assets',
       'Borrowing from friends or family',
       'Unemployment insurance (UI) benefit payments',
       'Stimulus (economic impact) payment',
       'Money saved from deferred or forgiven payments (to meet spending needs)',
       'Did not report what used in last 7 days to meet spending needs']
    food.rename(columns={'Unnamed: 1':'Total(including did not report)'},inplace=True)
    food.replace('-', 0,inplace=True)
    food['Total'] = food['Total(including did not report)'].astype(int) - food['Did not report'].astype(int)
    col_list = food.columns.tolist()
    for column in col_list[1:4]:
        food['% ' + column] = food[column] / food['Total']

    return food
