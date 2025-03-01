import re
import ply.lex as lex

string = """
# DBPedia: obras de Chuck Berry

SELECT ?nome ?desc WHERE {
  ?s a dbo:MusicalArtist.
  ?s foaf:name "Chuck Berry"@en.
  ?w dbo:artist ?s.
  ?w foaf:name ?nome.
  ?w dbo:abstract ?desc.
} LIMIT 1000
"""

# ?s    - Representa um artista musical
# ?w	- Representa uma obra
# ?nome - Nome da obra musical
# ?Desc - Descrição da obra

tokens = (
    'SELECT',
    'WHERE',
    'LIMIT',
    'DOT',
    'LCB',
    'RCB',
    'VAR',
    'LANG',
    'URI',
    'A',
    'INT',
    'COMMENT',
    'STR'
)

t_SELECT = r'SELECT'
t_WHERE = r'WHERE'
t_LIMIT = r'LIMIT'
t_DOT = r'\.'
t_LCB = r'\{'
t_RCB = r'\}'

def t_VAR(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = t.value.strip('?')
    return t

t_LANG = r'@[a-z]{2,3}(-[a-z]{2,3})?'
t_URI = r'[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z_][a-zA-Z0-9_-]*'
t_A = r'a'
t_COMMENT = r'\#.*'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STR(t):
    r'\"([^"\\]*(\\.[^"\\]*)*)\"'
    t.value = t.value.strip('"')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(string)

for tok in lexer:
    print(tok.type, tok.value)
