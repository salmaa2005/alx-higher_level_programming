#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 1 if the list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list) {
  listint_t *slow_ptr;
  listint_t *fast_ptr;

  slow_ptr = fast_ptr = list;
  while (fast_ptr && fast_ptr->next) {
    slow_ptr = slow_ptr->next;
    fast_ptr = fast_ptr->next->next;
    if (slow_ptr == fast_ptr)
      return (1);
  }
  return (0);
}
