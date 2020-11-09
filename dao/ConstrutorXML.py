class xmlBuilder:
    def __init__(self, dictionaryTypes, name):
      self.dictionaryTypes = dictionaryTypes  
      self.space = '    '   
      self.name = name
      
    def build(self):
        packageXml = open(self.name +'.xml', 'w')
        packageXml.write('<?xml version="1.0" encoding="UTF-8"?>\n' +
                            '<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n')
        for list in self.dictionaryTypes:
            if self.dictionaryTypes[list]:
                packageXml.write(self.space + '<types>\n')
                for item in self.dictionaryTypes[list]:
                    packageXml.write(self.space +self.space + '<members>'+str(item)+'</members>' + '\n')
                packageXml.write(self.space +self.space +  '<name>' + list + '</name>' + '\n')
                packageXml.write(self.space + '</types>\n')
        packageXml.write(self.space + '<version>48.0</version>\n')
        packageXml.write('</Package>')

   

    
    