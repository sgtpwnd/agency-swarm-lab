from agency_swarm.agents import Agent


class WebAutomationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="WebAutomationAgent",
            description="A Web Automation Agent capable of controlling web browsers using automation tools and managing backend operations.",
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
