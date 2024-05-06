from agency_swarm.agents import Agent


class ExtAICEO(Agent):
    def __init__(self):
        super().__init__(
            name="ExtAICEO",
            description="This agent will manage the ExtAI agency, ensure communication between agents, and oversee that the agency's goals are met. It is responsible for facilitating and monitoring the communication flow between Devid and BrowsingAgent.",
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
