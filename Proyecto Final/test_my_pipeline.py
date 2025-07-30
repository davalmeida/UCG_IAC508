# %%writefile test_my_pipeline.py
import pytest
import pandas as pd
from pipeline import DataPipeline

def test_most_valued_house():
    # Sample data similar to Housing.csv
    data = {
        'price': [100000, 250000, 175000],
        'area': [1200, 2000, 1500],
        'bedrooms': [2, 3, 2],
        'bathrooms': [1, 2, 1],
        'stories': [1, 2, 1],
        'mainroad': ['yes', 'no', 'yes'],
        'guestroom': ['no', 'yes', 'no'],
        'basement': ['no', 'no', 'yes'],
        'hotwaterheating': ['no', 'no', 'no'],
        'airconditioning': ['yes', 'no', 'yes'],
        'parking': [1, 2, 0],
        'prefarea': ['yes', 'no', 'yes'],
        'furnishingstatus': ['furnished', 'unfurnished', 'semi-furnished']
    }
    df = pd.DataFrame(data)
    pipeline = DataPipeline()
    # Preprocess to get area_miles
    X, y = pipeline.preprocess(df)
    # Find the index of the most valued house
    idx_max = y.idxmax()
    # Get area_miles for that house
    area_miles = X.loc[idx_max, 'area_miles']
    # Assert the price and area_miles are as expected
    assert y[idx_max] == 250000
    assert area_miles == 2.0

def test_most_valued_house_real_data():
    # Use the first 40 rows from the real Housing.csv
    df = pd.read_csv('Housing.csv').head(40)
    pipeline = DataPipeline()
    X, y = pipeline.preprocess(df)
    idx_max = y.idxmax()
    area_miles = X.loc[idx_max, 'area_miles']
    # The max price and area for the first 40 rows (from the csv sample)
    # Row 0: price=13300000, area=7420 -> area_miles=7.42
    # Row 1: price=12250000, area=8960 -> area_miles=8.96
    # Row 7: price=16200, area=10150000 -> area_miles=10.15 (but price is not max)
    # The max price is 13300000, area 7420, area_miles 7.42
    assert y[idx_max] == 13300000
    assert abs(area_miles - 7.42) < 1e-2 