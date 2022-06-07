from livereload import Server, shell
import os

server = Server()

# run a shell command
server.watch(os.getcwd())

# run a function
def alert():
    print('foo')
server.watch('foo.txt', alert)

server.watch('index.html', shell('make html', cwd='docs'))


server.serve()
