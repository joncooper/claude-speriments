#include <Python.h>
#include <stdio.h>
static void chk(PyStatus s){ if(PyStatus_Exception(s)){ fprintf(stderr,"[init-fail]\n"); Py_ExitStatusException(s);} }
int main(int argc,char**argv){
  PyStatus st; PyConfig cfg; PyConfig_InitIsolatedConfig(&cfg);
  cfg.use_environment=1; cfg.site_import=0; cfg.pathconfig_warnings=0;
  chk(PyConfig_SetBytesString(&cfg,&cfg.home,"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905"));
  chk(PyConfig_SetBytesString(&cfg,&cfg.program_name,"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/dropbox"));
  cfg.module_search_paths_set=1;
  chk(PyWideStringList_Append(&cfg.module_search_paths, L"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/python-pypkg.zip"));
  chk(PyWideStringList_Append(&cfg.module_search_paths, L"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/python-pyext"));
  chk(Py_InitializeFromConfig(&cfg)); PyConfig_Clear(&cfg);
  fprintf(stderr,"[c] init OK\n");
  int rc=0;
  if(argc>1){
    char buf[4096];
    snprintf(buf,sizeof(buf),"exec(compile(open(r'%s','rb').read(),r'%s','exec'))",argv[1],argv[1]);
    rc=PyRun_SimpleString(buf);
  }
  fprintf(stderr,"[c] PyRun rc=%d\n",rc);
  if(Py_FinalizeEx()<0) rc=120;
  return rc;
}
