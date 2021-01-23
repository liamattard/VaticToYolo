import xml.etree.ElementTree as ET
import sys
import os.path
from os import path

def main(*argv):

    # Enter XML file name as command line arg1
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()

    for child in root:
        for obj in child.iter('object'):

            id = 0
            for x in child.iter('id'):
                id = x.text
            print("Writing object with id " + id)

            for polygon in obj.iter('polygon'):



                for t in polygon.iter('t'):
                    if not path.exists("output/"+t.text+".txt"):
                        file_obj  = open("output/"+t.text+".txt", 'w+')

                    file_obj  = open("output/"+t.text+".txt", 'a')

                    x = []
                    y = []

                    for xPos in polygon.iter('x'):
                        x.append(int(xPos.text)/sys.argv[2])

                    for yPos in polygon.iter('y'):
                        y.append(int(yPos.text)/sys.argv[3])

                    file_obj.write(str(id) + ' ' + str(x[0]) + ' ' + str(y[0]) + ' ' + str(x[1]) + ' ' + str(y[1]) + '\n')






if __name__ == "__main__":
    main()
