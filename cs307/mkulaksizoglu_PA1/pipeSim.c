#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <assert.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
printf("I’m SHELL process, with PID:%d - Main command is: man grep | grep -A 3 -- \"-q\" > output.txt\n", (int) getpid());
	int fd[2];
    	pipe(fd);
    	int rc = fork();
    	
    	if (rc < 0) {
    	 // fork failed; exit
        fprintf(stderr, "fork failed\n");
        exit(1);
	}
	else if (rc==0){
		
	rc = fork();
		if(rc== 0){
		printf("I’m MAN process, with PID: %d- My command is: man grep\n", (int) getpid());
      		close(fd[0]);
		dup2(fd[1], STDOUT_FILENO);

		// now exec "wc"...
        	char *myargs[3];
        	myargs[0] = strdup("man");  // program: man
        	myargs[1] = strdup("grep"); // argument: grep
        	myargs[2] = NULL;           // marks end of array
        	execvp(myargs[0], myargs);  // runs manual of grep
		
        	
		}
		else if (rc>0){
		wait(NULL);
		printf("I’m GREP process, with PID: %d - My command is: grep -A 3 -- \"-q\" \n", (int) getpid());
		dup2(fd[0], STDIN_FILENO); //after dup, fd[0] acts like standartinput
        	close(fd[1]);
        	close(fd[0]);
        	
       
        
       		close(STDOUT_FILENO);
        	open("./output.txt", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
        
        
        
        	char *myargs[6];
        	myargs[0] = strdup("grep"); 
        	myargs[1] = strdup("-A"); // Options that allows specifying amount of line needed
        	myargs[2] = strdup("3"); 
        	myargs[3] = strdup("--");
        	myargs[4] = strdup("-q"); 
        	myargs[5] = NULL;           
		execvp(myargs[0], myargs);  
        	
		
		}
		else{
		fprintf(stderr, "fork failed\n");
       		 exit(1);
		}
		
		
	
	
	}
	else{
	close(fd[1]);
        
        wait(NULL); //shell waits for the children to finish their job
	printf("I’m SHELL process, with PID: %d - execution is completed, you can find the results in output.txt)\n", (int) getpid());
	
	}
	
	return 0;
}
