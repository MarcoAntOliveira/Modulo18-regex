import re


string  ='este e um teste de expressoes regulares'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub (r'teste','ABCD',  string))


regexp = re.compile(r'teste')
regexp.search(string)
regexp.findall(string)
regexp.sub(string, 'bd')