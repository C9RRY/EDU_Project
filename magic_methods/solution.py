import os
import tempfile


class File:
    def __init__(self, name):
        self.temp_dir = os.path.join(tempfile.gettempdir(), f'{name}')
        with open(self.temp_dir, 'w', encoding='utf-8') as fn:
            self.file = fn





path_to_file = "some_filename"
print(os.path.exists(path_to_file))
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))





