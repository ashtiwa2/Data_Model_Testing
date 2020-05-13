
import json
import xml.etree.ElementTree as ET

with open('data.json','r') as file:
    d= json.load(file)

e = ET.Element("Employee")
ET.SubElement(e,"Name").text = d["Name"]
ET.SubElement(e, "Age").text = str(d["Age"])
ET.SubElement(e, "Height").text = str(d["Height"])
ET.SubElement(e, "Education").text = d["Education"]
ET.SubElement(e, "Occupation").text = d["Occupation"]
Hob = ET.SubElement(e, "Hobbies")
ET.SubElement(Hob,'Hobbies').text = d["Hobbies"][0]
ET.SubElement(Hob,'Hobbies').text = d["Hobbies"][1]
ET.SubElement(Hob,'Hobbies').text = d["Hobbies"][2]
ET.SubElement(Hob,'Hobbies').text = d["Hobbies"][3]
ET.SubElement(e, "EMP ID").text = str(d["EMP ID"])

tree = ET.ElementTree(e)
tree.write("json_to_xml.xml")





