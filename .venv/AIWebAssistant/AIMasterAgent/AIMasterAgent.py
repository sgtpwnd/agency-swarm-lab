from agency_swarm.agents import Agent


class AIMasterAgent(Agent):
    def __init__(self):
        super().__init__(
            name="AIMasterAgent",
            description="An AI master agent with capabilities in NLP, machine learning, UI development, and secure authentication.",
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
