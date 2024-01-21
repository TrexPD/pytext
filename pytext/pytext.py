import re
from rich import print


class TextParser:
    def __init__(self, path: str):
        self.file_path = path
        with open(self.file_path, "rt+", encoding="utf-8") as file:
            self.file_contents = file.read()

    def remove_empty_lines(self):
        try:
            modified_content: re.sub = re.sub(r'^\s*\n', '', self.file_contents, flags=re.MULTILINE)
        except Exception as error:
            return "Error:", error
        else:
            self.file_contents = modified_content

    def remove_lines(self, row: int | list[int]):
        try:
            contents_list = self.file_contents.splitlines()
            
            if isinstance(row, list):
                inverse_row: list = sorted(row, reverse=True)
                for list_index in inverse_row:
                    contents_list.pop(list_index)
            else:
                contents_list.pop(row)
        except Exception as error:
            return "Error:", error
        else:
            self.file_contents = "\n".join(contents_list)

    def save_file(self, content: str):
        with open(self.file_path, mode="wt", encoding="utf-8") as file:
            file.write(content)

    def show(self):
        print(self.file_contents)

