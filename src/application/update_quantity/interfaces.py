from src.application.common.interfaces import UpdateQuantity, Committer


class DbGateway(UpdateQuantity, Committer):
    pass
