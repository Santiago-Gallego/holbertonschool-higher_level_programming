#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int find_node(listint_t **h, int number);
listint_t *insert_nodeint_at_index(listint_t **head, int idx, int n);

/**
 * insert_node - insert a new node
 * @head: a pointer to a pointer
 * @number: value of the n member
 * Return: a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t **ptr = head;
	listint_t *insert = NULL;
	int id;

	id = find_node(ptr, number);
	insert = insert_nodeint_at_index(ptr, id, number);
	return (insert);
}

/**
 * insert_nodeint_at_index - inserts a new node
 * @head: a pointer to a pointer
 * @id: the index
 * @n: value of the n element of the node
 * Return: a pointer to the new node
 */

listint_t *insert_nodeint_at_index(listint_t **head, int id, int n)
{
	listint_t **current = head;
	listint_t *access = *head;
	listint_t *newnode;
	listint_t *prev = NULL;
	int i = 0;

	if (head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = n;
	if (id == 0)
	{
		newnode->next = *current;
		*current = newnode;
	}
	else
	{
		while (i != id)
		{
			if (access->next != NULL)
			{
				prev = access;
				access = access->next;
				++i;
			}
			else if (id <= (i + 1))
			{
				access->next = newnode;
				return (newnode);
			}
			else
				return (NULL);
		}
		newnode->next = access;
		prev->next = newnode;
	}
	return (newnode);
}
/**
 * find_node - returns number of the first node
 * @h: pointer to the first element of the list
 * @number:int
 * Return: index of first node
 */
int find_node(listint_t **h, int number)
{
	listint_t *num = *h;
	int count = 0;

	while (num != NULL)
	{
		if (num->n < number)
		{
			count++;
		}
		num = num->next;
	}
	return (count);
}
