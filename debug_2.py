examples = []
n_in = 0
n_out = 0
with open("examples_2.txt") as f:
    lines = f.readlines()
    header = lines[0].split(" ")
    n_in = int(header[0])
    n_out = int(header[1])
    
    i = 1
    while i < len(lines):
        ex = []
        ins = []
        for j in range(n_in):
            ins.append(lines[i].strip())
            i += 1
        outs = []
        for j in range(n_out):
            outs.append(lines[i].strip())
            i += 1
        
        ex.append(ins)
        ex.append(outs)
        examples.append(ex)
        i += 1

print(examples)

i_example = 0
i_item_in = 0
def input():
    global i_example
    global i_item_in
    
    s = examples[i_example][0][i_item_in]
    
    print(s)
    i_item_in += 1
    # if i_item_in > (n_in + n_out):
    #     i_example = (i_example + 1) 
    #     i_item_in += 0
    return s

def set_i_ex(i):
    global i_example
    i_example = i

# i_item_out = 0
# old_print = print
# def print(*values: object, sep = " ", end = "\n", file = None, flush = False):
#     global i_item_out
    
#     s = sep.join(values)
    
#     i_item_out += 1
#     old_print(values, sep=sep, end=end, file=file, flush=flush)