import re

# Explicitly typed syntax (only allows int, float, str, bool)
TOKEN_TYPES = {
    r"def": "DEF",
    r"return": "RETURN",
    r"[a-zA-Z_][a-zA-Z0-9_]*": "IDENTIFIER",
    r"[0-9]+": "INTEGER",
    r"[0-9]+\.[0-9]+": "FLOAT",
    r"[-+*/=]": "OPERATOR",
    r"[\(\)\{\}]": "SYMBOL"
}

def tokenize(code):
    tokens = []
    while code:
        for pattern, tag in TOKEN_TYPES.items():
            match = re.match(pattern, code)
            if match:
                tokens.append((tag, match.group(0)))
                code = code[len(match.group(0)):].strip()
                break
    return tokens

# Test
code = "def add(x: int, y: int) -> int: return x + y"
print(tokenize(code))
