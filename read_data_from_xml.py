
import xml.etree.ElementTree as ET

with open('json_to_xml.xml','r') as f:
    mytree = ET.parse(f)
    myroot = mytree.getroot()

    print(myroot[5].text)
