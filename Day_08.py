import numpy as np
import re

from numpy.lib.ufunclike import _fix_out_named_y

#region: Additional functions
def convert_to_bin(term):
    term_list = list([0,0,0,0,0,0,0])
    for pos, char in enumerate('abcdefg'):
        if term.find(char) != -1:
            term_list[pos] = 1
    return term_list
    
def analyze_pattern_bin(terms):
    decoded = []
    for ind in range(0,10):
        decoded.append(convert_to_bin('00000000'))
    for count, term in enumerate(terms):
        terms[count] = convert_to_bin(term)
    orig_terms = terms.copy()
    # search for the unambigous numbers 1,4,7,8
    for term in terms:
        if sum(term) == 2:
            decoded[1] = term
        elif sum(term) == 4:
            decoded[4] = term
        elif sum(term) == 3:
            decoded[7] = term
        elif sum(term) == 7:
            decoded[8] = term
    # delete terms that have been found
    for deco in decoded:
        try:
            for i in range(0,len(terms)):
                terms.remove(deco)
            break
        except:
            continue
    # decode the remaining terms
    while len(terms) > 0:
        # if 4 and (1 or 7) have been decoded, we can identify 0, 6 and 9
        if sum(decoded[4]) == 4 and (sum(decoded[1]) == 2 or sum(decoded[7]) == 2):
            for term in terms:
                if sum(term) == 6:
                    if sum(np.array(term)*np.array(decoded[4])) == 4:   # it is a 9
                        decoded[9] = term
                    elif sum(np.array(term)*np.array(decoded[4])) == 3: # it is a 0 or a 6
                        if sum(decoded[1]) == 2:       # 1 has been decoded
                            if sum(np.array(term)*np.array(decoded[1])) == 1:   # it is a 6
                                decoded[6] = term
                            else:   # it is a 0
                                decoded[0] = term
                        elif sum(decoded[7]) == 3:    # 7 has been decoded
                            if sum(np.array(term)*np.array(decoded[7])) == 2:   # it is a 6
                                decoded[6] = term
                            else:   # it is a 0
                                decoded[0] = term 
                elif sum(term) == 5:    # this could be a 2,3,5
                    if sum(decoded[1]) == 2:    # the 1 and 4 is known
                        if sum(np.array(term)*np.array(decoded[4])) == 2:   # it is a 2
                            decoded[2] = term 
                        elif sum(np.array(term)*np.array(decoded[4])) == 3: # it is a 5 or 3
                            if sum(np.array(term)*np.array(decoded[1])) == 2:   # it is a 3
                                decoded[3] = term 
                            else:   # it is a 5
                                decoded[5] = term 
                    elif sum(decoded[7]) == 3:    # the 7 and 4 is known
                        if sum(np.array(term)*np.array(decoded[4])) == 2:   # it is a 2
                            decoded[2] = term 
                        elif sum(np.array(term)*np.array(decoded[4])) == 3: # it is a 5 or 3
                            if sum(np.array(term)*np.array(decoded[7])) == 3:   # it is a 3
                                decoded[3] = term 
                            else:   # it is a 5
                                decoded[5] = term
        # if 1 and 7 have been identified, we can identify 6
        if sum(decoded[1]) == 2 and sum(decoded[7]) == 3:
            for term in terms:
                if sum(term) == 6:  # this may be a 6
                    if sum(np.array(term)*np.array(decoded[1])) == 1:
                        if sum(np.array(term)*np.array(decoded[7])) == 2:   # this is a 6
                            decoded[6] = term
            # we can also identify 3
            for term in terms:
                if sum(term) == 5:  # this may be a 3
                    if sum(np.array(term)*np.array(decoded[1])) == 2 and sum(np.array(term)*np.array(decoded[7])) == 3: # it is a 3
                        decoded[3] = term
        # delete terms that have been found
        for deco in decoded:
            try:
                for i in range(0,len(terms)):
                    terms.remove(deco)
                break
            except:
                continue
    # All numbers have been deciphered (even though we would just need the last 4)
    digits = ''
    for term in orig_terms[10:14]:
        for number,deciphered in enumerate(decoded):
            if term == deciphered:
                digits = digits + str(number)
    return int(digits)

#endregion: Addtional functions
#region: Digits positions
file = open('Day_8_inpt.txt', 'r')
digits = list()
outputs = list()
for counter, line in enumerate(file.readlines()):
    digits.append([x for x in line.strip().split('|')[0].split(' ')[0:-1]])
    outputs.append([x for x in line.strip().split('|')[1].split(' ')[1::]])
#endregion: Digits loaded
#region: Part 1
counter = np.zeros(10)
for output in outputs:
    for term in output:
        if len(term) == 2:  # found a 1
            counter[1] += 1
        elif len(term) == 4:    # found a 4
            counter[4] += 1
        elif len(term) == 3:    # found a 7
            counter[7] += 1
        elif len(term) == 7:    # found a 8
            counter[8] += 1
print('There are ' + str(np.sum(counter)) + ' 1, 4, 7 or 8 in the outputs')
#endregion: Part 1 complete!
#region: Part 2
final_sum = 0
for idx, digit in enumerate(digits):
    tmp = digit
    for output in outputs[idx]:
        tmp.append(output)
    final_sum += analyze_pattern_bin(tmp)
print('The final sum of all outputs is: ' + str(final_sum))
#endregion: Part 2 complete!