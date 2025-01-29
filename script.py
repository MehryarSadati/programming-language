import readline

from antlr4 import InputStream, CommonTokenStream
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from Visitor import Visitor


def main():
    readline.read_init_file()
    print("Welcome!")
    print("Enter 'exit' to exit the program.")
    visitor = Visitor()
    while True:
        prompt = input("> ")
        if prompt == "exit":
            break
        input_stream = InputStream(prompt)
        lexer = GrammarLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = GrammarParser(tokens)
        tree = parser.root()

        visitor.visit(tree)


if __name__ == "__main__":
    main()
