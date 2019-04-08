import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords



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

def clean_tokenize(string):
    """
        Tokenization/string cleaning for datasets.
        :param string: a doc with multiple sentences, type: str
        return a word list, type: list
        e.g.
        Input: 'It is a nice day. I am happy.'
        ['it', 'is', 'a', 'nice', 'day', 'i', 'am', 'happy']
        """
#     string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string) # remove non alphabet, non digit, non punctuation
    string = re.sub(r"[^A-Za-z]", " ", string)
    string = re.sub(r"\'s", " \'s", string) # add a space before \'s
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string) #remove multiple spaces
    word_list = string.strip().lower().split() #strip "\n", convert to lower case, split string
    return  [word for word in word_list if word not in stopwords.words('english')] #remove stopwords
def load_clean_group():
    df_clean = clean(load())
    df_clean['OFFENSE_GROUP'] = df_clean['OFFENSE_CODE_GROUP'].apply(group)
    df_clean['OFFENSE_DESCRIPTION_WORDS'] = df_clean['OFFENSE_DESCRIPTION'].apply(clean_tokenize)
    print("Group successfully")
    return df_clean
