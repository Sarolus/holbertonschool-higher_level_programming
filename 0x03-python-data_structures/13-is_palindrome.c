#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: head node our list
 * Return: return 0 if it is not a palindrome, otherwise 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i = 0, j, *array;

	if (*head == NULL)
		return (1);

	current = *head;
	while (i < current)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}

	for (j = 0; j < i / 2; j++)
	{
		if (array[j] != array[i - j - 1])
			return (0);
	}

	return (1);
}
