from meinheld import patch

patch.patch_all()

from meinheld import server

from bottle import Bottle


myapp = Bottle()


@myapp.route('/')
def helloworld():
    return 'helloworld'
