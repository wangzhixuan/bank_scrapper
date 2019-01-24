
from .base_bank import BaseBank

class WellsFargo(BaseBank):
    def __init__(self, username, password):
        BaseBank.__init__(self, username=username, password=password, url='www.wellsfargo.com')

    def get_transactions(self):
        raise NotImplementedError