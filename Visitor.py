import operator
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^':operator.pow}

if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
    from .GrammarVisitor import GrammarVisitor
else:
    from GrammarParser import GrammarParser
    from GrammarVisitor import GrammarVisitor


class Visitor(GrammarVisitor):
    def __init__(self):
        self.myvars = {}

    def visitRoot(self, ctx):
        for child in ctx.statement():
            self.visit(child)

#written by myself in case of error check with 
    def visitAssign(self, ctx):
        # l = list(ctx.getChildren())
        # self.myvars[self.visit(l[0])] = self.visit(l[2])

        #debuging:
            
        var = ctx.ID().getText()
        value = self.visit(ctx.expr())
        print(f"Debug: Assigning {var} = {value}")  # Debug line
        self.myvars[var] = value
        print(f"Debug: myvars = {self.myvars} and the dict is {self.myvars.items()}")    # Debug line

#debuging completed but don't fully trust it yet
    def visitPrintStmt(self, ctx):
        value = self.visit(ctx.expr())
        var = ctx.expr().getText()
        if var in self.myvars:
            print(self.myvars[var])
        elif value is not None:
            print(value)


    def visitNum(self, ctx):
        return int(ctx.NUM().getText())
    
    def visitString(self, ctx):
        return ctx.STR().getText()

    def visitVar(self, ctx):
        var = ctx.ID().getText()
        if var in self.myvars:
            return self.myvars[var]
        else:
            print(f"ERROR! variable '{var}' not assigned!")
            return None
        
    def visitOps(self, ctx):
        l = list(ctx.getChildren())
        return ops[l[1].getText()](self.visit(l[0]), self.visit(l[2]))
    
    def visitGt(self, ctx):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) > self.visit(l[2]))
    
    def visitLt(self, ctx):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) < self.visit(l[2]))
    
    def visitEqual(self, ctx):
        l = list(ctx.getChildren())
        return (self.visit(l[0]) == self.visit(l[2]))
    
    def visitUnequal(self, ctx):
        l = list(ctx.getChildren())
        return (self.visit(l[0]) != self.visit(l[2]))
    
    def visitCondition(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]) == 1:
            return self.visit(l[2])
        elif len(l) > 3:
            if l[3].getText() == "else":
                return self.visit(l[4])