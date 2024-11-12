import csv
import pandas as pd
import numpy as np


def get_feedback_counts():
    path = 'dataset/teacherdb.csv'
    df = pd.read_csv(path)
    index = df.index
    no_of_feedbacks = len(index)
    total_feedbacks = len(index)*6

    df1 = df.groupby('Madhura_score').count()[['Madhura']]
    Madhura_negative_count = df1['Madhura'][-1]
    Madhura_neutral_count = df1['Madhura'][0]
    Madhura_positive_count = df1['Madhura'][1]

    df1 = df.groupby('Ravi_score').count()[['Ravi']]
    Ravi_negative_count = df1['Ravi'][-1]
    Ravi_neutral_count = df1['Ravi'][0]
    Ravi_positive_count = df1['Ravi'][1]

    df1 = df.groupby('Chaitra_score').count()[['Chaitra']]
    Chaitra_negative_count = df1['Chaitra'][-1]
    Chaitra_neutral_count = df1['Chaitra'][0]
    Chaitra_positive_count = df1['Chaitra'][1]

    df1 = df.groupby('Aishwarya_score').count()[['Aishwarya']]
    Aishwarya_negative_count = df1['Aishwarya'][-1]
    Aishwarya_neutral_count = df1['Aishwarya'][0]
    Aishwarya_positive_count = df1['Aishwarya'][1]

    df1 = df.groupby('Kiran_score').count()[['Kiran']]
    Kiran_negative_count = df1['Kiran'][-1]
    Kiran_neutral_count = df1['Kiran'][0]
    Kiran_positive_count = df1['Kiran'][1]

    df1 = df.groupby('Gurudhath_score').count()[['Gurudhath']]
    Gurudhath_negative_count = df1['Gurudhath'][-1]
    Gurudhath_neutral_count = df1['Gurudhath'][0]
    Gurudhath_positive_count = df1['Gurudhath'][1]

    total_positive_feedbacks = Madhura_positive_count + Ravi_positive_count + Chaitra_positive_count + Aishwarya_positive_count + Kiran_positive_count + Gurudhath_positive_count
    total_neutral_feedbacks = Madhura_neutral_count + Ravi_neutral_count + Chaitra_neutral_count + Aishwarya_neutral_count + Kiran_neutral_count + Gurudhath_neutral_count
    total_negative_feedbacks = Madhura_negative_count + Ravi_negative_count + Chaitra_negative_count +Aishwarya_negative_count + Kiran_negative_count + Gurudhath_negative_count

    li = [Madhura_positive_count,Madhura_negative_count,Madhura_neutral_count,
          Ravi_positive_count,Ravi_negative_count,Ravi_neutral_count,
          Chaitra_positive_count,Chaitra_negative_count,Chaitra_neutral_count,
          Aishwarya_positive_count,Aishwarya_negative_count,Aishwarya_neutral_count,
          Kiran_positive_count,Kiran_negative_count,Kiran_neutral_count,
          Gurudhath_positive_count,Gurudhath_negative_count,Gurudhath_neutral_count]


    return no_of_feedbacks,\
           int(round(total_positive_feedbacks / total_feedbacks * 100)),\
           int(round(total_negative_feedbacks / total_feedbacks * 100)),\
           int(round(total_neutral_feedbacks / total_feedbacks * 100)),\
            li


