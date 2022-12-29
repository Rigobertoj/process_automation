import xml.etree.cElementTree as ET

tree = ET.parse("data.xml")

root = tree.getroot()

country_1 = root[0]


for value in country_1:
    print(value.tag, value.attrib)