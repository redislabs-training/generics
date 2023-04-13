from cleo import Application

from generics.flush_namespace import FlushNamespace

def main():
    app = Application(name='Generic CLI', version='0.1.0')
    app.add(FlushNamespace())
    app.run()
    
    