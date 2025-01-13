from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
from dotenv import load_dotenv
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
import gradio as gr

load_dotenv()

agent = Agent(
    name="buddy",
    model = Groq(id = "llama-3.3-70b-versatile"),
    #model=OpenAIChat(id="gpt-4o"),
    tools = [YouTubeTools()],
    show_tool_calls= True,
    instructions=[
        "you are a youtube agent. check the video ans givce me the timestamp.",
        "don't create false timestamps.",
        "show me the timestamps in the format[start,end,summary]"
    ],
)

x = agent.run(
    "get me the timestamp of this video https://youtu.be/M22NWSGKlOg" , markdown=True
)
#print(x.content)

def callMe(text):
    x = agent.run(
    "get me the timestamp of this video" + text +
    "format the output in a tabular format. Also provide a summary at end."
      
    )
    return x.content


demo = gr.Interface(fn=callMe, inputs="text", outputs="text")
demo.launch()
