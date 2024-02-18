class leaf():
    def __init__(self, value):
        self.value = value


class unaryNode():
    def __init__(self, value):
        self.value = value
        self.child = None

    def setChild(child_node):
        child = child_node

class binaryNode():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def set_left_child(child_node):
        left_child = child_node

    def set_right_child(child_node):
        right_child = child_node

class Parser:
    def __init__(self, expression):
        self.tokens = self.tokenizer(expression)
        self.offset = ''
        self.expression()
        if len(self.tokens) > 0:
            raise ValueError("The parser completed without reading all of the tokens")
        print("___________________________________________________________________")


    def tokenizer(self, expression):
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

    def eat(self, character):
        if len(self.tokens) == 0:
            raise ValueError(f"Unexpected end of input; expected '{character}'")
        if self.tokens[0] != character:
            raise ValueError(f"Expected '{character}' but read '{self.tokens[0]}'")
        return self.tokens.pop(0)
    
    def is_next(self, character):
        if len(self.tokens) == 0:
            return False
        if self.tokens[0] != character:
            return False
        return True
    
    # checks if the next character is a var
    def is_next_var(self):
        if len(self.tokens) == 0:
            print("THE TOKEN STRING IS EMPTY")
            return False
        return self.tokens[0].islower() or self.tokens[0].isupper()


    def expression(self):
        print(f"{self.offset}calling conjunction")
        self.offset = self.offset + '\t'

        output_node = self.conjunction()

        self.offset = self.offset[:-1]

        return output_node


    def biconditional(self):
        raise NotImplementedError("Biconditional function not yet implemented.")

    def conditional(self):
        raise NotImplementedError("Conditional function not yet implemented.")

    def disjunction(self):
        raise NotImplementedError("Disjunction function not yet implemented.")

    def conjunction(self):
        
        print(f"{self.offset}calling negation")
        self.offset = self.offset + '\t'

        left_node = self.negation()
        self.offset = self.offset[:-1]

        while self.is_next('&'):
            print(self.tokens)
            print(f"{self.offset}eating '&'")
            
            output_node = binaryNode(self.eat('&'))
            output_node.left_child = left_node
            
            
            print(f"{self.offset}calling negation")
            self.offset = self.offset + '\t'

            output_node.right_child = self.negation()
            
            self.offset = self.offset[:-1]
            print(f"{self.offset}the current node is {output_node.value} with a left child {output_node.left_child.value} and a right child {output_node.right_child.value}")
            return output_node
        return left_node

    def negation(self):
        # Todo, try putting while to solve multiple negation bug
        if self.is_next('!'):
            print(f"{self.offset}eating '!'")
            print(self.tokens)
            self.eat('!')
            print(f"{self.offset}calling basic")
            self.offset = self.offset + '\t'
            output_node = unaryNode('!')
            output_node.child = self.basic()
            self.offset = self.offset[:-1]
            print(f"{self.offset}the current node is {output_node.value} with a child {output_node.child.value}")
            return output_node
        print(f"{self.offset}calling basic")
        self.offset = self.offset + '\t'
        output_node = self.basic()
        self.offset = self.offset[:-1]
        return output_node

    def basic(self):
        if self.tokens[0] == '(':
            print(self.tokens)
            self.eat("(")

            #comment out when done
            print(f"{self.offset}eating '('")
            print(f"{self.offset}calling expression")
            self.offset = self.offset + '\t'
            output_node = self.expression()
            self.offset = self.offset[:-1]

            
            print(self.tokens)
            self.eat(")")

            #comment out when done
            print(f"{self.offset}eating ')'")
            return output_node

        
        if self.is_next_var():
            #comment out when done
            print(self.tokens)
            print(f"{self.offset}eating '{self.tokens[0]}'")
            output_node = leaf(self.eat(self.tokens[0]))
            print(f"{self.offset}leaf node is {output_node.value}")
            return output_node
        raise ValueError('Malformed expression.')


def main():
    input = "(!A&B)"
    parser = Parser(input)








if __name__ == "__main__":
    main()