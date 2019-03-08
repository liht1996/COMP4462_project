import pandas as pd
import numpy as np



def load():
    df = pd.read_csv("crime.csv", engine='python', parse_dates = ['OCCURRED_ON_DATE'], index_col = ['INCIDENT_NUMBER'])
    print("Load successfully. The shape is ")
    print(df.shape)
    return df

def clean(df):
    df['SHOOTING'] = df['SHOOTING'].fillna("N")
    df_clean = df.dropna(axis = 0)
    print("Clean successfully. The shape is ")
    print(df_clean.shape)
    return df_clean

def group(offense):
    group_dict = {
        'Traffic': ['Motor Vehicle Accident Response', 'Towed'],
        'Property': ['Larceny', 'Vandalism', 'Larceny From Motor Vehicle', 'Property Lost', 
                     'Residential Burglary', 'Property Related Damage', 'Auto Theft', 
                     'Robbery', 'Other Burglary', 'Burglary - No Property Taken'],
        'Assault': ['Simple Assault', 'Aggravated Assault', 'Harassment', 'Offenses Against Child / Family', 
                    'Criminal Harassment', 'Homicide', 'Manslaughter'],
        'Dispute': ['Verbal Disputes', 'Landlord/Tenant Disputes'],
        'Violations': ['Drug Violation', 'Firearm Violations', 'Violations', 'License Violation', 
                       'Restraining Order Violations', 'Liquor Violation', 'Assembly or Gathering Violations'],
        'Public Safety': ['Disorderly Conduct', 'Ballistics', 'Firearm Discovery', 'Arson', 'Explosives',
                          'Biological Threat'],
        'Public Affair': ['Medical Assistance', 'Warrant Arrests', 'Investigate Person', 'Investigate Property', 
                          'Police Service Incidents', 'Fire Related Reports', 'Search Warrants', 
                          'License Plate Related Incidents', 'Prisoner Related Incidents', 'Service'],
        'Fraud': ['Fraud', 'Confidence Games', 'Counterfeiting', 'Commercial Burglary', 'Embezzlement'],
        'Other': ['Other', 'Missing Person Located', 'Missing Person Reported', 'Property Found', 
                  'Recovered Stolen Property', 'Auto Theft Recovery', 'Operating Under the Influence', 
                  'Evading Fare', 'Prostitution', 'Harbor Related Incidents', 'Bomb Hoax', 'Phone Call Complaints', 
                  'Aircraft', 'Gambling']}
    
    for key in group_dict.keys():
        if offense in group_dict[key]:
            return key
        
    return np.nan

def load_clean_group():
    df_clean = clean(load())
    df_clean['OFFENSE_GROUP'] = df_clean['OFFENSE_CODE_GROUP'].apply(group)
    print("Group successfully")
    return df_clean