#include <stdio.h>
#include "Python.h"

/**
 * print_item_info - Print the information of items of a python list
 * @Item: Item of an python object.
 * @itemIndex: Index of the items of a python list.
 */
void print_item_info(PyObject *Item, int itemIndex)
{
	char *itemName;

	itemName = (char *)Py_TYPE(Item)->tp_name;
	printf("Element %d: %s\n", itemIndex, itemName);
}

/**
 * print_python_list_info - Main function that manage the printing of
 * a python list informations.
 * @p: Pointer of our python list.
 */
void print_python_list_info(PyObject *p)
{
	int itemIndex, allocObjNb;
	Py_ssize_t objListsize = 0;
	PyObject *Item;

	if (PyList_Check(p))
	{
		objListsize = PyList_Size(p);
		allocObjNb = ((PyListObject *)p)->allocated;

		printf("[*] Size of the Python list = %d\n", (int)objListsize);
		printf("[*] Allocated = %d\n", allocObjNb);
		for (itemIndex = 0; itemIndex < objListsize; itemIndex++)
		{
			Item = PyList_GetItem(p, itemIndex);
			print_item_info(Item, itemIndex);
		}
	}
}
