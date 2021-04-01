import re


class Parser:

    def __init__(self):
        self.banText = ""
        self.bangla_fullstop = u"\u0964"
        self.whitespace = re.compile(u"[\s\u0020\u00a0\u1680\u180e\u202f\u205f\u3000\u2000-\u200a]+", re.UNICODE)
        self.bangla_fullstop = u"\u0964"
        self.punctSeq = u"['\"“”‘’]+|[?!,…]+|[:;]+"
        self.punc = u"[(),$%^&*+={}\[\]:\"|\'\~`<>/,¦!?½£¶¼©⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟↉¤¿º;-]+"
        self.punc_sen = u"[!?]"
        self.rawBan = ""
        self.rawParseBan_sent = []
        self.rawParseBan_word = []
        self.temp = []
        self.total_line = 0

    def read_data(self):
        with open(
                'C:\\Users\\User\\Desktop\\Ben.txt',
                'r', encoding='UTF-8') as f:
            for line in f:
                self.total_line += 1
                en, bn, _ = line.split('\t')
                self.banText += bn

    def parse_bangla_sentence(self):
        self.rawBan = self.banText.split(self.bangla_fullstop)
        for s in self.rawBan:
            temp = re.split(self.punc_sen, s)
            for t in temp:
                self.rawParseBan_sent.append(t)

        print('Total Bangla Sentence in the corpus: ' + str(len(self.rawParseBan_sent)))

    def avg_ban_sent_len(self):
        # eliminating the punctuations and whitespaces
        self.rawBan = self.whitespace.sub(" ", self.banText).strip()
        self.rawBan = re.sub(self.punctSeq, " ", self.rawBan)
        self.rawBan = re.sub(self.bangla_fullstop, " ", self.rawBan)
        self.rawBan = re.sub(self.punc, " ", self.rawBan)

        # tokenizing the bangla corpus. len(self.rawParseBan) is the total num of words
        self.rawParseBan_word = self.rawBan.split()

        print('Average Bangla Sentence Length: ' +
              str(round(len(self.rawParseBan_word) / len(self.rawParseBan_sent), 2)))


parser = Parser()
parser.read_data()
parser.parse_bangla_sentence()
parser.avg_ban_sent_len()
