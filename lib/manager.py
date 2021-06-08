from random import randint

def get_user_agent() -> str:
    with open('lib/user-agents.txt') as agents_file:
        user_agents = agents_file.readlines()
        user_agent = user_agents[randint(0, len(user_agents) -1)]
        user_agent = user_agent.encode('utf-8')

        return str(user_agent)


# Get a random user-agent
headers = {'User-Agent': get_user_agent()}

# Props to requests
props = {
    'verify': False,
    'timeout': 10,
    'allow_redirects': False,
    'headers': headers
}