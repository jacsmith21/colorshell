import sys

class out:
    shell = sys.stdout.shell

    @staticmethod
    def black(text='', end='\n'):
        out.shell.write(str(text)+end, 'SYNC')

    @staticmethod
    def red(text='', end='\n'):
        out.shell.write(str(text)+end, 'COMMENT')

    @staticmethod
    def green(text='', end='\n'):
        out.shell.write(str(text)+end, 'STRING')

    @staticmethod
    def blue(text='', end='\n'):
        out.shell.write(str(text)+end, 'stdout')

    @staticmethod
    def purple(text='', end='\n'):
        out.shell.write(str(text)+end, 'BUILTIN')

    @staticmethod
    def orange(text='', end='\n'):
        out.shell.write(str(text)+end, 'KEYWORD')

    @staticmethod
    def trace(text=''):
        out.black('TRACE: ' + text)
    
    @staticmethod
    def debug(text=''):
        out.purple('DEBUG: ' + text)
    
    @staticmethod
    def info(text=''):
        out.green('INFO: ' + text)

    @staticmethod
    def warning(text=''):
        out.shell.write('WARNING: ' + text + '\n', 'stderr')

    @staticmethod
    def error(text='', exeption=None):
        out.shell.write('ERROR: '+text+'\n', 'ERROR')
        if exception is not None:
            out.shell.write(str(exception), 'ERROR')
        
