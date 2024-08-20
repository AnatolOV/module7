class WordsFinder:
    def __init__(self, *names_files):
        self.file_names = names_files

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            # print(file_name,':')
            with open(file_name, encoding='utf-8') as file:
                intro_ = file.read()
                words = intro_.split()
                words_lower = [word.lower() for word in words]
                exceptions_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for char in exceptions_:
                    words_lower = [word.replace(char, '') for word in words_lower]
                all_words[file_name] = words_lower
        return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        new_dict = {}
        for key, values in dict_.items():
            for value in values:
                if value == word:
                    index = values.index(value)
                    # print(key, index)
                    new_dict[key] = index
        # print(new_dict)
        return new_dict





a = WordsFinder('products.txt', 'test.txt')
print(a.get_all_words())
print(a.find('кодировку'))
