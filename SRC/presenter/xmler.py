import xml.etree.ElementTree as ET
from model.globalsvar import HUB_TELEMETRY_TAG, HUB_SETINGS_TAG
import datetime


class xmler(object):
    
    
    def loadXML(self, xmlpath):
        self.path = xmlpath
        self.tree = ET.parse(xmlpath)
        self.root = self.tree.getroot()
                
    
    def testprintxml(self):
        print(self.root.text)
        for element in self.root: 
            print(element.tag, element.attrib)
            for one in element:
                print(one.tag, " = " , one.text, one.attrib)
        print("**" * 33)


    def reload_xml(self):
        self.tree = ET.parse( self.path)
        self.root = self.tree.getroot()
        

    def get_formatet_intag(self, tag):
        result = [1,2,3]  
        target = self.root.find(tag)
#         result.append(target.tag.join(" = ").join(target.text).join(target.attrib))
        result.append(target.attrib)
        for one in target:
#             print(one.tag, " = " , one.text, one.attrib)
            text_string = one.tag.join(" = ").join(one.text).join(one.attrib)
            print(one.tag)
            print(one.text)
            print(one.attrib)
#             print(text_string)
            result.append(text_string)
        print(result)
        return result 


    def make_string_telemetry(self, tag, text):
        result = [tag, ' = ']
        if tag== "MBTIME":
            print("fpund FORMAT MBTIME")
            print( int(text, 16).__str__())
            print( datetime.datetime.fromtimestamp(int(text, 16)))
            print( datetime.datetime.fromtimestamp((int(text,16) * 10)))
            print( int(text, 16).__str__())
            print( int(text, 16).__str__())
            #text = int(text, 16).__str__()
            text = datetime.datetime.fromtimestamp(int(text, 16)).__str__()
        result.append(text)
        return "".join(result)
    
    
    def formatedstringlist_from_telemetry(self):
        result = []
        target = self.root.find(HUB_TELEMETRY_TAG)
        i = 1
        for device in target:
            print("*"*33,i,"*"*33)
            result.append(device.tag)
            for parametr in device:
                print("Tag")
                print(parametr.tag)
                print("text")
                print(parametr.text)
                print("attrib")
                print(parametr.attrib)
                print("Join")
#                 text_line = [parametr.tag," = ",parametr.text]
#                 result.append("".join(text_line))
                result.append("".join(
                    self.make_string_telemetry(
                        parametr.tag, 
                        parametr.text))
                )
            i+=1
        return result 


    def make_string_from_tag(self, tag, text, attrib):
        result = [tag, ' = ']
        if attrib.get("FORMAT")== "STRING":
            print("fpund FORMAT STRING")
        if attrib.get("FORMAT")== "HEX" or attrib.get("FORMAT")=="MBUSHEX":
            text = int(text, 16).__str__()
        result.append(text)
        if attrib.get("UNIT"):
            result.append(" " + attrib.get("UNIT"))
        if attrib.get("FORMAT")=="MBUSHEX":
            result.append(" (MBUSHEX)")
        return "".join(result)
    
    
    def formatedstringlist_from_hubsetings(self):
        result = []
        target = self.root.find(HUB_SETINGS_TAG)
        i = 1
        for device in target:
            print("*"*33,i,"*"*33)
            result.append(self.make_string_from_tag(device.tag,device.text,device.attrib))
            print(result[result.__len__()-1])
            for parametr in device:
                text_line = [
                        "       |","_____",
                        self.make_string_from_tag(
                            parametr.tag,parametr.text,parametr.attrib
                        )
                ]
                result.append("".join(text_line))
            i+=1
        return result 
