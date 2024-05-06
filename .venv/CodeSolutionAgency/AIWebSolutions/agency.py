from agency_swarm import Agency
from TaskExecutionAgent import TaskExecutionAgent
from InteractionAgent import InteractionAgent
from AIWebSolutionsCEO import AIWebSolutionsCEO


agency = Agency([aiwebsolutions_ceo, interaction_agent, task_execution_agent, [aiwebsolutions_ceo, interaction_agent],
 [aiwebsolutions_ceo, task_execution_agent],
 [interaction_agent, task_execution_agent]],
                shared_instructions='./agency_manifesto.md', # shared instructions for all agents
                max_prompt_tokens=25000, # default tokens in conversation for all agents
                temperature=0.3, # default temperature for all agents
                )
                
if __name__ == '__main__':
    agency.demo_gradio()
