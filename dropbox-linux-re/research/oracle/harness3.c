#include <Python.h>
#include <stdio.h>
static void chk(PyStatus s){ if(PyStatus_Exception(s)){ fprintf(stderr,"[init-fail]\n"); Py_ExitStatusException(s);} }
int main(void){
  PyStatus st; PyConfig cfg; PyConfig_InitIsolatedConfig(&cfg);
  cfg.use_environment=0; cfg.site_import=0; cfg.pathconfig_warnings=0;
  chk(PyConfig_SetBytesString(&cfg,&cfg.home,"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905"));
  chk(PyConfig_SetBytesString(&cfg,&cfg.program_name,"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/dropbox"));
  cfg.module_search_paths_set=1;
  chk(PyWideStringList_Append(&cfg.module_search_paths, L"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/python-pypkg.zip"));
  chk(PyWideStringList_Append(&cfg.module_search_paths, L"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/python-pyext"));
  chk(Py_InitializeFromConfig(&cfg)); PyConfig_Clear(&cfg);
  fprintf(stderr,"[c] init OK\n");
  PyObject* sysm=PyImport_ImportModule("sys");
  if(!sysm){ fprintf(stderr,"[c] import sys FAILED\n"); PyErr_Print(); return 3; }
  PyObject* ver=PyObject_GetAttrString(sysm,"version");
  const char* vs = ver? PyUnicode_AsUTF8(ver): "?";
  fprintf(stderr,"[c] sys.version=%s\n", vs?vs:"(null)");
  // try importing zipimport and loading a code object WITHOUT executing it
  const char* code =
    "import os,sys,zipimport,opcode,json\n"
    "os.write(2,b'[py] driver live\n')\n"
    "z=zipimport.zipimporter(r'/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/python-pypkg.zip')\n"
    "os.write(2,b'[py] zipimporter ok\n')\n"
    "c=z.get_code('abc')\n"              // stdlib module, decrypt+unmarshal, NO exec
    "os.write(2,('[py] got code: %s consts=%d names=%d\n'%(c.co_name,len(c.co_consts),len(c.co_names))).encode())\n"
    "open(r'/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/oracle/their_opmap.json','w').write(json.dumps(opcode.opmap))\n"
    "os.write(2,b'[py] wrote opmap\n')\n";
  int rc=PyRun_SimpleString(code);
  fprintf(stderr,"[c] PyRun rc=%d\n", rc);
  if(Py_FinalizeEx()<0) rc=120;
  return rc;
}
