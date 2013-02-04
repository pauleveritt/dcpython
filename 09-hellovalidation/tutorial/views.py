import colander
import deform
from pyramid.decorator import reify
from pyramid.view import view_config, view_defaults

class Person(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    age = colander.SchemaNode(colander.Integer(),
                              validator=colander.Range(0, 200))

@view_defaults(route_name='hello',
               renderer='templates/helloworld.pt')
class HelloWorld(object):
    title = 'Hello World'
    status_message = None

    def __init__(self, request):
        self.request = request

    @reify
    def form(self):
        schema = Person()
        return deform.Form(schema, buttons=('submit',))

    @reify
    def reqts(self):
        reqts = self.form.get_widget_resources()
        return dict(
            js_links=reqts.get('js', []),
            css_links=reqts.get('css', [])
        )

    @view_config()
    def hello_world(self):

        return dict(form=self.form)

    @view_config(request_param='submit')
    def submit_handler(self):
        form = self.form
        controls = self.request.POST.items()

        try:
            appstruct = form.validate(controls)
        except deform.ValidationFailure as e:
            return dict(form=e)

        ## Process the valid form data
        self.status_message = 'Added person: ' + appstruct['name']

        return dict(form=form, appstruct=appstruct)