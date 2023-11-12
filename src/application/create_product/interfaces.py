from src.application.common.interfaces import CreateProduct, Committer


class DbGateway(CreateProduct, Committer):
    pass
