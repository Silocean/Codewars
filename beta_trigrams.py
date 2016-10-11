'''
Description:

Trigrams are a special case of the n-gram, where n is 3. One trigram is a continious sequence of 3 chars in phrase. Wikipedia

You have to return all trigrams for the given phrase. Return an empty string for phrases shorter than 3.

Example:

trigrams('the quick red') == 'the he_ e_q qu qui uic ick ck k_r _re red'
'''
def trigrams(phrase):
    # Good Luck!
    return ' '.join(map(lambda y:y.replace(' ','_'), [phrase[x:x+3] for x in range(len(phrase)-2)]))