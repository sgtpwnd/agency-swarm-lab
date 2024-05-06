from agency_swarm.agents import Agent


class TaskExecutionAgent(Agent):
    def __init__(self):
        super().__init__(
            name="TaskExecutionAgent",
            description="This agent is responsible for web browser interactions, including form submissions, clicks, and navigation, using web automation tools like Selenium or Puppeteer. It should efficiently perform tasks that facilitate the user's interaction with web content and achieve specific goals set by the user.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
