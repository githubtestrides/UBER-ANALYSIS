import pandas as pd
def clean(df):
    new_df=df[:-1]
    new_df['START_DATE*'] = pd.to_datetime(new_df['START_DATE*'])
    new_df['END_DATE*'] = pd.to_datetime(new_df['END_DATE*'])
    new_df['month'] = new_df['START_DATE*'].dt.month
    return new_df

def month(df):
    new_df = df[:-1]
    new_df['START_DATE*'] = pd.to_datetime(new_df['START_DATE*'])
    new_df['END_DATE*'] = pd.to_datetime(new_df['END_DATE*'])
    new_df['month'] = new_df['START_DATE*'].dt.month




    trip=new_df['month'].value_counts().reset_index()
    trip.rename(columns={'index': 'month', 'month': 'trip'},inplace=True)

    return trip

def time(df):
    new_df = df[:-1]
    new_df['START_DATE*'] = pd.to_datetime(new_df['START_DATE*'])
    new_df['END_DATE*'] = pd.to_datetime(new_df['END_DATE*'])
    new_df['month'] = new_df['START_DATE*'].dt.month

    x = new_df['START_DATE*'].dt.hour.value_counts().reset_index()
    x.rename(columns={'index': 'Hours', 'START_DATE*': 'trip'}, inplace=True)

    return x

def purpose(df):
    new_df = df[:-1]
    y = new_df['PURPOSE*'].value_counts().reset_index()
    y.rename(columns={'index': 'purpose', "PURPOSE*": 'counts'}, inplace=True)
    return y




