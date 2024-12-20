""" make a list of sentences that use the vocative case """
import nltk
nltk.download('punkt')


def main():
    """
    make the O.txt file
    maha.txt is the text of the mahabharata
    """
    with open('maha.txt', 'r', encoding='utf-8') as mahafile:
        maha = mahafile.read()

    output = []

    string_maha = maha.replace('\n', ' ')
    tok = nltk.sent_tokenize(string_maha)
    with open('O.txt', 'w') as filename:
        for sentence in tok:
            words = nltk.word_tokenize(sentence)
            for word in words:
                if word == 'O':
                    sentence = sentence.replace('"', '')
                    sentence = sentence.replace("'", '')
                    sentence = ' '.join(sentence.split())
                    output.append(sentence)
        output = set(output)
        for sentence in output:
            filename.write(sentence + '\n')

if __name__ == '__main__':
    main()
