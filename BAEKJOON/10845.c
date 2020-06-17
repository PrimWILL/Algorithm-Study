#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct queueNode {
    int data;
    struct queueNode* link;
} queueNode;

typedef struct {
    queueNode *front, *rear;
} LQueueType;

LQueueType* createLinkedQueue()
{
    LQueueType *LQ = (LQueueType*)malloc(sizeof(LQueueType));
    LQ->front = NULL;
    LQ->rear = NULL;
    return LQ;
}

int isEmpty(LQueueType* LQ)
{
    if (LQ->front == NULL) return 1;
    else return 0;
}

void push(LQueueType* LQ, int d)
{
    queueNode* temp = (queueNode*)malloc(sizeof(queueNode));
    temp->data = d;
    temp->link = NULL;

    if (LQ->front == NULL){
        LQ->front = temp;
        LQ->rear = temp;
    }
    else {
        LQ->rear->link = temp;
        LQ->rear = temp;
    }
}

int pop(LQueueType* LQ)
{
    queueNode* temp = LQ->front;
    if(isEmpty(LQ)) return -1;
    else {
        int d = temp->data;
        LQ->front = temp->link;
        if(LQ->front == NULL) 
            LQ->rear = NULL;
        free(temp);
        return d;
    }
}

void printSize(LQueueType* LQ)
{
    int cnt = 0;
    queueNode* q = (queueNode*)malloc(sizeof(queueNode));
    q = LQ->front;
    while(q != NULL)
    {
        q = q -> link;
        cnt++;
    }
    printf("%d\n", cnt);
    free(q);
}

void printFront(LQueueType* LQ)
{   
    if(LQ->front != NULL)
        printf("%d\n", LQ->front->data);
    else printf("%d\n", -1);
}

void printBack(LQueueType* LQ)
{
    if(LQ->rear != NULL)
        printf("%d\n", LQ->rear->data);
    else printf("%d\n", -1);
}

int main(void)
{
    int n;
    scanf("%d", &n);

    LQueueType* LQ = createLinkedQueue();
    while(n--)
    {   
        char instruction[1000];
        scanf("%s", instruction);
        if (strcmp(instruction, "push") == 0)
        {
            int d;
            scanf("%d", &d);
            push(LQ, d);
        }
        else if (strcmp(instruction, "pop") == 0)
            printf("%d\n", pop(LQ));
        else if (strcmp(instruction, "empty") == 0)
            printf("%d\n", isEmpty(LQ));
        else if (strcmp(instruction, "size") == 0)
            printSize(LQ);
        else if (strcmp(instruction, "front") == 0)
            printFront(LQ);
        else if (strcmp(instruction, "back") == 0)
            printBack(LQ);
    }
    return 0;
}