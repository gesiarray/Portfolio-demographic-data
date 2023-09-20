import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
  df = pd.read_csv('adult.data.csv')
  

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

    # What is the average age of men?
  average_age_men = round(df[df['sex'] == 'Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
  Bachelor_dg = df['education'] == 'Bachelors'
  Bachelor_dg_total = Bachelor_dg.sum()

  educated_total = df['education'].value_counts().sum()
  percentage_bachelors = round(Bachelor_dg_total / educated_total * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_edu = ['Bachelors','Masters','Doctorate']
  higher_education = df[df['education'].isin(higher_edu)]
  higher_education_df = higher_education[higher_education['salary']=='>50K']

  lower =['HS-grad', '11th', '9th', 'Some-college', 'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Prof-school', '5th-6th', '10th', '1st-4th', 'Preschool', '12th']
  lower_edu = df[df['education'].isin(lower)]
  lower_education = lower_edu[lower_edu['salary'] == '>50K']
  

    # percentage with salary >50K
  higher_education_rich = round(higher_education_df.shape[0]/higher_education.shape[0]*100,1)
  
  lower_education_rich = round(lower_education.shape[0]/lower_edu.shape[0]*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  min_hours_workers = df[df['hours-per-week'] == min_work_hours]
  min_hrs_salary = min_hours_workers[min_hours_workers['salary'] == '>50K']
  rich_percentage = round(min_hrs_salary.shape[0]/min_hours_workers.shape[0]*100,1)


    # What country has the highest percentage of people that earn >50K?
  country_income_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
  total_people_per_country = df['native-country'].value_counts()
  percentage_high_income = round((country_income_counts / total_people_per_country)*100,1)
  
  highest_earning_country = percentage_high_income.idxmax()
  highest_earning_country_percentage = percentage_high_income.max()

    # Identify the most popular occupation for those who earn >50K in India.
  india_df = df[df['native-country'] == 'India']
  india_df1 = india_df[india_df['salary']=='>50K']
  india_df1['count'] = 1

  top_india_occupation = india_df1.groupby(['occupation']).sum().reset_index()[['occupation','count']].sort_values(by='count',ascending=False)
  top_india_occupation.reset_index(inplace=True)
  top_IN_occupation= top_india_occupation.loc[0,'occupation']

    # DO NOT MODIFY BELOW THIS LINE

  if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

  return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
