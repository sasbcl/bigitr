#
# Read configuration files for cvs/git synchronization
#

import config

ABORT = 0
WARN = 1
CONTINUE = 2
onerror = {
    'abort': ABORT,
    'warn': WARN,
    'continue': CONTINUE,
}


class AppConfig(config.Config):
    def __init__(self, configFileName):
        config.Config.__init__(self, configFileName, {
            'onerror': 'abort',
            'preimport': 'true'})

    def getGitDir(self):
        return self.get('global', 'gitdir')

    def getLogDir(self):
        return self.get('global', 'logdir')

    def getMailFrom(self):
        return self.get('global', 'mailfrom')

    def getSmartHost(self):
        return self.get('global', 'smarthost')

    def getImportError(self):
        return onerror[self.get('import', 'onerror')]

    def getImportCVSDir(self):
        return self.get('import', 'cvsdir')
    
    def getExportPreImport(self):
        return self.getboolean('export', 'preimport')

    def getExportError(self):
        return onerror[self.get('export', 'onerror')]

    def getExportCVSDir(self):
        return self.get('export', 'cvsdir')
