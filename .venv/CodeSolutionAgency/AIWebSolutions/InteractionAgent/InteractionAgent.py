from agency_swarm.agents import Agent


class InteractionAgent(Agent):
    def __init__(self):
        super().__init__(
            name="InteractionAgent",
            description="This agent specializes in user interactions and handles voice or text inputs through advanced NLP technologies. It manages user feedback and utilizes NLP libraries like NLTK or spaCy to interpret and act on user inputs, ensuring effective communication and interaction with users.",
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
