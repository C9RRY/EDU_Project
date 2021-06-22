import os
import tempfile



class File:

    def __init__(self, name):
        self.temp_dir = os.path.join(f"{name}")
        self.file = File.file_exist(self)

    def file_exist(self):
        if os.path.exists(self.temp_dir):
            with open(self.temp_dir, 'w', encoding='utf-8') as fl:
                return fl
        else:
            open(self.temp_dir, 'w', encoding='utf-8')
            return ()

    def read(self):
        return self.file





path_to_file = "some_filename"
print(os.path.exists(path_to_file))
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
print(file_obj.read())





