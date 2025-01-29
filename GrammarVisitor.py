# Generated from Grammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#root.
    def visitRoot(self, ctx:GrammarParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assign.
    def visitAssign(self, ctx:GrammarParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#printStmt.
    def visitPrintStmt(self, ctx:GrammarParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#condition.
    def visitCondition(self, ctx:GrammarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Unequal.
    def visitUnequal(self, ctx:GrammarParser.UnequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Ops.
    def visitOps(self, ctx:GrammarParser.OpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Equal.
    def visitEqual(self, ctx:GrammarParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Var.
    def visitVar(self, ctx:GrammarParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Num.
    def visitNum(self, ctx:GrammarParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Lt.
    def visitLt(self, ctx:GrammarParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#String.
    def visitString(self, ctx:GrammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Gt.
    def visitGt(self, ctx:GrammarParser.GtContext):
        return self.visitChildren(ctx)



del GrammarParser