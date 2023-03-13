#include <stdio.h>
#include <stdlib.h>
#include  "lists.h"
/* Helper function to reverse a linked list */
void reverse(listint_t **head)
{
    listint_t *prev = NULL, *curr = *head, *next = NULL;
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    *head = prev;
}

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL) {
        /* An empty list or a list with only one element is a palindrome */
        return 1;
    }

    /* Find the middle node of the linked list */
    listint_t *slow = *head, *fast = *head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    /* Reverse the second half of the linked list */
    reverse(&slow);

    /* Compare the first half with the reversed second half */
    listint_t *p1 = *head, *p2 = slow;
    while (p2) {
        if (p1->n != p2->n) {
            /* The linked list is not a palindrome */
            return 0;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    /* Restore the original linked list by reversing the second half again */
    reverse(&slow);

    /* The linked list is a palindrome */
    return 1;
}

