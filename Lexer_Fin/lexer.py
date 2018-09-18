import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'\:SUM'
t_MINUS = r':RES'
t_TIMES = r'\:MUL'
t_DIVIDE = r':DIV'
t_EQUALS = r':='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

lex.input("x = 3 :SUM 4 :RES 5 :MUL 6 :DIV 10")
while True:
    tok = lex.token()
    if not tok: break
    print (str(tok.value) + " - " + str(tok.type))
