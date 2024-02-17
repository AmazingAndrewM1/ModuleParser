def parser(expression):
    tokens = []
    
    conditional_flag = 0
    biconditional_flag = 0
    for character in expression:
        if character.islower() or character.isupper():
            tokens.append('VAR')
        elif character == '!':
            tokens.append('!')
        elif character == '|':
            tokens.append('|')
        elif character == '&':
            tokens.append('&')
        elif character == '(':
            tokens.append('(')
        elif character == ')':
            tokens.append(')')
        elif character == '=' and conditional_flag == 0:
            conditional_flag = 1
        elif character == '>' and conditional_flag == 1:
            tokens.append('=>')
            conditional_flag = 0
        elif character == '<' and biconditional_flag == 0:
            biconditional_flag = 1
        elif character == '=' and biconditional_flag == 1:
            biconditional_flag = 2
        elif character == '>' and biconditional_flag == 2:
            tokens.append('<=>')
            biconditional_flag = 0
        elif character.isspace():
            pass
        else:
            raise Exception(f"Invalid Character Input: {character}")
    return tokens


def main():
    tokens = parser("(A & b) <= c")
    print(tokens)

if __name__ == "__main__":
    main()