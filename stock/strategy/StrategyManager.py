from .BuyRA_5 import BuyRA_5
from .BuyGC_5 import BuyGC_5
from .SellDC_5 import SellDC_5
from .SellMAX_10 import SellMAX_10
from .BuySupportLevel_3M import BuySupportLevel_3M
from .BuyMomentum import BuyMomentum
from .SellMomentum import SellMomentum


class StrategyManager:

    def __init__(self):
        self.buy_map = {
            'MOMENTUM': BuyMomentum(),
            'RA_5': BuyRA_5(),
            'GC_5': BuyGC_5(),
            'SUPPORT_LEVEL_3M': BuySupportLevel_3M(),
        }
        self.sell_map = {
            'MOMENTUM': SellMomentum(),
            'MAX_10': SellMAX_10(),
            'DC_5': SellDC_5(),
        }

    def get_strategy(self, buy_code, sell_code):
        buy_func = self.buy_map.get(buy_code, BuyRA_5())
        sell_func = self.sell_map.get(sell_code, SellMAX_10())

        return buy_func, sell_func


