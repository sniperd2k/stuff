import os
import re
import shutil

#some examples of how you can sort a mess of files into folders based up on the names of the files

def main():
    target_path = "X:\\pictures\\"
    source_path_list = ["X:\\photosync\\"]
    for source_path in source_path_list:
        file_list = get_file_list(source_path)
        file_dict = get_file_dict(file_list)
        move_files(source_path, target_path, file_dict)

def move_files(source_path, target_path, file_dict):
    for target_folder, file_list in file_dict.items():
        if not os.path.exists("".join([target_path, target_folder])):
            os.makedirs("".join([target_path, target_folder]))
        for the_file in file_list:
            print("".join(["moving:",source_path, the_file, " to:", target_path, target_folder, "\\", the_file]))
            shutil.move("".join([source_path, the_file]), "".join([target_path, target_folder, "\\", the_file]))
    
def get_file_dict(file_list):
    file_dict = {}
    for the_file in file_list:
        
        date_match_1 = re.search(r"^(\d{8})_", the_file)
        if date_match_1:
            key_1 = date_match_1.group(1)
            key_1 = re.sub("(\d{4})(\d{2})(\d{2}).*", "\\1-\\2-\\3", key_1)
            file_dict = update_file_dict(file_dict, key_1, the_file)
        
        date_match_2 = re.search("^IMG_(\d{8})", the_file, flags=re.IGNORECASE)
        if date_match_2:
            key_2 = date_match_2.group(1)
            key_2 = re.sub("^(\d{4})(\d{2})(\d{2}).*", "\\1-\\2-\\3", key_2)
            file_dict = update_file_dict(file_dict, key_2, the_file)
            
    return file_dict        
    
def get_file_list(source_path):
    file_list = os.listdir(source_path)
    return file_list

def update_file_dict(file_dict, key, the_file):
    if key not in file_dict:
        file_dict[key] = []
    file_dict[key].append(the_file)
    return file_dict

if __name__ == "__main__":
    main()
