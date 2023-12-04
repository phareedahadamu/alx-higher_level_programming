#include "lists.h"

/**
 * check_cycle - A function that checks if there is a
 *               cycle in a singly linked list
 * @list: Head pointer to the list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
