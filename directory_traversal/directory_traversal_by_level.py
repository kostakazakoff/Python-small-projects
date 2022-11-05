import os


def extract_files_by_level(source, level_to_extract):
    for file_path in os.listdir(source):
        current_path = os.path.join(source, file_path)

        if os.path.isfile(current_path):
            extension = current_path.split('.')[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(file_path)
        
        elif os.path.isdir(current_path) and level_to_extract:
            extract_files_by_level(current_path, level_to_extract - 1)


directory = input('Enter the directory to traverse: ')
level = int(input('Enter the traversing level: '))
files = {}

extract_files_by_level(directory, level)

sorted_files = dict(sorted(files.items(), key=lambda x: x[0]))

with open('report.txt', 'w', encoding='UTF8') as f:
    for extension, names in sorted_files.items():
        f.write(f'{extension}\n')
        [f.write(f'- - - {name}\n') for name in sorted(names)]
