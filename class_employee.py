class Employee:
    def __init__(self):
        return
    class Parttime:
        def __init__(self,Employee,parttime):
            self.parttime=parttime
        def find(self,parttime):
            try:
                if self.parttime:
                    print("The employee is  part time worker") 
            except:
                raise KeyError
    class Fulltime:
        def __init(self,Employee,fulltime):
            self.fulltime=fulltime
        def find(self,fulltime):
            try:
                if self.fulltime:
                    print("The employee is working full time") 
            except:
                raise KeyError
                               