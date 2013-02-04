import colander
import deform
from pyramid.view import view_config

class Person(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    age = colander.SchemaNode(colander.Integer(),
                              validator=colander.Range(0, 200))

class HelloWorld(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='hello',
                 renderer='templates/helloworld.pt')
    def hello_world(self):
        schema = Person()
        form = deform.Form(schema, buttons=('submit',))

        return dict(title='Hello World', form=form,
                    reqts=form.get_widget_resources())

