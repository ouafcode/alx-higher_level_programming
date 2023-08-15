#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int len = PyList_Size(p);
	int j;
	PyListObject *objt = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", objt->allocated);
	for (j = 0; j < len; j++)
		printf("Element %i: %s\n", j, Py_TYPE(objt->ob_item[j])->tp_name);
}
