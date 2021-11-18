/*** Definition Section has one variable
which can be accessed inside yylex()
and main() ***/
%{

%}

%option noyywrap

ID[a-zA-Z][1-9]*
CONST [0-9]+

/*** Rule Section has three rules, first rule
matches with capital letters, second rule
matches with any character except newline and
third rule does not take input after the enter***/
%%

"int"|"float"|"bool"|"cin"|"cout"|"main"|"#include"|"<iostream>"|"using"|"namespace"|"std"|"while"|"for"|"if"|"else"|"return" {printf("Cuvant cheie: %s\n", yytext);}

{CONST} 	{printf( "Constanta: %s\n", yytext ); }

"("|")"|"{"|"}"|";"|"<<"|">>"|"," {printf( "Separatori: %s\n", yytext );}

"="|"+"|"-"|"*"|"%"|"/"|"++"|"=="|"!="|"<"|">"|">="|"<="|"+="|"-=" {printf( "Operator: %s\n", yytext ); }

{ID} 	{printf( "Identificator : %s\n", yytext ); }


%%

/*** Code Section prints the number of
capital letter present in the given input***/
int main(){

// Uncomment the lines below
// to take input from file
FILE *fp;
char filename[50];
printf("Enter the filename: \n");
scanf("%s",filename);
fp = fopen(filename,"r");
yyin = fp;

yylex();


return 0;
}
