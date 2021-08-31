def load_words(filename):
    wordlist = list()
    # 'with' can automate finish 'open' and 'close' file
    with open(filename) as f:
        # fetch one line each time, include '\n'
        for line in f:
            # strip '\n', then append it to wordlist
            wordlist.append(line.rstrip('\n'))
    print
    " ", len(wordlist), "words loaded."
    print
    '\n'.join(wordlist)
    return wordlist


wordlist = load_words('all_words.txt')
