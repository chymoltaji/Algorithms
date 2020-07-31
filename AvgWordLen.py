# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

def avg_word_len(sentence):
    count = list(map(len, sentence.split(' ')))
    total = sum(count)
    avg = total/len(count)
    print(avg)

avg_word_len("yhergtfaw tgefds dgfs gtfd f gdtsfd g tgrf gdfsvads gsdf")
avg_word_len("gbsv gfd rgfds graf rfasd htegfa tshgfadfgshfadrgthgfargsthgfa")