from place import Place

class Bar(Place):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.name_ = "Bar"
        self.description_ = "You are in the bar"
        if self.dev_log_: print("INFO: New bar created")

        
class Temple(Place):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.name = "Temple"
        self.description_ = "You are in the temple"
        if self.dev_log_: print("INFO: New temple created")
        
class Townhall(Place):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.name= "Townhall"
        self.description_ = "You are in the townhall"
        if self.dev_log_: print("INFO: New temple created")
    
    
    