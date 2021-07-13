from random import randint


def get_user_agent() -> str:
    """ Returns a user-agent from user-agents.txt file """

    filename: str = "src/juumla/user-agents.txt"
    with open(filename) as file:
        user_agents: str = file.readlines()
        user_agents: str = user_agents[randint(0, len(user_agents) -1)]
        user_agents = user_agents.encode('utf-8')

        return str(user_agents)


headers = {
    'User-Agent': get_user_agent()
}


props = {
    'verify': False,
    'timeout': 20,
    'allow_redirects': True,
    'headers': headers
}