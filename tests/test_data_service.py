import pandas as pd
from app.services.data_service import summarize

def test_numeric_summary():
    result = summarize(pd.DataFrame({'sales': [10, 20, 30]}))
    assert result['numeric_summary']['sales']['sum'] == 60
    assert result['profile']['rows'] == 3
