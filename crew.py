# pyright: reportMissingImports=false
from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task 

# Forming the Tech-Focused Crew with some enhanced configuration.
crew= Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential, # Optional : Sequential Task Execution
    memory=True, # Optional : Enable Memory for Agents
    cache=True, # Optional : Enable Caching for Tools
    max_rpm=100,
    share_crew=True
)

# Start the Task Execution process with Enhanced Feedback
result=crew.kickoff(inputs={'topic': 'AI vs ML vs DL vs Data Science'})
print("Final Result:", result)