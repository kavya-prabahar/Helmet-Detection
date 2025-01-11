import os
import xml.etree.ElementTree as ET

xml_folder = 'Dataset/annotations'
txt_folder = 'Dataset/yolo_annotations'

class_mapping = {'With Helmet':0, 'Without Helmet' : 1}

def convert_xml_to_yolo(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)

    output_txt = os.path.join(txt_folder, os.path.basename(xml_file).replace('xml','txt'))


    with open(output_txt, 'w') as f:
        for obj in root.findall('object'):
            class_name = obj.find('name').text
            if class_name not in class_mapping:
                continue
            class_id = class_mapping[class_name]

            xmin = int(obj.find('bndbox/xmin').text)
            xmax = int(obj.find('bndbox/xmax').text)
            ymin = int(obj.find('bndbox/ymin').text)
            ymax = int(obj.find('bndbox/ymax').text)

            x_center = (xmin + xmax) / 2 / width
            y_center = (ymin + ymax) / 2 / height
            bbox_width = (xmax - xmin) / width
            bbox_height = (ymax - ymin) / height

            f.write(f"{class_id} {x_center} {y_center} {bbox_width} {bbox_height}\n")

def process_annotations():
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('xml'):
            convert_xml_to_yolo(os.path.join(xml_folder,xml_file))

process_annotations()
    