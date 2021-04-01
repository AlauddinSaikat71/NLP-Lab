import re
from builtins import str


class Tokenizer:

    def __init__(self):
        self.BanText = ""
        self.EngText = ""
        self.rawParseEng = []
        self.whitespace = re.compile(u"[\s\u0020\u00a0\u1680\u180e\u202f\u205f\u3000\u2000-\u200a]+", re.UNICODE)
        self.bangla_fullstop = u"\u0964"
        self.punctSeq = u"['\"“”‘’]+|[?!,…]+|[:;]+"
        self.punc = u"[(),$%^&*+={}\[\]:\"|\'\~`<>/,¦!?½£¶¼©⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟↉¤¿º;-]+"
        self.rawBan = ""
        self.rawParseBan = []
        self.temp = []
        self.banDict = dict()
        self.engDict = dict()
        self.total_line = 0
        self.allCharEng = []
        self.allCharBan = []
        self.avgEngSetLen = 0
        self.avgBanSetLen = 0

    def read_data(self):
        with open(
                'C:\\Users\\User\\Desktop\\Ben.txt',
                'r', encoding='UTF-8') as f:
            for line in f:
                self.total_line += 1
                en, bn, _ = line.split('\t')
                self.BanText += bn
                self.EngText += en

    def parse_english_text(self):
        # self.rawParseEng = re.findall(r'\w+', self.EngText)
        # tokenizing the english corpus. len(self.rawParseEng) is the total num of words
        self.rawParseEng = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+", self.EngText)
        return self.rawParseEng

    def parse_bangla_text(self):
        # eliminating the punctuations and whitespaces
        self.rawBan = self.whitespace.sub(" ", self.BanText).strip()
        self.rawBan = re.sub(self.punctSeq, " ", self.rawBan)
        self.rawBan = re.sub(self.bangla_fullstop, " ", self.rawBan)
        self.rawBan = re.sub(self.punc, " ", self.rawBan)

        # tokenizing the bangla corpus. len(self.rawParseBan) is the total num of words
        self.rawParseBan = self.rawBan.split()

    def create_bangla_dict(self):
        # Counting unique words
        for word in self.rawParseBan:
            if word not in self.banDict:
                self.banDict[word] = 1
            else:
                self.banDict[word] += 1

    def create_english_dict(self):
        # Counting unique words
        for word in self.rawParseEng:
            if word not in self.engDict:
                self.engDict[word] = 1
            else:
                self.engDict[word] += 1

    def parse_text_to_chars(self, text, lang):
        # total chars in corpus
        print('Total Character in ' + lang + ' Side: ')
        if lang == 'English':
            self.allCharEng = len(list(text))
            print(self.allCharEng)
        else:
            self.allCharBan = len(list(text))
            print(self.allCharBan)

    def top_ten_freq(self, word_dict):
        freq = []
        for word in word_dict:
            freq.append((word_dict[word] / len(word_dict), word_dict[word], word))

        freq.sort(reverse=True)

        top_ten = []
        for percent, freq_, word_ in freq[0:10]:
            top_ten.append((percent, freq_, word_))

        return top_ten

    def average_sentence_len(self):
        self.temp = re.split(r'[.?!]', self.EngText)

        print('Average English Sentence Length: ')
        self.avgEngSetLen = len(self.rawParseEng) / len(self.temp)
        print(round(self.avgEngSetLen, 2))

        print()
        print('Average Bangla Sentence Length: ')
        self.avgBanSetLen = len(self.rawParseBan) / len(self.temp)
        print(round(self.avgBanSetLen, 2))

    def print_top_ten(self, data, lang):
        print()
        print(lang + ' top ten: ')
        for percentage, freq_, word_ in data:
            print(word_, '\t', freq_, '\t', round(percentage, 4))
        print()

    def write_to_file(self):
        f = open("tokenizer.txt", "w+", encoding="utf-8")
        f.write('Total Unique Words' + '\n')
        f.write('English' + '\t' + 'Bangla' + '\n')
        f.write(str(len(self.engDict)) + '\t' + str(len(self.banDict)) + '\n')
        f.write('')
        f.write('\n')

        f.write('Total Chars \n')
        f.write('English' + '\t' + 'Bangla' + '\n')
        f.write(str(self.allCharEng) + '\t' + str(self.allCharBan) + '\n')
        f.write('')
        f.write('\n')

        f.write('Average Sentence Length \n')
        f.write('English' + '\t' + 'Bangla' + '\n')
        f.write(str(round(self.avgEngSetLen, 2)) + '\t' + str(round(self.avgBanSetLen, 2)))
        f.write('')
        f.write('\n')
        f.write('')
        f.write('\n')

        f.write('Top Ten Words in Bangla: \n')
        f.write('Word' + '\t' + 'Freq' + '\t' + 'Percentage (%)' + '\n')

        banTopTen = self.top_ten_freq(self.banDict)
        for percentage, freq_, word_ in banTopTen:
            f.write(str(word_) + '\t' + str(freq_) + '\t' + str(round(percentage, 4)) + '\n')

        f.write('')
        f.write('\n')
        f.write('Top Ten Words in English: \n')
        f.write('Word' + '\t' + 'Freq' + '\t' + 'Percentage (%)' + '\n')

        engTopTen = self.top_ten_freq(self.engDict)
        for percentage, freq_, word_ in engTopTen:
            f.write(str(word_) + '\t' + str(freq_) + '\t' + str(round(percentage, 4)) + '\n')

        f.close()

    def get_bangla_text(self):
        return self.BanText

    def get_english_text(self):
        return self.EngText

    def get_parsed_english_text(self):
        return self.rawParseEng

    def get_parsed_bangla_text(self):
        return self.rawParseBan

    def get_bangla_dict(self):
        return self.banDict

    def get_english_dict(self):
        return self.engDict

    def get_avg_eng_sentence_len(self):
        return self.avgEngSetLen

    def get_avg_ban_sentence_len(self):
        return self.avgBanSetLen

    def get_all_char_eng(self):
        return self.allCharEng

    def get_all_char_ban(self):
        return self.allCharBan


tokenizer = Tokenizer()
tokenizer.read_data()

tokenizer.parse_english_text()
tokenizer.parse_bangla_text()

tokenizer.create_bangla_dict()
tokenizer.create_english_dict()

tokenizer.print_top_ten(tokenizer.top_ten_freq(tokenizer.get_bangla_dict()), 'Bangla')
tokenizer.print_top_ten(tokenizer.top_ten_freq(tokenizer.get_english_dict()), 'English')

print()
tokenizer.average_sentence_len()

print()
tokenizer.parse_text_to_chars(tokenizer.get_english_text(), 'English')
tokenizer.parse_text_to_chars(tokenizer.get_bangla_text(), 'Bangla')

tokenizer.write_to_file()
