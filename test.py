def tokenizer(expression):
    tokens = []
    
    conditional_flag = 0
    biconditional_flag = 0
    for character in expression:
        if character == '<' and biconditional_flag == 0:
            biconditional_flag = 1
        elif character == '=' and biconditional_flag == 1:
            biconditional_flag = 2
        elif character == '>' and biconditional_flag == 2:
            tokens.append('<=>')
            biconditional_flag = 0
        elif character == '=' and conditional_flag == 0:
            conditional_flag = 1
        elif character == '>' and conditional_flag == 1:
            tokens.append('=>')
            conditional_flag = 0
        elif conditional_flag != 0 or biconditional_flag != 0:
            raise Exception(f"Invalid Syntax")
        elif character.islower() or character.isupper() or character in "!|&()":
            tokens.append(character)
        elif character.isspace():
            pass
        else:
            raise Exception(f"Invalid Character Input: {character}")
    if conditional_flag != 0 or conditional_flag != 0:
        raise Exception(f"Invalid Syntax")
    return tokens


def main():
    tokens = tokenizer("(A & b) <=> c t")
    print(tokens)

if __name__ == "__main__":
    main()