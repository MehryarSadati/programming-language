import readline
import sys

from antlr4 import InputStream, CommonTokenStream, FileStream
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
        input_stream = InputStream(prompt)  # for terminal input
        lexer = GrammarLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = GrammarParser(tokens)
        tree = parser.root()

        visitor.visit(tree)


if __name__ == "__main__":
    # Check if a file argument is provided
    if len(sys.argv) > 1:
        # for file input
        input_stream = FileStream(sys.argv[1])
        lexer = GrammarLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = GrammarParser(token_stream)
        tree = parser.root()

        visitor = Visitor()
        visitor.visit(tree)
    else:
        main()
