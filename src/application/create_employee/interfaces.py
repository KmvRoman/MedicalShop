from src.application.common.interfaces import CreateEmployee, Committer


class DbGateway(CreateEmployee, Committer):
    pass
