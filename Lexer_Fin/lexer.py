import ply.lex as lex

tokens = [ 'NAME','NUMBER','EQUALS' ]

reserved = {'SUM' : 'PLUS', 'RES':'MINUS', 'MUL':'TIMES', 'DIV':'DIVIDE'}

tokens += reserved.values()
t_ignore = ' \t'

t_EQUALS = r':='



def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

lex.input("x = 3 + 4 RES 5 MUL 6 DIV 10")
while True:
    tok = lex.token()
    if not tok: break
    print (str(tok.value) + " - " + str(tok.type))
