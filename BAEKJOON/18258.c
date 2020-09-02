#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*typedef struct QueueNode {
    int data;
    struct QueueNode *link;
} QueueNode;

typedef struct {
    QueueNode *rear, *front;
} Queue;

void init(Queue *q)
{
    q->rear = q->front = NULL;
}

int is_empty(Queue *q)
{
    return (q->front == NULL);
}

int size(Queue *q)
{
    int cnt = 0;
    if (is_empty(q)) return 0;
    for (QueueNode *temp = q->front; temp != NULL; temp = temp->link)
        cnt++;
    return cnt;
}

void push(Queue *q, int data)
{
    QueueNode* temp = (QueueNode*)malloc(sizeof(QueueNode));
    temp->data = data;
    temp->link = NULL;
    if (is_empty(q)) {
        q->front = temp;
        q->rear = temp;
    }
    else {
        q->rear->link = temp;
        q->rear = temp;
    }
}

int pop(Queue *q)
{
    if (is_empty(q))
        return -1;
    int temp = q->front->data;
    q->front = q->front->link;
    return temp;
}

int front(Queue *q)
{
    if (is_empty(q))
        return -1;
    return q->front->data;
}

int back(Queue *q)
{
    if (is_empty(q))
        return -1;
    return q->rear->data;
}

int main(void)
{
    Queue q;
    init(&q);

    int N;
    scanf("%d", &N);

    while(N--) {
        char str[10];
        scanf("%s", str);
        if (!strcmp(str, "push")) {
            int data = 0;
            scanf("%d", &data);
            push(&q, data);
        }
        else if (!strcmp(str, "front"))
            printf("%d\n", front(&q));
        else if (!strcmp(str, "back"))
            printf("%d\n", back(&q));
        else if (!strcmp(str, "pop"))
            printf("%d\n", pop(&q));
        else if (!strcmp(str, "size"))
            printf("%d\n", size(&q));
        else if (!strcmp(str, "empty"))
            printf("%d\n", is_empty(&q));
    }
    return 0;
}*/

typedef struct Queue {
    int data[2000000];
    int front, rear;
} Queue;

void init(Queue *q) {
    q->front = q->rear = -1;
}

int is_empty(Queue *q) {
    return (q->front == q->rear);
}

int size(Queue *q) {
    if (is_empty(q)) {
        return 0;
    }
    return (q->rear - q->front);
}

void push(Queue *q, int data) {
    q->data[++(q->rear)] = data;
}

int pop(Queue *q) {
    if (is_empty(q)) return -1;
    return q->data[++(q->front)];
}

int front(Queue *q) {
    if (is_empty(q)) return -1;
    return q->data[q->front + 1];
}

int back(Queue *q) {
    if (is_empty(q)) return -1;
    return q->data[q->rear];
}

int main(void) {
    Queue q;
    init(&q);

    int N;
    scanf("%d", &N);

    while(N--) {
        char str[6];
        scanf("%s", str);
        if (!strcmp(str, "push")) {
            int data = 0;
            scanf("%d", &data);
            push(&q, data);
        }
        else if (!strcmp(str, "front"))
            printf("%d\n", front(&q));
        else if (!strcmp(str, "back"))
            printf("%d\n", back(&q));
        else if (!strcmp(str, "pop"))
            printf("%d\n", pop(&q));
        else if (!strcmp(str, "size"))
            printf("%d\n", size(&q));
        else if (!strcmp(str, "empty"))
            printf("%d\n", is_empty(&q));
    }
    return 0;
}