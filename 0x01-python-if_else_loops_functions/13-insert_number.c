#include "lists.h"

/**
 * insert_node - function that inserts number into sorted singly linked list
 * @head: pointer to pointer to head node
 * @number: value in node to be inserted
 * Return: Address of new_node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr;

	if (head == NULL)
	{
		return (NULL);
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if (number < 0 && number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	ptr = *head;
	while (ptr->next != NULL && (ptr->next)->n < number)
		ptr = ptr->next;
	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
