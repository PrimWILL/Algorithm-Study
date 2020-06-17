#include <stdio.h>
#include <stdlib.h>

typedef struct stackNode {
    int data;
    struct stackNode* link;
} stackNode;

stackNode* top;

int push(char c);
void pop();

int main(void)
{
    int n;
    scanf("%d", &n);
    while(n--)
    {
        char str[51];
        scanf("%s", str);
        
        for(int i = 0; str[i] != '\0'; i++)
        {
            if(top == NULL) push(str[i]);
            else if(top->data == '(' && str[i] == ')') pop();
            else push(str[i]);
        }
        if(top == NULL) printf("YES\n");
        else printf("NO\n");
        top = NULL;
    }
}

int push(char c)
{   
    stackNode* temp = (stackNode*)malloc(sizeof(stackNode));
    temp->data = c;
    temp->link = top;
    top = temp;
    return 0;
}

void pop()
{   
    stackNode* temp = top;
    top = temp->link;
    free(temp);
}