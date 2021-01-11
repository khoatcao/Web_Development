'''
import xml.dom.minidom as xml

def main() : 
    doc = xml.parse("file.xml")
    print(doc.nodeName)
    #print(doc.firstChild.tagName)
    expertise = doc.getElementsByTagName("expertise")
    print("length",len(expertise))
    for skill in expertise : 
        print(skill.getAttribute("name"))

if __name__=="__main__" : #z telling the program that there is a program to excute
    main()
'''
import xml.etree.ElementTree as ET
tree = ET.parse("file.xml")
pprint(tree.)