from nlp_tokenizer_2016831027 import tokenizer
import matplotlib.pyplot as plt


class Histogram:

    def draw_histogram(self):
        x_axis = ['English', 'Bangla']
        y_axis = [len(tokenizer.get_english_dict()), len(tokenizer.get_bangla_dict())]
        plt.xlabel('Language')
        plt.ylabel('Total Unique Words')
        plt.title('Unique Words English vs. Bangla')
        plt.bar(x_axis, y_axis, facecolor='blue', alpha=0.5, width=0.8)
        plt.show()

        x_axis = ['English', 'Bangla']
        y_axis = [tokenizer.get_avg_eng_sentence_len(), tokenizer.get_avg_ban_sentence_len()]
        plt.xlabel('Language')
        plt.ylabel('Average Sentence Length')
        plt.title('Average Sentence Length English vs. Bangla')
        plt.bar(x_axis, y_axis, facecolor='red', alpha=0.5, width=0.8)
        plt.show()

        x_axis = ['English', 'Bangla']
        y_axis = [tokenizer.get_all_char_eng(), tokenizer.get_all_char_ban()]
        plt.xlabel('Language')
        plt.ylabel('Total chars')
        plt.title('Number of Chars English vs. Bangla')
        plt.bar(x_axis, y_axis, facecolor='green', alpha=0.5, width=0.8)
        plt.show()


histogram = Histogram()
histogram.draw_histogram()
