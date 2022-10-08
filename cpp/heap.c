

#include <stdio.h>

#include <stdlib.h>

#define PQ_SIZE 50

typedef int item_type;

typedef struct {
    item_type q[PQ_SIZE+1]; /* body of queue */
    int n; /* number of queue elements */
} priority_queue;

int pq_parent(int n) {
    if (n == 1) {
        return(-1);
    }
    return((int)n/2);
}

int pq_young_child(int n) {
    return(2 * n);
}

void pq_swap(priority_queue *q, int n, int m) {
    item_type buffer;
    buffer = q->q[n];
    q->q[n] = q->q[m];
    q->q[m] = buffer;
}

void bubble_up(priority_queue *q, int p) {
    if (pq_parent(p) == -1) {
        return; /* at root of heap, no parent */
    }
    if (q->q[pq_parent(p)] > q->q[p]) {
        pq_swap(q, p, pq_parent(p));
        bubble_up(q, pq_parent(p));
    } 
}

void pq_insert(priority_queue *q, item_type x) {
    if (q->n >= PQ_SIZE) {
        printf("Warning: priority queue overflow! \n");
    } else {
        q->n = (q->n) + 1;
        q->q[q->n] = x;
        bubble_up(q, q->n);
    }
}

void pq_show(priority_queue *q) {
    int i; /* counter */
    for (i = 0; i <= q->n; i++) {
        printf("%d ", q->q[i]);
    }
    printf("\n");
}

void pq_init(priority_queue *q) {
    q->n = 0;
}

void make_heap(priority_queue *q, item_type s[], int n) {
    int i; /* counter */
    pq_init(q);
    for (i = 0; i < n; i++) {
        pq_insert(q, s[i]);
    }
}

void bubble_down(priority_queue *q, int p) {
    int c; /* child index */
    int i; /* counter */
    int min_index; /* index of lightest child */
    c = pq_young_child(p);
    min_index = p;
    for (i = 0; i <= 1; i++) {
        if ((c + i) <= q->n) {
            if (q->q[min_index] > q->q[c + i]) {
                min_index = c + i;
            }
        }
    }
    if (min_index != p) {
        pq_swap(q, p, min_index);
        bubble_down(q, min_index);
    }
}

item_type extract_min(priority_queue *q) {
    int min = -1; /* minimum value */
    if (q->n <= 0) {
        printf("Warning: empty priority queue.\n");
    } else {
        min = q->q[1];
        q->q[1] = q->q[q->n];
        q->n = q->n - 1;
        bubble_down(q, 1);
    }
    return(min);
}

void heapsort_(item_type s[], int n) {
    int i; /* counters */
    priority_queue q; /* heap for heapsort */
    make_heap(&q, s, n);

    for (i = 0; i < n; i++) {
        s[i] = extract_min(&q);
    } 
}

void array_show(item_type s[], int n) {
    int i; /* counter */
    for (i = 0; i < n; i++) {
        printf("%d ", s[i]);
    }
    printf("\n");
}

int main() {
    priority_queue *pq = malloc(sizeof(priority_queue));

    // int my_numbers[] = {18, 21, 29, 14};
    int my_numbers[] = {18, 21, 29, 14, 25, 17, 19, 22, 26, 20};
    size_t n = sizeof(my_numbers)/sizeof(my_numbers[0]);

    // array_show(my_numbers, n);
    // heapsort_(my_numbers, n);
    // array_show(my_numbers, n);


    make_heap(pq, my_numbers, n);
    pq_show(pq);

    // int min = extract_min(pq);
    // printf("%d\n", min);

    pq->q[1] = 23;
    bubble_down(pq, 1);

    pq_show(pq);

    return 0;
}