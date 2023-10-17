<<<<<<< HEAD
/*

 * File: 13-is_palindrome.c

 * Auth: Mbah Nkemdinma

 */


#include "lists.h"


listint_t *reverse_listint(listint_t **head);

int is_palindrome(listint_t **head);


/**

 * @head: A pointer to the starting node of the list to reverse.

 *

 * Return: A pointer to the head of the reversed list.

 */

listint_t *reverse_listint(listint_t **head)

{

        listint_t *node = *head, *next, *prev = NULL;


        while (node)

        {

                next = node->next;

                node->next = prev;

                prev = node;

                node = next;

        }


        *head = prev;

        return (*head);
=======
#include "lists.h"


/**

 * reverse_listint - reverses a linked list

 * @head: pointer to the first node in the list

 *

 * Return: pointer to the first node in the new list

 */

void reverse_listint(listint_t **head)

{

  listint_t *prev = NULL;

  listint_t *current = *head;

  listint_t *next = NULL;


  while (current)

    {

      next = current->next;

      current->next = prev;

      prev = current;

      current = next;

    }


  *head = prev;
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9

}


/**

<<<<<<< HEAD
 * is_palindrome - Checks if a singly linked list is a palindrome.

 * @head: A pointer to the head of the linked list.

 *

 * Return: If the linked list is not a palindrome - 0.

 *         If the linked list is a palindrome - 1.
=======
 * is_palindrome - checks if a linked list is a palindrome

 * @head: double pointer to the linked list

 *

 * Return: 1 if it is, 0 if not
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9

 */

int is_palindrome(listint_t **head)

{

<<<<<<< HEAD
        listint_t *tmp, *rev, *mid;

        size_t size = 0, i;


        if (*head == NULL || (*head)->next == NULL)

                return (1);


        tmp = *head;

        while (tmp)

        {

                size++;

                tmp = tmp->next;

        }


        tmp = *head;

        for (i = 0; i < (size / 2) - 1; i++)

                tmp = tmp->next;


        if ((size % 2) == 0 && tmp->n != tmp->next->n)

                return (0);


        tmp = tmp->next->next;

        rev = reverse_listint(&tmp);

        mid = rev;


        tmp = *head;

        while (rev)

        {

                if (tmp->n != rev->n)

                        return (0);

                tmp = tmp->next;

                rev = rev->next;

        }

        reverse_listint(&mid);


        return (1);
=======
  listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;


  if (*head == NULL || (*head)->next == NULL)

    return (1);


  while (1)

    {

      fast = fast->next->next;

      if (!fast)

        {

          dup = slow->next;

          break;

        }

      if (!fast->next)

        {

          dup = slow->next->next;

          break;

        }

      slow = slow->next;

    }


  reverse_listint(&dup);


  while (dup && temp)

    {

      if (temp->n == dup->n)

        {

          dup = dup->next;

          temp = temp->next;

        }

      else

        return (0);

    }


  if (!dup)

    return (1);


  return (0);
>>>>>>> bf9e2de82e4cec68ecf4aea6d965e0ec4f0dabc9

}
