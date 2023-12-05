#include "lists.h"
/**
 * insert_node - A function that inserts a new node in
 *               a sorted singly linked list
 * @head: Pointer to the list
 * @number: The number to be inserted
 * Return: returns the address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	listint_t *tmp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	tmp = (*head)->next;
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (new->n < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	tmp = (*head)->next;
	while (current->next != NULL)
	{
		if (new->n < tmp->n)
			break;
		current = current->next;
		tmp = tmp->next;
	}
	new->next = tmp;
	current->next = new;
	return (new);
}
