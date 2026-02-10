# pyright: reportMissingImports=false
from crewai  import Agent
from tools import yt_tool

# Create a senior blog content researcher agent

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video content for the topic{topic} from Yt Channel',
    verboese=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in Ai Data Science , Machine Learning and GenAI. Skilled in extracting key insights and information from video content to create comprehensive research reports."
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# Creating a Senior Blog Writer Agent with Yt Tool

blog_writer = Agent(
    role='Blog Writer',
    goal='write a comprehensive blog post on the topic {topic} using the research report provided by the Blog Researcher.',
    verboese=True,
    memory=True,
    backstory=(
        "Experienced blog writer with a strong background in Ai Data Science, Machine Learning and GenAI. Skilled in crafting engaging and informative blog posts that effectively communicate complex topics to a wide audience."
    ),
    tools=[yt_tool],
    allow_delegation=False
)