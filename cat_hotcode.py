import pandas as pd
def one_hot_encoding_and_bind(dataframe, feature_to_encode):
    dummies = pd.get_dummies(dataframe[[feature_to_encode]])
    res = pd.concat([dataframe, dummies], axis=1)
    return(res)