'''В этой проге '''
class WordsFinder:
    def __init__(self, *files: str):
        self.files = [*files]

    def get_all_words(self):
        punct_zn = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for f in self.files:
            all_words_file = []
            with open(f, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for zn in punct_zn:
                        line = line.replace(zn, '')
                    line = line.split()
                    all_words_file += line
                all_words.update({f:all_words_file})
        return all_words
    def find(self, word: str):
        word = word.lower()
        word_search = {}
        position = 1
        for file_name, words_in_file in self.get_all_words().items():
            for word_in_file in words_in_file:
                if word == word_in_file:
                    word_search.update({file_name: position})
                    position = 1
                else:position +=1
        return word_search

    def count(self, word):
        word = word.lower()
        word_search = {}
        for file_name, words_in_file in self.get_all_words().items():
            counter = 0
            for word_in_file in words_in_file:
                if word == word_in_file:
                    counter += 1
            word_search.update({file_name: counter})
        return word_search

if __name__ == '__main__':

    a1 = WordsFinder('test.txt', 'products.txt')
    print(a1.get_all_words())
    print(a1.find('potato'))
    print(a1.count('Спасибо'))
