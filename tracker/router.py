from rest_framework.routers import DefaultRouter
from .viewsets import PoliticianViewSet, StockViewSet, TradeViewSet

router = DefaultRouter()
router.register(r"politicians", PoliticianViewSet, basename="politician")
router.register(r"stocks", StockViewSet, basename="stock")
router.register(r"trades", TradeViewSet, basename="trade")
