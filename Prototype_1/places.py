from place import place

class bar(place):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.description_ = "You are in a bar"
        if self.dev_log_: print("INFO: New bar created")

        
class temple(place):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.description_ = "You are in the temple"
        if self.dev_log_: print("INFO: New temple created")
        
class townhall(place):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.description_ = "You are in the townhall"
        if self.dev_log_: print("INFO: New temple created")
    
    
    