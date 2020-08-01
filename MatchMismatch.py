#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common. 

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def match_mismatch(in1, in2):
    in1 = set(in1.split(" "))
    in2 = set(in2.split(" "))
    different, common = sorted(list(in1^in2)), sorted(list(in1&in2))

    # for i in in1:
    #     if i in in2:
    #         common.append(i)
    #     else:
    #         different.append(i)
    # for j in in2:
    #     if j in in1:
    #         common.append(i)
    #     else:
    #         different.append(i)
    # common = tuple(common)
    # different = tuple(different)

    print(f"Common:\t\t{common}\nDifferent:\t{different}")

match_mismatch(sentence1, sentence2)