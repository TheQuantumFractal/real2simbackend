import pandas as pd
import json

def csv_to_json(csv_file, json1_file, json2_file, json3_file):
    df = pd.read_csv(csv_file)
    # Create a new DataFrame with the first three columns removed
    new_df = df.drop(columns=[df.columns[0], df.columns[2]])
    new_df = new_df.dropna()
    question_list = new_df.columns.tolist()
    prompt_dict = {}
    first_dates = {}
    emoji_dict = {}
    for row in new_df.itertuples(index=False):
        i = 0
        for question in row:
            if i == 0:
                prompt_dict[question] = "" 
                first_dates[question] = row[15]
                emoji_dict[question] = row[16]
                i += 1
            elif question != 'NaN':
                prompt_dict[row[0]] += question_list[i] + row[i] 
                i += 1
    with open(json1_file, 'w') as file:
        json.dump(prompt_dict, file)
    with open(json2_file, 'w') as file:
        json.dump(first_dates, file)
    with open(json3_file, 'w') as file:
        json.dump(emoji_dict, file)

if __name__ == "__main__":
    responses = '/phase1/data/responses.csv'
    user_profiles = '/phase1/data/characters.json'
    first_dates = '/phase1/data/first_dates.json'
    emoji_dict = '/phase1/data/profiles.json'
    csv_to_json(responses, user_profiles, first_dates, emoji_dict)
