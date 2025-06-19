import re

inputs = open('./input.txt').read().split('\n')
for string in inputs:
    match = re.match(r'([A-Za-z-]+)-(\d{3})\[([A-Za-z]{5})\]',string)
    s,r_id,order = match.groups()
    decrypted = ' '.join([''.join([chr((((ord(c)-97)+int(r_id))%26)+97) for c in word]) for word in s.split('-')])
    if 'north' in decrypted:
        print(decrypted, r_id)