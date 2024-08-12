import logging
import pandas as pd


def load_data(path):
    try:
        df = pd.read_csv(path)
        logging.info('Data imported successfully')
        return df
    except BaseException:
        logging.info('Reading data failed')


def cleaned_data(df):
    try:
        df.columns = df.columns.str.strip()
        df.drop(["fnlgt", "education-num", "capital-gain", "capital-loss"],
                 axis=1, inplace=True)
        
        for col in df.drop(['age', 'hours-per-week'], axis=1).columns:
            for i in range(len(df)):
                df[col][i] = df[col][i][1:]
        
        logging.info('Data cleaned successfully')
        df.to_csv('clean_census.csv')
        return df
    
    except BaseException:
        logging.info('Data is not cleaned properly')



df = load_data('census.csv')
cleaned_data(df)