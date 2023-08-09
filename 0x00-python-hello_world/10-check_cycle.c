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
	int i = 0, len = 0;

	if (!list)
		return (0);
	len = length_of_list(list);
	while (moving_point->next != NULL)
	{
		if ((i + 1) > len)
			break;
		moving_point = moving_point->next;
		if (fix_point == moving_point)
		{
			return (1);
		}
		i++;
	}
	return (0);
}
/**
 * length_of_list - calculates the length of a linked list
 * @list: linked list to calculate the length of
 *
 * Return: length of the linked list
 */
int length_of_list(listint_t *list)
{
	int length = 0;

	while (list != NULL)
	{
		length++;
		list = list->next;
	}

	return (length);
}
