class Dayana:
    message_general = "Voy a gastar"
    def __init__(self, _name):
        self.name = _name
        

    def gastar(self,):
        print(self.message_general)

    def gastar(self,_metodo=''):
        print(self.message_general)
        if _metodo != '':
            print(_metodo)
        
