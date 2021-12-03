import numpy as np

def determine_binary_gamma(digits):
    binary_gamma = ''
    for ind in range(0,np.shape(digits)[1]):
        binary_gamma = binary_gamma + str(int(np.sum(digits,0)[ind] >= np.shape(digits)[0]/2))
    return binary_gamma

def determine_binary_epsilon(digits):
    binary_epsilon = ''
    for ind in range(0,np.shape(digits)[1]):
        binary_epsilon = binary_epsilon + str(int(np.sum(digits,0)[ind] < np.shape(digits)[0]/2))
    return binary_epsilon


def determine_oxygen_rating(binary_list):
    tmp_list = binary_list
    bit_idx = 0
    while np.shape(tmp_list)[0] > 1:
        compare_against = int(determine_binary_gamma(tmp_list)[bit_idx])
        for reading_idx in range(np.shape(tmp_list)[0]-1, -1, -1):
            if tmp_list[reading_idx, bit_idx] != compare_against:
                tmp_list = np.delete(tmp_list, reading_idx, 0)
        bit_idx += 1
    binary_rating = ''
    for char in tmp_list[0]:
        binary_rating = binary_rating + str(char) 
    return binary_rating


def determine_CO2_scrubber_rating(binary_list):
    tmp_list = binary_list
    bit_idx = 0
    while np.shape(tmp_list)[0] > 1:
        compare_against = int(determine_binary_epsilon(tmp_list)[bit_idx])
        for reading_idx in range(np.shape(tmp_list)[0]-1, -1, -1):
            if tmp_list[reading_idx, bit_idx] != compare_against:
                tmp_list = np.delete(tmp_list, reading_idx, 0)
        bit_idx += 1
    binary_rating = ''
    for char in tmp_list[0]:
        binary_rating = binary_rating + str(char) 
    return binary_rating

### Part 1
file = open('Day_3_inpt.txt', 'r')
lines = file.readlines()

binary_digits = np.array([[int(digit) for digit in (line.strip())] for line in lines])
binary_gamma = determine_binary_gamma(binary_digits)
binary_epsilon = determine_binary_epsilon(binary_digits)

print('Binary gamma is ' + str(binary_gamma) + ' therefore binary epsilon is ' + str(binary_epsilon) +
     ' and the power consumption ' + str(int(binary_gamma,2)*int(binary_epsilon,2)))

## Part 2
print('The oxygen rating is ' + determine_oxygen_rating(binary_digits) + ' the CO2 scrubber rating is ' 
    + determine_CO2_scrubber_rating(binary_digits) + ' their product is ' +
    str(int(determine_oxygen_rating(binary_digits),2) * int(determine_CO2_scrubber_rating(binary_digits),2)))