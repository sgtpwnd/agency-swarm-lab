from agency_swarm.agents import Agent


class AIWebSolutionsCEO(Agent):
    def __init__(self):
        super().__init__(
            name="AIWebSolutionsCEO",
            description="This agent oversees the overall project and serves as the primary point of communication with the user, managing and coordinating the activities of other agents while ensuring the project adheres to its mission and core functionalities.",
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
