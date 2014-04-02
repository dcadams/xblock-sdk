"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from django.templatetags.static import static

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment


class HelloWorldXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )
    
    studentIdList = []
    studentIdCount = []

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the HelloWorldXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/hello_world.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/hello_world.css"))
        frag.add_javascript(self.resource_string("static/js/src/raphael-min.js"))
        frag.add_javascript(self.resource_string("static/js/src/qwerty-hancock.js"))
        frag.add_javascript(self.resource_string("static/js/src/main.js"))
        frag.add_javascript(self.resource_string("static/js/src/hello_world.js"))
        frag.initialize_js('HelloWorldXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        studentId = data['student_id']
        userDict = {}
        
        for student in self.studentIdCount:
            if student['student_id'] == studentId:
                student['count'] += 1
        
        if studentId not in self.studentIdList:
            self.studentIdList.append(studentId)
            userDict['student_id'] = studentId
            userDict['count'] = 1
            
            self.studentIdCount.append(userDict)

        self.count += 1
        return {"count": self.count, "studentIdCount": self.studentIdCount}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Know Your Notes",
             """<vertical_demo>
                <hello_world/>
                </vertical_demo>
             """),
        ]

    