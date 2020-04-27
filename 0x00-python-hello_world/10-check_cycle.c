#include <stdio.h>
#include "lists.h"
/**
 *check_cycle - check if an individually linked list has a cycle.
 *@list: the list to check
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *h,*t;

	if (list == NULL)
		return (0);

	h = t =list;

	while (t != NULL && t->next != NULL)
	{
		h = h->next;
		t = t->next->next;

		if (h == t)
			return (1);
	}
	return (0);
}
