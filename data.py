#!/usr/bin/env python
# coding: utf-8

# In[5]:


def convert_data_types(df):
    # Convert columns to the desired data types
    df["number_of_open_complaints"] = df["number_of_open_complaints"].astype(str)
    df["gender"] = df["gender"].astype(bool)
    df["vehicle_class"] = df["vehicle_class"].astype(str)
    df["policy_type"] = df["policy_type"].astype(str)

    return df


def lower_snake(df):
    lower_and_snake = lambda x: x.lower().replace(" ", "_")
    df.columns = list(map(lower_and_snake, list(df.columns)))
    return df




def standardize_gender(df):
    
    df['gender'] = df['gender'].replace("F", "female")
    df['gender'] = df['gender'].replace("M", "male")

    return df

def clean_and_format_data(df):
   
    df['customer_lifetime_value'] = df['customer_lifetime_value'] / 100.0

    return df