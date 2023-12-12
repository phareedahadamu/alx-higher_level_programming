#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t i;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < PyList_Size(p); i++)
		{
			PyTypeObject *type = (PyTypeObject *)PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, type->tp_name);
		}
	}
}
