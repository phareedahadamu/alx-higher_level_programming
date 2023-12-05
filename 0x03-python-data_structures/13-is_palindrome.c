#include "lists.h"
#include <stddef.h>
#include <stdio.h>
/**
 * is_palindrome - A function that checks if the numbers in
 *                 a singly linked list is a palindrome
 * @head: Pointer to the first node of the list
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *tmp1 = *head;
	int count = 0, j = 0;

	if (*head == NULL)
		return (1);
	while (tmp->next != NULL)
	{
		count++;
		tmp = tmp->next;
	}
	count++;
	int arr[count];

	while (j < count && tmp1 != NULL)
	{
		arr[j] = tmp1->n;
		j++;
		tmp1 = tmp1->next;
	}
	int i = 0;

	while (i < count)
	{
		if (arr[i] != arr[count - 1])
			return (0);
		count -= 1;
		i += 1;
	}
	return (1);
}
