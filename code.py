class Process:
    def __init__(self):
        self.code=[]
        self.func={}
    def set_action(self,ope,func):
        self.func[ope]=func

class CodeLine:
    def __init__(self,ope,args):
        self.ope=ope
        self.args=args
