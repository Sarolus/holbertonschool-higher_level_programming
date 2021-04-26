#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: the checked list
 * Return: return 0 if there is no cycle, otherwise 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tmp = list;

	if (!list && !list->next)
	{
		while (!tmp && !head && !head->next)
		{
			head = head->next;
			tmp = tmp->next->next;

			if (head == tmp)
				return (1);
		}
	}

	return (0);
}
