from random import randint

import json

def get_user_agent():
    with open('lib/user-agents.txt') as agents_file:
        user_agents = agents_file.readlines()
        user_agent = user_agents[randint(0, len(user_agents) -1)]
        user_agent = user_agent.encode('utf-8')

        return str(user_agent)