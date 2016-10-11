'''
Description:

Mr. E Ven only likes even length words. Please create a translator so that he doesn't have to hear those pesky odd length words. For some reason he also hates punctuation, he likes his sentences to flow.

Your translator should take in a string and output it with all odd length words having an extra letter (the last letter in the word). It should also remove all punctuation (.,?!) as well as any underscores (_).

"How did we end up here? We go?" translated becomes-> "Howw didd we endd up here We go"
'''
import string
def evenator(s):
    return ' '.join(map(lambda x: x + x[len(x)-1] if len(x) % 2 != 0 else x,
          s.translate(None, ',.!?_').split(' '))).strip()