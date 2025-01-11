import os
import shutil
import random

images_folder = 'Dataset/images'  
annotations_folder = 'Dataset/yolo_annotations'
organized_images_folder = 'splitted_data/images'
organized_labels_folder = 'splitted_data/labels' 
train_val_split_ratio = 0.8

def create_dirs():
    for folder in [organized_images_folder, organized_labels_folder]:
        for subfolder in ['train', 'val']:
            os.makedirs(os.path.join(folder, subfolder), exist_ok=True)

def organize_data():
    for root, _, files in os.walk(images_folder):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                rel_path = os.path.relpath(root, images_folder)
                print(f"Processing image: {file} at {root}")
                
                split_folder = 'train' if random.random() < train_val_split_ratio else 'val'

                image_dest_folder = os.path.join(organized_images_folder, split_folder, rel_path)
                os.makedirs(image_dest_folder, exist_ok=True)
                shutil.copy2(os.path.join(root, file), image_dest_folder)
                print(f"Copied image to: {image_dest_folder}")

                annotation_file = os.path.splitext(file)[0] + '.txt'
                annotation_src = os.path.join(annotations_folder, rel_path, annotation_file)
                if os.path.exists(annotation_src):
                    annot_dest_folder = os.path.join(organized_labels_folder, split_folder, rel_path)
                    os.makedirs(annot_dest_folder, exist_ok=True)
                    shutil.copy2(annotation_src, annot_dest_folder)
                    print(f"Copied annotation to: {annot_dest_folder}")
                else:
                    print(f"Warning: Annotation for {file} not found.")

if __name__ == "__main__":
    create_dirs()  
    print("Organizing images and labels...")
    organize_data() 
    print("Dataset reorganization completed!")
