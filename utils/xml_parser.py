import xml.etree.ElementTree as Et
i = 0
path = "../data/label{0}.xml".format(i)

tree = Et.parse(path)
root = tree.getroot()
tup_list = []
for child in root.iter('object'):
    key = child.find('name').text
    for coord in child.iter('bndbox'):
        xmin = coord.find('xmin').text
        ymin = coord.find('ymin').text
        xmax = coord.find('xmax').text
        ymax = coord.find('ymax').text
        coords = [xmin, ymin, xmax, ymax]
        tup_list.append((key, coords))

for e in tup_list:
    print(e)
