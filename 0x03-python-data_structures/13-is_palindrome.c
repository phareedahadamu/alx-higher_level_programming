#include "lists.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * add_nodeint - A function that adds a new node at the start of the list
 * @head: A pointer to the head pointer
 * @n: The integer at athe the new node
 * Return: The address of the new node on success else NULL
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = n;
	if (*head == NULL)
	{
		*head = new_node;
	}
	else
	{
		new_node->next = *head;
		*head = new_node;
	}
	return (*head);
}
/**
 * is_palindrome - A function that checks if the numbers in
 *                 a singly linked list is a palindrome
 * @head: Pointer to the first node of the list
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *head2 = NULL, *tmp = *head, *tmp2 = *head;

	while (tmp->next != NULL)
	{
		add_nodeint(&head2, tmp->n);
		tmp = tmp->next;
	}
	add_nodeint(&head2, tmp->n);
	while (head2 != NULL && tmp2 != NULL)
	{
		if (head2->n != tmp2->n)
			return (0);
		head2 = head2->next;
		tmp2 = tmp2->next;
	}
	free_listint(head2);
	return (1);
}
