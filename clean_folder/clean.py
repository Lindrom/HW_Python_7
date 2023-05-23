import os
import sys
import shutil
import re

def normalize(filename):
    transliteration_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '',
        'ы': 'y', 'ъ': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    # Транслитерация кириллицы
    normalized = ''.join(transliteration_map.get(c.lower(), c) for c in filename)

    # Смена недопустимых символов на "_"
    normalized = re.sub(r'[^a-zA-Z0-9]+', '_', normalized)

    return normalized

def process_folder(folder_path):
    contents = os.listdir(folder_path)
    
    for item in contents:
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            filename, extension = os.path.splitext(item)
            new_filename = normalize(filename) + extension

            if extension.lower() in ['.jpeg', '.png', '.jpg', '.svg']:
                destination_folder = os.path.join(folder_path, 'images')

            elif extension.lower() in ['.avi', '.mp4', '.mov', '.mkv']:
                destination_folder = os.path.join(folder_path, 'video')

            elif extension.lower() in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                destination_folder = os.path.join(folder_path, 'documents')

            elif extension.lower() in ['.mp3', '.ogg', '.wav', '.amr']:
                destination_folder = os.path.join(folder_path, 'audio')

            elif extension.lower() in ['.zip', '.gz', '.tar']:
                destination_folder = os.path.join(folder_path, 'archives', filename)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.unpack_archive(item_path, destination_folder)
                continue

            else:
                # Если расширение не указано - то оставляем без изменений
                continue

            # Перенос в нужную папку
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(destination_folder, new_filename))
            

if name == 'main':
    process_folder()