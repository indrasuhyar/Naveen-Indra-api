import pandas as pd
from functions import get_distinct_count, get_distinct_percentage

def test_employees_csv_stats():
    df = pd.read_csv('employees.csv')
    
    # Assert Job ID is 51% distinct
    distinct_pct = get_distinct_percentage(df)
    assert round(distinct_pct['Job ID']) == 51
    
    # Assert # Of Positions has 25 distinct (number)
    distinct_counts = get_distinct_count(df)
    assert distinct_counts['# Of Positions'] == 25
    
    # Assert Agency has 54 distinct (number)
    assert distinct_counts['Agency'] == 54
