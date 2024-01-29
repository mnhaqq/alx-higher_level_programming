#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function to check whether a linked list is a palindrome
 * @head: pointer to head pointer
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int i, left, right;
	int len_list = len_listint(*head);
	int *arr;

	arr = malloc(sizeof(int) * len_list);
	if (arr == NULL)
		return (1);
	ptr = *head;
	i = 0;
	while (ptr != NULL)
	{
		arr[i] = ptr->n;
		i++;
		ptr = ptr->next;
	}

	left = 0;
	right = len_list - 1;
	while (left < right)
	{
		if (arr[left] != arr[right])
		{
			free(arr);
			return (0);
		}
		left++;
		right--;
	}
	free(arr);
	return (1);
}

/**
 * len_listint - function to find length of linked list
 * @h: pointer to head node
 * Return: number of node
 */
int len_listint(const listint_t *h)
{
	const listint_t *ptr;
	int n;

	ptr = h;
	n = 0;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		n++;
	}
	return (n);
}
