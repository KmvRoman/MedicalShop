from src.application.common.interfaces import CreateOrder, Committer, AddPriceToOrderProduct


class DbGateway(CreateOrder, Committer, AddPriceToOrderProduct):
    pass
