import os
import re


def find_file_by_extension(extension, path):
    global count, lines_count
    size = 0
    output = ''
    file_list = []
    for root, dirs, files in os.walk(path):
        if any((x in re.split(r'[\\\/]+', root) for x in dirs_excluded)):
            continue
        for searched_file in files:
            if searched_file.split('.')[-1] == extension:
                file_list.append(os.path.join(root, searched_file))
    for each in file_list:
        output += str(each) + '\n'
        size += int(os.path.getsize(each))
        count += 1

        with open(each, 'rb') as f:
            for _ in f: lines_count += 1

    output += f'Files found: {count}\n'
    output += f'Total Size: {str(size // (1024*1024))} MB\n'
    output += f'Total lines count: {lines_count}'
    return output


file_extension = input('What file extension do you search for (exe, mp3,  txt...)?: ')
system_path = input('Enter/the/path/in/system: ')
dirs_excluded = input('Enter directories to exclude, separated with comma (example: Dir1, Dir2, ...): ').split(', ')
count = 0
lines_count = 0

result = find_file_by_extension(file_extension, system_path)
print(result)

