import pandas as pd

def profile(df: pd.DataFrame):
    return {
        'rows': int(len(df)),
        'columns': list(map(str, df.columns)),
        'missing_values': {str(k): int(v) for k, v in df.isna().sum().items()},
        'duplicate_rows': int(df.duplicated().sum()),
        'numeric_columns': list(map(str, df.select_dtypes(include='number').columns)),
        'preview': df.head(8).fillna('').astype(str).to_dict(orient='records'),
    }

def summarize(df: pd.DataFrame):
    numeric = df.select_dtypes(include='number')
    stats = {}
    for col in numeric.columns:
        series = numeric[col].dropna()
        if not series.empty:
            stats[str(col)] = {
                'sum': round(float(series.sum()), 3),
                'average': round(float(series.mean()), 3),
                'minimum': round(float(series.min()), 3),
                'maximum': round(float(series.max()), 3),
            }
    return {'profile': profile(df), 'numeric_summary': stats}
