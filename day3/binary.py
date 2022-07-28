#!/usr/bin/env python3


def get_zeros_and_ones(bin_list, i):
    zeros = ones = 0
    
    for binary in bin_list:
        if binary[i] == '0':
            zeros += 1
        else:
            ones += 1
    
    return zeros, ones
    
    
def part_one():
    gamma = ''
    epsilon = ''
    
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines(False)
        for i in range(len(lines[0])):
            zeros , ones = get_zeros_and_ones(lines, i)
                            
            if zeros > ones:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'
        
    return int(gamma, 2) * int(epsilon, 2)
    
    
def get_next_list(bin_list, criteria, i):
    zeros, ones = get_zeros_and_ones(bin_list, i)
    
    if criteria == 'O2':
        first = '0'
        second = '1'
    elif criteria == 'CO2':
        first = '1'
        second = '0'
    
    next_list = []
    if zeros > ones:
        for binary in bin_list:
            if binary[i] == first:
                next_list.append(binary)
    else:
        for binary in bin_list:
            if binary[i] == second:
                next_list.append(binary)
    
    return next_list
        
    
def get_rating(bits, bin_list, criteria):
    for i in range(bits):            
        next_list = get_next_list(bin_list, criteria, i)
        if len(next_list) > 0:
            bin_list = next_list
        else:
            break
    
    return int(bin_list[0], 2)
    
    
def part_two():   
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines(False)
        bits = len(lines[0])
        
        o2_rating = get_rating(bits, lines, 'O2')
        co2_rating = get_rating(bits, lines, 'CO2')
    
    return o2_rating * co2_rating
    
    
if __name__ == "__main__":
    p1 = part_one()
    print(f'The power consumption is: {p1}')
    
    p2 = part_two()
    print(f'The life support rating is: {p2}')
