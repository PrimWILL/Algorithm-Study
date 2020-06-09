#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* num_to_bits(unsigned int num, int len) {
    char* bits = (char *) malloc(len + 1);
    // char* bits = (char *) calloc(len + 1, sizeof(char));
    int idx = len-1, i;
    bits[len] = '\0';

    while (num > 0 && idx >= 0) {
        if (num % 2 == 1) {
            bits[idx--] = '1';
        } else { 
            bits[idx--] = '0';
        }
        num /= 2;
    }

    for (i = idx; i >= 0; i--){ 
        bits[i] = '0';
    }
     printf("%s\n", bits);
    return bits;        // return binary bits
}
struct NODE{
  struct NODE * next;
  int data;
};

int main()
{
  struct NODE * head = malloc(sizeof(struct NODE)); //머리 노드 생성
 
  struct NODE * node1 = malloc(sizeof(struct NODE));//첫번째 노드 생성
  head->next=node1; //머리 노드 다음으로 node1 지정
  node1->data=10; //node1의 data에 10 저장
 
  struct NODE * node2 = malloc(sizeof(struct NODE));//두번째 노드 생성
  node1->next=node2; //node1 다음으로 node2 지정
  node2->data=20; //node2의 data에 20 저장 
  printf("node2: %d\n",node2->data);
 
  node2->next=NULL; //node2 다음으로 NULL 지정함으로써 끝을 알림
 
  struct NODE * curr = head->next; //연결리스트 훑을 포인터 선언
  while(curr != NULL){   //포인터가 NULL을 가르키지 않을때 
    printf("%d\n",curr->data); //현재 노드의 data에 저장된 값 출력
    curr = curr->next;  //현재 노드를 현재 노드가 가르키고 있는 다음노드로 변경
  }

 
  free(node2);  // 메모리 해제
  free(node1);
  free(head);  
    unsigned int num = 15;
    int len = 8;
    /*while(1)
    {
        num = num / 2;
        len++;
        if(len == 1) {
            len += 1;
            break;
        }
    }*/  
    unsigned int address = 0x10000000;
    address += 12;
    printf("%d\n", address -0x10000000);
    char c[10];
    scanf("%s", c);
    printf("%s", c);
    printf("%s\n", num_to_bits(num, len));

    char* c1;
    char temp[10];
    scanf("%s", temp);
    char* tmp_char = (char*)malloc(sizeof(char) * 10);
    strcpy(tmp_char, temp);
    c1 = strtok(tmp_char, ":");
    printf("%s", c1);
    return 0; 
}

struct Inst {
    char *name;     // instruction name
    char *op;       // opcode
    char type;      // R, I, J format
    char *funct;    // function code
};

struct Data {
    int value;
    struct Data *next;
};

struct Text {
    int idx;
    char *d;        // rd
    char *s;        // rs
    char *t;        // rt
    unsigned int address;
    struct Text *next;
};

struct Sym {
    char *name;
    int size;
    unsigned int address;
    struct Data *first;
    struct Sym *next;
    struct Data *last;
};