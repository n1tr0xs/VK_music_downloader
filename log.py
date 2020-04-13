class LogFile():
    def __init__(self, folder:str):
        self.file_path = folder + 'log.txt'
        self.downloaded = self.parse()
        
    def write_(self, song:str):
        with open(self.file_path, 'a', encoding='utf-8') as out:
            out.write(song + '\n')

    def parse(self) -> list:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return set(file.read().split('\n'))
        except FileNotFoundError:
            return []
