grammar Grammar;

root: (statement NEWLINE)* statement? EOF;

statement: assign
        |  printStmt
        |  condition
        ;

assign: ID ':=' expr; 

printStmt: PRINT_CMD WS* expr; 

condition: 'if' expr statement ('else' statement)?;


expr: ID                                      #Var
    | expr ('+' | '-' | '*' | '/' | '^') expr #Ops
    | expr GT expr                            #Gt
    | expr LT expr                            #Lt
    | expr EQ expr                            #Equal
    | expr UNEQ expr                          #Unequal
    | NUM                                     #Num
    | STR                                     #String
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUM: [0-9]+ ;
NEWLINE: [\r\n]+ ;
LT: '<' ;
GT: '>' ;
EQ: '==';
UNEQ: '!=';
PRINT_CMD: 'print' [ \t]*;
STR: '"' ( ~["\n\r] | '\\"')* '"' ;

WS: [ \t]+ -> skip ;