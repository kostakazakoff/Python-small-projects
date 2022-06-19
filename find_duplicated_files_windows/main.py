from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import fnmatch
import os


class MainWidget(Widget):
    pass
#     def press(self):
#         input_text = self.input_text.text
#         files_size = 0
#         output = ''
#         chk_name = []
#         duplicated = []
#         list_of_files = []
#
#         # creating a list of each files from the entered system path:
#         # chk_name contains just the names of files
#         # list_of_files contains the full path
#         for root, dirs, files in os.walk(input_text):
#             for name in files:
#                 if fnmatch.fnmatch(name, '*.*'):
#                     chk_name.append(name)
#                     list_of_files.append(os.path.join(root, name))
#         # using the chk_name list for searching the duplicates
#         # and using the index (dupl_index) to operate in the list_of_files
#         # because the equal indexes of the same files in both lists:
#         for n in chk_name:
#             files_counter = chk_name.count(n)
#             # using the counter - using this iteration,
#             # checking if they are a duplicated files by each of the names in chk_name list:
#             if files_counter > 1:
#                 for i in range(files_counter):
#                     dupl_index = chk_name.index(n)
#                     dupl_info = list_of_files[dupl_index]
#                     # append the (full path) file from the list_of_files to the duplicated list
#                     # using the same index:
#                     duplicated.append(dupl_info)
#                     # removing the names and file info (full path) from the lists:
#                     chk_name.remove(n)
#                     list_of_files.remove(dupl_info)
#         # if they are duplicated files in the list (checking the length of the list):
#         if len(duplicated) > 0:
#             for each in duplicated:
#                 # preparing the output (file info and size):
#                 output += str(each) + '\n'
#                 files_size += int(os.path.getsize(each))
#         else:
#             output = 'No duplicated files found' + '\r'
#
#         output += '========================================================' + '\n'
#         output += 'Duplicated files size: ' + str(files_size // (1024 * 1024)) + ' MB'
#         return output


class Action(GridLayout):
    def __init__(self, **kwargs):
        super(Action, self).__init__(**kwargs)
        self.cols = 1
        self.path_input = TextInput(multiline=False)
        self.add_widget(self.path_input)
        self.button = Button(text='Go', fontsize=18)
        self.button.bind(self.press())
        self.add_widget(self.button)
        self.output = self.press()
        self.result = Label(text=self.output)
        self.add_widget(self.result)

    def press(self, path_input):
        input_text = path_input.text
        files_size = 0
        output = ''
        chk_name = []
        duplicated = []
        list_of_files = []

        # creating a list of each files from the entered system path:
        # chk_name contains just the names of files
        # list_of_files contains the full path
        for root, dirs, files in os.walk(input_text):
            for name in files:
                if fnmatch.fnmatch(name, '*.*'):
                    chk_name.append(name)
                    list_of_files.append(os.path.join(root, name))
        # using the chk_name list for searching the duplicates
        # and using the index (dupl_index) to operate in the list_of_files
        # because the equal indexes of the same files in both lists:
        for n in chk_name:
            files_counter = chk_name.count(n)
            # using the counter - using this iteration,
            # checking if they are a duplicated files by each of the names in chk_name list:
            if files_counter > 1:
                for i in range(files_counter):
                    dupl_index = chk_name.index(n)
                    dupl_info = list_of_files[dupl_index]
                    # append the (full path) file from the list_of_files to the duplicated list
                    # using the same index:
                    duplicated.append(dupl_info)
                    # removing the names and file info (full path) from the lists:
                    chk_name.remove(n)
                    list_of_files.remove(dupl_info)
        # if they are duplicated files in the list (checking the length of the list):
        if len(duplicated) > 0:
            for each in duplicated:
                # preparing the output (file info and size):
                output += str(each) + '\n'
                files_size += int(os.path.getsize(each))
        else:
            output = 'No duplicated files found' + '\r'

        output += '========================================================' + '\n'
        output += 'Duplicated files size: ' + str(files_size // (1024 * 1024)) + ' MB'
        return output


class DFinder(App):
    def build(self):
        return Action()


if __name__ == '__main__':
    DFinder().run()
