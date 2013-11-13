import urllib
import json
import nltk

"""
Quick implementation to analyze word frequency in job posts
"""
def main():
    # 1. download all positions
    # 2. jsonify
    # 3. loop through all pages

    # first 6 pages (only 6 page of jobs)
    descriptions = []
    for page in xrange(7):
        text = json.loads(urllib.urlopen('http://jobs.github.com/positions.json?page=%d' % page).read())
        # only interested in descriptions
        # filter out html tags
        descriptions.extend(nltk.clean_html(post['description']) for post in text)

    # tokenizations
    desc_tokens = (nltk.word_tokenize(desc) for desc in descriptions)

    # concat all tokens, allow dups
    all_tokens = []
    for t in desc_tokens:
        all_tokens.extend(t)

    # all get stop words
    stop_words = nltk.corpus.stopwords.words()

    # plus some known useless words
    stop_words.extend(['we', 'a', 're', 'you', 'the', 'us', '.', '..', '...'])

    # only keep ascii
    tokens = [token.lower() for token in all_tokens if token not in stop_words and token.lower().isalpha()]

    # count frequency
    fdist = nltk.FreqDist(tokens)

    return get_top_tokens(fdist, 100)

def get_top_tokens(fdist, count = 50):
    # keep top 50
    top_tokens = []
    counter = 0

    for key,val in fdist.items():
        if val > 1 and counter < count:
            top_tokens.append((key, val))
            counter +=1

    return top_tokens

if __name__ == '__main__':
    print main()
