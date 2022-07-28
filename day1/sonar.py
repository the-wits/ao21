#!/usr/bin/env python3


def increments():
    n = 0
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        current_val = int(lines[0])
        
        for i in range(1, len(lines)):
            next_val = int(lines[i])
            if current_val < next_val:
                n += 1
            current_val = next_val

    return n


def window_increments():
    n = 0
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        current_win = int(lines[0]) + int(lines[1]) + int(lines[2])
        
        for i in range(1, len(lines) - 2):
            next_win = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
            if current_win < next_win:
                n += 1
            current_win = next_win
            
    return n
    

if __name__ == "__main__":
    #increments()
    print(window_increments())
