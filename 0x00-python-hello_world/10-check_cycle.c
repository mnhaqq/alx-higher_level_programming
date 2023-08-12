#include "lists.h"

/**
 * check_cycle - function to check if there's a cycle in a linked list
 * @list: linked list
 * Return: 0 if there's no cycle, 1 if there's a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
