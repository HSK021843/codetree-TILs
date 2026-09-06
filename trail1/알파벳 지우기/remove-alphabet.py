def extract_number(string):
    extracted = ''

    for e in string:
        if e.isdigit():
            extracted += e
    
    return int(extracted)

    
f_str = input()
s_str = input()

print(extract_number(f_str) + extract_number(s_str))