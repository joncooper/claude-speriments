#include <Python.h>
#include <stdio.h>
int main(int argc, char** argv){
  Py_Initialize();
  int rc=0;
  if(argc>1){ FILE* f=fopen(argv[1],"r"); if(f){ rc=PyRun_SimpleFile(f, argv[1]); fclose(f);} else {perror("open");rc=2;} }
  if(Py_FinalizeEx()<0) rc=120;
  return rc;
}
