import csv
import pandas as pd
import numpy as np



def write_to_csv_departments(time,teachingscore,teaching,courseContentscore,courseContent,
                 examinationscore,examination,labWorkscore,labWork,libraryFacilitiesscore,
                 libraryFacilities,extraCurricularscore,extraCurricular,username):

    with open('dataset/database.csv', 'r') as f:
        reader = csv.reader(f)
        for header in reader:
            break
    with open('dataset/database.csv', "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        dict = {'Timestamp': time, 'teachingscore': teachingscore, 'teaching': teaching,
                'coursecontentscore': courseContentscore, 'coursecontent': courseContent,
                'examinationscore': examinationscore, 'examination': examination,
                'labworkscore': labWorkscore, 'labwork': labWork,'libraryfacilitiesscore': libraryFacilitiesscore,
                'libraryfacilities': libraryFacilities, 'extracurricularscore': extraCurricularscore,
                'extracurricular': extraCurricular, 'username': username}
        writer.writerow(dict)



def write_to_csv_teachers(Madhura,Madhura_score,Ravi,Ravi_score,Chaitra,Chaitra_score,
                          Aishwarya,Aishwarya_score,Kiran,Kiran_score,Gurudhath,Gurudhath_score):
    with open('dataset/teacherdb.csv', 'r') as f:
        reader = csv.reader(f)
        for header in reader:
            break
    with open('dataset/teacherdb.csv', "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        dict = {'Madhura': Madhura, 'Madhura_score': Madhura_score,
                'Ravi': Ravi,'Ravi_score': Ravi_score,
                'Chaitra': Chaitra, 'Chaitra_score': Chaitra_score,
                'Aishwarya': Aishwarya, 'Aishwarya_score': Aishwarya_score,
                'Kiran': Kiran, 'Kiran_score': Kiran_score,
                'Gurudhath': Gurudhath, 'Gurudhath_score': Gurudhath_score
               }
        writer.writerow(dict)




def get_counts():
    path = 'dataset/database.csv'
    df = pd.read_csv(path)
    index = df.index
    no_of_students = len(index)
    total_feedbacks = len(index)*6

    df1 = df.groupby('teachingscore').count()[['teaching']]
    teaching_negative_count = df1['teaching'][-1]
    teaching_neutral_count = df1['teaching'][0]
    teaching_positive_count = df1['teaching'][1]

    df1 = df.groupby('coursecontentscore').count()[['coursecontent']]
    coursecontent_negative_count = df1['coursecontent'][-1]
    coursecontent_neutral_count = df1['coursecontent'][0]
    coursecontent_positive_count = df1['coursecontent'][1]

    df1 = df.groupby('examinationscore').count()[['examination']]
    examination_negative_count = df1['examination'][-1]
    examination_neutral_count = df1['examination'][0]
    examination_positive_count = df1['examination'][1]

    df1 = df.groupby('labworkscore').count()[['labwork']]
    labwork_negative_count = df1['labwork'][-1]
    labwork_neutral_count = df1['labwork'][0]
    labwork_positive_count = df1['labwork'][1]

    df1 = df.groupby('libraryfacilitiesscore').count()[['libraryfacilities']]
    libraryfacilities_negative_count = df1['libraryfacilities'][-1]
    libraryfacilities_neutral_count = df1['libraryfacilities'][0]
    libraryfacilities_positive_count = df1['libraryfacilities'][1]

    df1 = df.groupby('extracurricularscore').count()[['extracurricular']]
    extracurricular_negative_count = df1['extracurricular'][-1]
    extracurricular_neutral_count = df1['extracurricular'][0]
    extracurricular_positive_count = df1['extracurricular'][1]

    total_positive_feedbacks = teaching_positive_count + coursecontent_positive_count + examination_positive_count + labwork_positive_count + libraryfacilities_positive_count + extracurricular_positive_count
    total_neutral_feedbacks = teaching_neutral_count + coursecontent_neutral_count + examination_neutral_count + labwork_neutral_count + libraryfacilities_neutral_count + extracurricular_neutral_count
    total_negative_feedbacks = teaching_negative_count + coursecontent_negative_count + examination_negative_count +labwork_negative_count + libraryfacilities_negative_count + extracurricular_negative_count

    li = [teaching_positive_count,teaching_negative_count,teaching_neutral_count,
          coursecontent_positive_count,coursecontent_negative_count,coursecontent_neutral_count,
          examination_positive_count,examination_negative_count,examination_neutral_count,
          labwork_positive_count,labwork_negative_count,labwork_neutral_count,
          libraryfacilities_positive_count,libraryfacilities_negative_count,libraryfacilities_neutral_count,
          extracurricular_positive_count,extracurricular_negative_count,extracurricular_neutral_count]

    return no_of_students,\
           int(round(total_positive_feedbacks / total_feedbacks * 100)),\
           int(round(total_negative_feedbacks / total_feedbacks * 100)),\
           int(round(total_neutral_feedbacks / total_feedbacks * 100)),\
            li

def get_tables():
    df= pd.read_csv('dataset/database.csv')
    df = df.tail(5)
    return [df.to_html(classes='data')]

def get_titles():
    df = pd.read_csv('dataset/database.csv')
    return df.columns.values

