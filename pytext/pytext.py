import re


class ParserText:
    def __init__(self, path: str):
        self.file_path = path
        with open(self.file_path, "rt", encoding="utf-8") as file:
            self.file_contents = file.read()

    
    def remove_empty_lines(self):
        modified_content = re.sub(r'^\s*\n', '', self.file_contents, flags=re.MULTILINE)
        self.save_file(modified_content)


    def save_file(self, content: str):
        with open(self.file_path, "wt", encoding="utf-8") as file:
            file.write(content)

