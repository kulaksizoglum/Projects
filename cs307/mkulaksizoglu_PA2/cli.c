
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <assert.h>
#include <sys/wait.h>
typedef struct{
char cmd[32];
char input[32];
char option[32];
char redirection[32];
char background[32];
}arr;



int
main(int argc, char *argv[])
{
  FILE *file =fopen("commands.txt", "r");
  FILE *wfile;
  char fname[]="parse.txt";
  wfile = fopen(fname,"w");
  char buffer[128];
  
  while(fgets(buffer, sizeof(buffer), file) != NULL){
  	
  	arr command;
  	char *args[32];
  	char *token;
  	bool option= false;
	bool input = false;
	bool background= false;
	bool redirection= false;
  	int x= 0;
  	token = strtok(buffer," \n");
  	
  	strcpy(command.cmd,token);
  	args[x]= token;
  	 token= strtok(NULL," \n");
  	  x++; 
  	fprintf(wfile,"----------\n");
  	fprintf(wfile,"Command: %s\n",command.cmd);
 
  	 
  	while(token != NULL){
  	
 

  	  if (token[0] == '-'){
		option = true;
		strcpy(command.option,token);
  	  }
  	  else if(token[0] =='<' || token[0] == '>'){
  	  	redirection = true;
  	  	strcpy(command.redirection,token);
  	  	args[x]= token;
  	  	token= strtok(NULL," \n");
  	  	
  	  }
  	  else if(token[0]=='&'){
  	  	background= true;
  	  	strcpy(command.background,token);
  	  }
  	  else{
		input = true;
		strcpy(command.input,token);  	  
  	  }
  	  
  	  args[x]= token;
  	  token= strtok(NULL," \n");
  	  x++; 
  	}
  	
  	
  	
  	
  	  if(input){
  	  fprintf(wfile,"Input: %s\n",command.input);
  	  }
  	  else{
  	  fprintf(wfile,"Input: \n");
  	  }
  	  if(option){
  	  fprintf(wfile,"Option: %s\n",command.option);
  	  }
  	  else{
  	  fprintf(wfile,"Option: \n");
  	  }
  	  if (redirection){
	  fprintf(wfile,"Redirection: %s\n",command.redirection);	  	  
  	  }
  	  else{
  	  fprintf(wfile,"Redirection: -\n");
  	  }
  	  if (background){
  	  fprintf(wfile,"Background job: y\n");
  	  }
  	  else{
  	  fprintf(wfile,"Background job: n\n");
  	  }
  	fprintf(wfile,"----------\n");
  	args[x]= NULL; 
  	
  	
  	
  	
  }
  fclose(file);
  fclose(wfile);
    return 0;
}

