def e_mail(s):
    if s.count('@') != 1:
        return "NO"
    if s.startswith('@') or s.endswith('@'):
        return "NO"
    if s.startswith('.') or s.endswith('.'):
        return "NO"
    at_index = s.index('@')
    if '.' not in s[at_index:]:
        return "NO"
    if s[at_index + 1] == '.'or s[at_index - 1] == '.':
        return "NO"
    return "YES"
while True:
    try:
        s1 = input()
    except :
        break
    print(e_mail(s1))