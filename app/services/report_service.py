from app.services.data_service import summarize

def build_report(df):
    return summarize(df)
