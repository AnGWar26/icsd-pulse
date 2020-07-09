# icsd-pulse

This project aims to analyze the Household Pulse Survey Data across several dimensions in order to gain insight into COVID-19's impact on different demographics. In addition to answering the questions below, we will also analyze the the effects of COVID-19 by race/ethnicity on each of the dimensions offered by the Household Pulse Survey. All of these questions will be analyzed at the spatial scale of the nation, the nation's 15 biggest MSAs, and will be analyzed temporally across all weeks the Census Bureau has released data.

#### Create the environment
In order to create the environment, you will require conda.
1. Run `git clone https://github.com/AnGWar26/icsd-pulse.git`
2. Run `conda env create -f environment.yml`
3. After conda has finished resolving the packages run `conda activate icsd-pulse`

#### Questions
* What is the distribution of families in each food security band depending on the methods they used to fulfill their spending needs?
* How does mental health vary by age?
	* Create a "mental health index" by adding together average response for each question.
* How has the education of kids been impacted in the age of COVID-19 by the level of education achieved by their parents?