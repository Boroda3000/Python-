class WordsFinder:
    
    def __init__(self, *files):
        self.file_names  = list(files)

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            words = []
            with open(file, 'r', encoding = 'utf-8') as file_:
                for word in file_:
                    word = word.lower()
                    word = word.strip()
                    word = word.replace(',', '')
                    word = word.replace('.', '')
                    word = word.replace('=', '')
                    word = word.replace('?', '')
                    word = word.replace('!', '')
                    word = word.replace(';', '')
                    word = word.replace(':', '')
                    word = word.replace(' - ', '')
                    words.extend(word.split())
            all_words[file] = words
        return all_words   
    
    def find(self, word):
        find_dict = {}
        for key, value in self.get_all_words().items():
            find_dict[key] = value.index(word.lower()) + 1
        return find_dict

    def count(self, word):
        count_dict = {}
        for key, value in self.get_all_words().items():
            count_dict[key] = value.count(word.lower())
        return count_dict
    

finder2 = WordsFinder('test_7,3.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего