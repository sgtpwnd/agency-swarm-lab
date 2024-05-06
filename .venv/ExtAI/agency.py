from agency_swarm import Agency
from BrowsingAgent import BrowsingAgent
from Devid import Devid
from ExtAICEO import ExtAICEO

# Initialize agents
ext_aiceo = ExtAICEO()
devid = Devid()
browsing_agent = BrowsingAgent()

# Setup Agency with appropriate configurations
agency = Agency([ext_aiceo, devid, browsing_agent, [ext_aiceo, devid],
                 [ext_aiceo, browsing_agent],
                 [devid, browsing_agent]],
                shared_instructions='./agency_manifesto.md',
                max_prompt_tokens=25000,
                temperature=0.3)

# Main execution block
if __name__ == '__main__':
    try:
        # Launching the Gradio interface with the correct 'share' parameter
        agency.demo_gradio(server_name="0.0.0.0", share=True)
    except Exception as e:
        # Error handling to catch and log any issues during the execution
        print(f"An error occurred: {e}")
