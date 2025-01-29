# Simple Programming Language

This repository contains a simple programming language implemented using ANTLR4 and Python. The language's grammar is defined in `Grammar.g4`, and the corresponding lexer, parser, and visitor are generated accordingly.

## Getting Started

### Prerequisites

- **Python 3.x**
- **ANTLR4 Tool**: Required for generating lexer and parser from the grammar file.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/MehryarSadati/programming-language.git
   cd programming-language
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install ANTLR4**:
    Download ANTLR4 Tool: ANTLR4 Complete JAR
    Move the JAR File: Place it in the project directory.

    For convenience, you can add an alias to your shell profile.

4. **Generate Lexer, Parser and Visitor (with -no-listener flag.)**:
   ```bash
   antlr4 -Dlanguage=Python3 -no-listener -visitor Grammar.g4
   ```

5. **You can run programs written in this language using the interpreter by executing script.py.**:
```bash
python3 script.py
```
