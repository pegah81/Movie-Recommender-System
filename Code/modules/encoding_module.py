import pandas as pd
import ast


# Making json values to dataframe
def json_to_DF(dataset, feature):
    dataset[feature] = dataset[feature].apply(ast.literal_eval)
    names_df = pd.DataFrame(dataset[feature].apply(lambda x: [item['name'] for item in x]))
    names_df = pd.DataFrame(names_df[feature].explode())
    name_counts = names_df[feature].value_counts()
    df_count = pd.DataFrame({'name': name_counts.index, 'frequency': name_counts.values})
    df_count.reset_index(drop=True, inplace=True)
    df_count.columns = ['name', 'frequency']
    return df_count


def onehot_json(dataset, feature, name):
    name_ids = []
    for index, row in dataset.iterrows():
        name_list = ast.literal_eval(row[feature])
        ids = [genre[name] for genre in name_list]
        name_ids.append(ids)

    # IDs as a new feature
    feature_name = name + '_col'
    dataset[feature_name] = name_ids
    df_encoded = pd.get_dummies(dataset[feature_name].apply(pd.Series).stack()).sum(level=0)
    # Concatenate the encoded genres with the original dataframe
    dataset = pd.concat([dataset, df_encoded], axis=1)
    return dataset
