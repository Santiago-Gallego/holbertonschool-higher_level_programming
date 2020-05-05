#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - Check if list is a palindrome
 * @head: list
 * Return: 1 if is palindrome
 **/
int is_palindrome(listint_t **head)
{
	listint_t *a = *head;
	listint_t *b = *head;

	if (*head == NULL)
		return (1);

	while (b && b->next && b->next->next)
	{
		a = a->next;
		b = b->next->next;
	}

	a = reverse_list(&a);
	b = *head;
	while (a && b)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}

	return (1);
}

/**
 * reverse_list - Reverse
 * @head:list
 * Return: new head
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}
