#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *fix_point = list, *moving_point = list;

	if (!list)
		return (0);

	while (moving_point->next != NULL)
	{
		moving_point = moving_point->next;
		if (fix_point == moving_point)
		{
			return (1);
		}
	}
	return (0);
}
