import fnmatch
import os


class Duplicated:
    def __init__(self):
        self.size = 0
        self.file_names = []
        self.duplicated = []
        self.list_of_files = []

    def find_duplicated_files(self, sys_path):
        '''
        creating a list of all files from the entered system path:
        file_names contains just the names of files
        list_of_files contains the full path
        '''
        for root, dirs, files in os.walk(sys_path):
            for name in files:
                if fnmatch.fnmatch(name, '*.*'):
                    self.file_names.append(name)
                    self.list_of_files.append(os.path.join(root, name))
        '''
        using the file_names list for searching the duplicates
        and using the index (dupl_index) to operate in the list_of_files
        because the equal indexes of the same files in both lists:
        '''
        for name in self.file_names:
            files_counter = self.file_names.count(name)
            '''
            using the counter - using this iteration,
            checking if they are a duplicated files by file of the names in file_names list:
            '''
            if files_counter > 1:
                for i in range(files_counter):
                    dupl_index = self.file_names.index(name)
                    dupl_info = self.list_of_files[dupl_index]
                    self.duplicated.append(dupl_info)
                    self.size += int(os.path.getsize(dupl_info))
                    print(dupl_info)
                    self.file_names.remove(name)
                    self.list_of_files.remove(dupl_info)

        return self.duplicated, self.size


dupl = Duplicated()
source_path = input('Enter a system path for the search: ')
duplicated_files, duplicated_files_size = dupl.find_duplicated_files(source_path)
print(f'Duplicated files size: {duplicated_files_size / (1024 * 1024):.1f} MB')
