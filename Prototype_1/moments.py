from choice import Choice
from moment import Moment

class Bar_daytime(Moment):
    def __init__(self, place, dev_log=False):
        super().__init__(place, dev_log)
        self.description_ = "It is still pretty early, so there is not many people here."
        
class Bar_night(Moment):
    def __init__(self, place, dev_log=False):
        super().__init__(place, dev_log)
        self.description_ = "The bar is crowded with drunkards, as it always is at night."
        
class Temple_regular(Moment):
    def __init__(self, place, dev_log=False):
        super().__init__(place, dev_log)
        self.description_ = "A few people are praying, and priests are minding their own business."
        
class Temple_priestConv(Moment):
    def __init__(self, place, dev_log=False):
        super().__init__(place, dev_log)
        self.description_ = "The priest looks at you and says: \"What can I do for you?\"."
        
class Temple_office(Moment):
    def __init__(self, place, dev_log=False):
        super().__init__(place, dev_log)
        self.description_ = "A huge crow is praying while the high priest performs the office."
        
class Townhall_daytime(Moment):
    def __init__(self, place, dev_log=False):
        super().__init__(place, dev_log)
        self.description_ = "A few people are queueing, waiting to be received by the officials."
        