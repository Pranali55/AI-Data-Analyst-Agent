from app.agents.planner_agent import plan
from app.agents.analysis_agent import run as analyze
from app.agents.insight_agent import run as insight

async def run(df, question):
    steps = plan(question)
    results = analyze(df)
    explanation = await insight(question, results)
    return {'plan': steps, 'results': results, 'explanation': explanation}
