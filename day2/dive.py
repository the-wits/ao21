#!/usr/bin/env python3


def part_one():
    horizontal = 0
    depth = 0
    
    with open("input.txt", "r") as file:
        for line in file:
            move = line.split()
            if move[0] == "forward":
                horizontal += int(move[1])
            elif move[0] == "down":
                depth += int(move[1])
            elif move[0] == "up":
                depth -= int(move[1])
            else:
                print("[ERROR]\nNon valid input!\n")
    
    return horizontal * depth


def part_two():
    horizontal = 0
    depth = 0
    aim = 0    
    
    with open("input.txt", "r") as file:
        for line in file:
            move = line.split()
            if move[0] == "forward":
                horizontal += int(move[1])
                depth += aim * int(move[1])
            elif move[0] == "down":
                aim += int(move[1])
            elif move[0] == "up":
                aim -= int(move[1])
            else:
                print("[ERROR]\nNon valid input!\n")
    
    return horizontal * depth 
    
    
if __name__ == "__main__":
    p1 = part_one()
    print(p1)
    
    p2 = part_two()
    print(p2)
