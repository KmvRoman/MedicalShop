from src.presentation.web.api.v1.endpoints.statistic import read_stats
from src.presentation.web.api.v1.endpoints.user import user

routers = [read_stats.router, user.router]
