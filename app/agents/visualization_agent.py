import plotly.express as px

def build_chart(df, column):
    if column not in df.columns:
        raise ValueError('Unknown column')
    if not str(df[column].dtype).startswith(('int', 'float')):
        raise ValueError('Choose a numeric column')
    fig = px.histogram(df, x=column, title=f'Distribution of {column}')
    return fig.to_json()
