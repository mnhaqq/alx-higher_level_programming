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
	else
	{
		ptr = *head;
		while (ptr != NULL && ptr->next != NULL)
		{
			if ((ptr->next)->n > number || ptr->next == NULL)
			{
				new->next = ptr->next;
				ptr->next = new;
				break;
			}
			ptr = ptr->next;
		}
		return (new);
	}
}
