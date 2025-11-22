"""
P:
- We're building a structure
- All building blocks are cubes
- Structure is in layers
- Upper layer block must be supported by four below
- Top of structure is a single block (sounds like a pyramid)
- A block in a lower can support multiple upper
- No gaps between blocks

- Input: # of blocks
- Output: 

Questions:
- Are all blocks the same size?
- Do we have to use as many blocks as possible?
- Can a layer be a single 

Implicit Rules:
- Layer number correlates with blocks in layer (1, 2, 3 squared)

Example:
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

Data Structures:
- Input: integer
- Could use nested list to represent the structuree

Algorithm
- Take the number provided
- Add up the squares of the number 
- Once the sum of squares exceeds the number, go back 
- the difference in the number and the last number is the remaining blocks

"""

def calculate_leftover_blocks(n):
    blocks_remaining = n
    next_layer = 1
    blocks_required = next_layer ** 2
    total_layers = 0

    while blocks_remaining >= blocks_required: #9 #9
        blocks_remaining = blocks_remaining - blocks_required
        total_layers += 1
        next_layer += 1 #2
        blocks_required = next_layer ** 2 # 4
        print(f'Blocks Remaining: {blocks_remaining}')

    return blocks_remaining

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True