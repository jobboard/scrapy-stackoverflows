import json
import nltk
import sys
import urllib

"""
Quick implementation to analyze word frequency in job posts
"""
def main(Company = None):
    # 1. download all positions
    # 2. jsonify
    # 3. loop through all pages

    # first 6 pages (only 6 page of jobs)
    descriptions = []
    for page in xrange(7):
        text = json.loads(urllib.urlopen('http://jobs.github.com/positions.json?page=%d' % page).read())

        # only interested in descriptions
        # filter out html tags

        # only interested in one company?
        if Company:
            descriptions.extend(nltk.clean_html(post['description']) for post in text if post['company'].lower() == Company)
        else:
            descriptions.extend(nltk.clean_html(post['description']) for post in text)

    # tokenizations
    desc_tokens = (nltk.word_tokenize(desc) for desc in descriptions)

    # concat all tokens, allow dups
    all_tokens = []
    for t in desc_tokens:
        all_tokens.extend(t)

    # all get stop words
    stop_words = nltk.corpus.stopwords.words()

    # only keep ascii
    tokens = [token.lower() for token in all_tokens if token not in stop_words and token.lower().isalpha()]

    # plus some known useless words + punctuations
    punctuations = (',', '.', '*', '!', ':', '>', '<')
    punctuations = [p*i for p in punctuations for i in xrange(5)]
    common_words = ['we', 'a', 're', 'you', 'the', 'us', 'if', 'or', 'as', 'well', 'our', 'amp']
    common_words.extend(punctuations)
    tokens = [token.lower() for token in tokens if token not in common_words]

    # count frequency
    fdist = nltk.FreqDist(tokens)

    show_word_count = 100

    fdist.plot(show_word_count)
    return get_top_tokens(fdist, show_word_count)

def get_top_tokens(fdist, count = 50):
    # keep top 50
    top_tokens = []
    counter = 0

    for key, val in fdist.items():
        if val > 1 and counter < count:
            top_tokens.append((key, val))
            counter += 1

    return top_tokens

if __name__ == '__main__':
    company = None
    if len(sys.argv) > 1:
        company = sys.argv[1]
    print main(Company = company)
