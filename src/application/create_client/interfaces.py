from src.application.common.interfaces import CreateClient, Committer


class DbGateway(CreateClient, Committer):
    pass
