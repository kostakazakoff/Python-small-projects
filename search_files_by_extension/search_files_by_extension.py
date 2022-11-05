import os


def find_file_by_extension(extension, path):
    global count
    size = 0
    output = ''
    # creating a list for searched files:
    file_list = []

    for root, dirs, files in os.walk(path):
        for searched_file in files:
            # checking if the extension of the file is the searched one:
            if searched_file.split('.')[-1] == extension:
                # append the list of results:
                file_list.append(os.path.join(root, searched_file))

    # preparing the output:
    for each in file_list:
        output += str(each) + '\n'
        size += int(os.path.getsize(each))
        count += 1
    
    output += f'Files found: {count}\n'
    output += f'Total Size: {str(size // (1024*1024))} MB'
    return output


file_extension = input('What file extension do you search for (exe, mp3,  txt...)?: ')
system_path = input('Enter/the/path/in/system: ')
count = 0

result = find_file_by_extension(file_extension, system_path)
print(result)

