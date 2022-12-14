import numpy as np
import pandas as pd


def check_info(data):
    print(data.name, 'dataset schema:')
    print('---------------------------------------------')
    print(data.info())


def shape(data):
    print(data.name, 'shape:', data.shape)


def size(data):
    print(data.name, 'size:', data.size)


def get_unique_values(data):
    cols = data.columns
    for i in cols:
        if data[i].dtype == 'O':
            print('Unique values in column ', i, 'are', data[i].unique())
            print('----------------------------------------------')


def check_missing_val(data):
    print('Sum of missing values in', data.name)
    print('------------------------------')
    print(data.isnull().sum())


def get_categorical_variables(data):
    categorical_data = data.select_dtypes(exclude='number')
    categorical_data.head()


def get_numercial_variables(data):
    categorical_data = data.select_dtypes(exclude='number')
    categorical_data.head()


def replace_outliers_with_nan(num_data, dataset_new):
    # treating outliers
    count = 1
    for col in num_data:
        Q1 = num_data[col].quantile(0.25)
        Q3 = num_data[col].quantile(0.75)
        IQR = Q3 - Q1
        print(f'column {count}: {num_data[col].name}\n------------------------')
        print('1st quantile => ', Q1)
        print('3rd quantile => ', Q3)
        print('IQR =>', IQR)

        fence_low = Q1 - (1.5 * IQR)
        print('fence_low => ' + str(fence_low))

        fence_high = Q3 + (1.5 * IQR)
        print('fence_high => ' + str(fence_high))
        print("\n------------------------")

        count = count + 1

        # replacing outliers with nan
        dataset_new[col][((dataset_new[col] < fence_low) | (dataset_new[col] > fence_high))] = np.nan


def get_column_with_nan_values(dataset_new):
    print(dataset_new.select_dtypes(include='number').isnull().sum())


def export_to_csv(data, name, index=False):
    data.to_csv(name, index=index)