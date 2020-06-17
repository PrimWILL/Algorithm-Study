#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct stackNode {
    int data;
    struct stackNode* link;
} stackNode;

stackNode* top;

int isEmpty()
{
    if(top == NULL) return 1;
    else return 0;
}

int printTop()
{
    if(isEmpty()) return -1;
    else return top->data;
}

int printSize()
{
    stackNode* p = top;
    int size = 0;
    while(p != NULL)
    {
        p = p -> link;
        size++;
    }
    return size;
}

void push(int d)
{
    stackNode* temp = (stackNode*)malloc(sizeof(stackNode));
    temp->data = d;
    temp->link = top;
    top = temp;
}

int pop()
{
    stackNode* temp = top;
    if(isEmpty()) return -1;
    else
    {
        int item = temp->data;
        top = temp->link;
        free(temp);
        return item;
    }
}

int main(void)
{
    int n;
    scanf("%d", &n);

    while(n--)
    {
        char instruction[10];
        int d = 0;
        scanf("%s", instruction);
        if(strcmp(instruction, "push") == 0)
        {
            /* push: 정수 d를 스택에 넣는 연산 */
            scanf("%d", &d);
            push(d);
        }
        else if(strcmp(instruction, "top") == 0)
        {
            /* top: 스택에 가장 위에 있는 정수 출력 */
            printf("%d\n", printTop());
        }
        else if(strcmp(instruction, "size") == 0)
        {
            /* size: 스택에 들어있는 정수의 개수를 출력 */
            printf("%d\n", printSize());
        }
        else if(strcmp(instruction, "pop") == 0)
        {
            /* 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력 */
            /* 만약 스택에 들어있는 정수가 없는 경우 -1을 출력 */
            printf("%d\n", pop());
        }
        else if(strcmp(instruction, "empty") == 0)
        {
            /* 스택이 비어있으면 1, 아니면 0을 출력 */
            printf("%d\n", isEmpty());
        }
    }
    return 0;
}