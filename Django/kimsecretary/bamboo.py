class Bamboo:
    fw = open ('bamboo.txt', 'w')
    fr = open ('bamboo.txt', 'r')
    
    def __init__(self):
        pass
    
    def file_write(self,input,bamboo_num):
        
        self.fw.write(bamboo_num)
        self.fw.write("/#/")
        self.fw.write(input)
        
    def file_read_rand(self):
        return self.fr.readline()
        
    def file_read_num(self,num):
        return "숫자리드"
        
    def file_read_key(self,key):
        return "키워드리드"
        
        
        
        