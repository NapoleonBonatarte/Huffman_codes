

def str_to_codes(text,mapping):
    retarr = []
    for letter in text:
        if letter == "<END>":
            break
        if letter in mapping:
            retarr.append(mapping[letter])
    retarr.append(mapping["<END>"])
    return retarr

def codes_to_chunks(codes):
    all_nums = ''
    retarr = []
    tempval = ''
    for i in codes:
        for j in i:
            all_nums += j
    for bit in all_nums:
        tempval += bit
        if len(tempval) == 8:
            retarr.append(tempval)
            tempval = ''
    if len(tempval) > 0:
        retarr.append(tempval + '0' * (8 - len(tempval)))
    return retarr

def print_chunks_as_decimal(chunks):
    for chunk in chunks:
        print(int(chunk,base=2),end=' ')

def ints_to_bits(vals):
    retstring = ''
    for i in vals:
        temp = bin(i)[2:]

        retstring += ((8-len(temp)))* '0' + temp
    return retstring

def bits_to_str(bits, root):
    end_string = ''
    index = 0
    cur = root
    while len(bits) > index:
        if type(cur) is str:
            if cur == '<END>':
                break
            end_string += cur
            cur = root
            index -= 1
        else:
            if bits[index] == '0':
                cur = cur.left
            else:
                cur = cur.right
        index += 1
        
    return end_string


