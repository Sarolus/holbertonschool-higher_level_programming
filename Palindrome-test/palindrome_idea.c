#include "lists.h"

/**
 * _ListLen - Give the lenght of a linked list
 * @head: head node of our list.
 * Return: return the size of the list.
 */
int _ListLen(listint_t *head)
{
	listint_t *current = head;
	size_t size = 0;

	while (current)
	{
		size++;
		current = current->next;
	}

	return (size);
}
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: head node our list
 * Return: return 0 if it is not a palindrome, otherwise 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i = 0, j, *array, limit, listlen;

	if (*head == NULL || head == NULL)
		return (1);

	listlen = _ListLen(*head);
	array = malloc(sizeof(int) * listlen);

	current = *head;
	while (current)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}

	limit = (i % 2 == 0) ? i / 2 : (i + 1) / 2;

	for (j = 0; j < limit; j++)
	{
		if (array[j] != array[i - 1 - j])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
