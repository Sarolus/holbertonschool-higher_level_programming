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

	while (!tmp && !head->next && !head->next->next)
	{
		head = head->next->next;
		tmp = tmp->next;

		if (head == tmp)
		{
			head = list;
			while (head != tmp)
			{
				head = head->next;
				tmp = tmp->next;
			}
			return (1);
		}
	}

	return (0);
}
