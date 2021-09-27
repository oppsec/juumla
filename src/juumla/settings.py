from random import randint


def get_user_agent() -> str:
    " Return a random User-Agent from user-agents.txt file to use on requests "

    file_path: str = "src/juumla/user-agents.txt"
    
    with open(file_path) as content:
        user_agent: str = content.readlines()
        user_agent: str = user_agent[randint(0, len(user_agent) -1)]
        user_agent: str = user_agent.encode('utf-8')

        return str(user_agent)


headers = {
    'User-Agent': get_user_agent(),
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


props = {
    'verify': False,
    'allow_redirects': True,
    'headers': headers
}