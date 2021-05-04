#include <stdio.h>
#include <Python.h>

/**
 * print_item_info - Print the information of items of a python list
 * @item: Item of an python object.
 * @itemIndex: Index of the items of a python list.
 */
void print_item_info(PyObject *item, int itemIndex)
{
	char *itemName;

	itemName = (char *)Py_TYPE(item)->tp_name;
	printf("Element %d: %s\n", itemIndex, itemName);
}

/**
 * print_python_list_info - Main function that manage the printing of
 * a python list informations.
 * @p: Pointer of our python list.
 */
void print_python_list_info(PyObject *p)
{
	int itemIndex, allocObjNb = 0;
	Py_ssize_t objListSize = 0;
	PyObject *item;

	if (PyList_Check(p))
	{
		objListSize = PyList_Size(p);
		allocObjNb = ((PyListObject *)p)->allocated;

		printf("[*] Size of the Python List = %d\n", (int)objListSize);
		printf("[*] Allocated = %d\n", allocObjNb);
		for (itemIndex = 0; itemIndex < objListSize; itemIndex++)
		{
			item = PyList_GetItem(p, itemIndex);
			print_item_info(item, itemIndex);
		}
	}
}
