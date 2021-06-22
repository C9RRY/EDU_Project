import os
import tempfile


class File:

    def __init__(self, name):
        self.file_dir = os.path.join(f"{name}")
        self.file = File.file_exist(self)

    def __add__(self, other):
        added_string = self.read() + other.read()
        dir_of_file = os.path.join(tempfile.gettempdir(), self.file_dir)
        added_file = File(dir_of_file)
        added_file.write(added_string)
        return added_file

    def __iter__(self):
        return self

    def __next__(self):
        x =
        return 2

    def file_exist(self):
        if os.path.exists(self.file_dir):
            with open(self.file_dir, 'r', encoding='utf-8') as fl:
                return fl.read()
        else:
            open(self.file_dir, 'w', encoding='utf-8')
            return ()

    def read(self):
        return self.file

    def write(self, string):
        self.file = string
        with open(self.file_dir, 'w', encoding='utf-8') as fl:
            fl.write(self.file)









path_to_file = "some_filename"
print(os.path.exists(path_to_file))
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
print(file_obj.read())
file_obj.write("some_text")
print(file_obj.read())
file_obj.write("other_text")
print(file_obj.read())
file_obj_1 = File(path_to_file + '1')
file_obj_2 = File(path_to_file + "2")
file_obj_1.write("line 1 \n")
file_obj_2.write("line 2 \n")
new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))
print(tempfile.gettempdir())
for line in new_file_obj:
    print(ascii(line))



