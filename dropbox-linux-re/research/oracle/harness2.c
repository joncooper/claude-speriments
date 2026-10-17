#include <Python.h>
#include <stdio.h>
#define CHK(s) do{ if(PyStatus_Exception(s)){ fprintf(stderr,"[harness] init failed at step\n"); Py_ExitStatusException(s);} }while(0)
int main(int argc, char** argv){
  PyStatus status; PyConfig config;
  PyConfig_InitIsolatedConfig(&config);
  config.use_environment = 0;
  config.site_import = 0;
  config.pathconfig_warnings = 0;
  status = PyConfig_SetBytesString(&config, &config.home, "/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905"); CHK(status);
  status = PyConfig_SetBytesString(&config, &config.program_name, "/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/dropbox"); CHK(status);
  config.module_search_paths_set = 1;
  status = PyWideStringList_Append(&config.module_search_paths, L"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/python-pypkg.zip"); CHK(status);
  status = PyWideStringList_Append(&config.module_search_paths, L"/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/python-pyext"); CHK(status);
  fprintf(stderr,"[harness] calling Py_InitializeFromConfig\n");
  status = Py_InitializeFromConfig(&config);
  CHK(status);
  PyConfig_Clear(&config);
  fprintf(stderr,"[harness] init OK\n");
  int rc=0;
  if(argc>1){ FILE* f=fopen(argv[1],"r"); if(f){ rc=PyRun_SimpleFile(f, argv[1]); fclose(f);} }
  if(Py_FinalizeEx()<0) rc=120;
  return rc;
}
