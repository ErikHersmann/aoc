from helper import problem_data

tls_support = 0
ssl_support = 0
for line in problem_data.splitlines():
    # Parse until first [
    # Parse until second ]
    # Parse until end
    i = 0
    abba_found = False
    invalid = False
    inside_brackets = False
    has_ssl = False
    aba_strings = []
    bab_strings = []
    while i < len(line)-2:
        if line[i] == "[":
            inside_brackets = True
        if line[i] == "]":
            inside_brackets = False
        four_window = line[i:i+4]
        if i < len(line)-3 and line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[1+i]:
            abba_found = True if not inside_brackets else abba_found
            invalid = True if inside_brackets else invalid
        three_window = line[i:i+3]
        if line[i] == line[i+2] and line[1+i] != line[i]:
            if not inside_brackets:
                if three_window in aba_strings:
                    has_ssl = True
                bab_strings.append(line[i+1] + line[i] + line[i+1])
            else:
                if three_window in bab_strings:
                    has_ssl = True
                aba_strings.append(line[i+1] + line[i] + line[i+1])
        i += 1
    # print(line, abba_found, invalid)
    tls_support += 1 if (abba_found and not invalid) else 0
    ssl_support += has_ssl
print(tls_support)
print(ssl_support)