# pyright: reportMissingImports=false
from crewai import Task 
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research Task 
research_task = Task(
    description = (
        "Identify the Video {topic}."
        "Get detailed information about the video from the Channel"
    ),
    expected_output="A comprehensive 3 paragraphs long report based on the {topic} of the video from the channel.",
    tools=[yt_tool],
    agent=blog_researcher

)

# Writing task with language model configuration
write_task = Task(
    description=(
        "Write a comprehensive blog post on the topic {topic} using the research report provided by the Blog Researcher."
    ),
    expected_output="A well-structured and engaging blog post that effectively communicates the key insights and information from the research report.",
    tools=[yt_tool],
    async_execution=False,
    agent=blog_writer,
    output_file='new-blog-post.md' # Example of output custamization
)