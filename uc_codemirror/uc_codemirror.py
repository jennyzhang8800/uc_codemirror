"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

from lib_util import Util
from path2json import  path2json
class UcCodemirrorXBlock(XBlock):
    """
    UcCodemirror XBlock
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    logger = Util .uc_logger()
    lab = String(default="",scope=Scope .user_state ,help="lab")
    file_path = String(default="",scope=Scope .user_state ,help="path")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the UcCodemirrorXBlock, shown to students
        when viewing courses.
        """

        fragment = Fragment()
        fragment.add_content(Util.load_resource("static/html/uc_codemirror.html"))
        fragment.add_css(Util.load_resource("static/css/uc_codemirror.css"))
        fragment.add_css(Util.load_resource("static/jstree/dist/themes/default/style.min.css"))
        fragment.add_javascript(Util.load_resource("static/js/src/uc_codemirror.js"))
        fragment.add_javascript(Util.load_resource("static/js/src/jquery.js"))
        fragment.add_javascript(Util.load_resource("static/js/src/jstree.min.js"))
        fragment.initialize_js('UcCodemirrorXBlock')
        return fragment

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler

    def get_jsonData(self, data, suffix=''):
        """
        把路径转化为json串.
        """
        self.logger.info("get_jsonData")
        Path2json=path2json()
        jsonData=Path2json.getJson(data["lab_path"])
        lab_path=data["lab_path"]
        return {"jsonData":jsonData,"lab_path":lab_path }

    @XBlock.json_handler

    def readFile(self, data, suffix=''):
        """
        读jstree中选定的文件.
        """
        self.logger.info("readFile")
        self.file_path = data["file_path"]
        output=open(data["file_path"],"r")
        fileData=output.read()
        output.close()
        return {"fileData":fileData}

    @XBlock.json_handler
    def save2local(self, data, suffix=''):
        """
        编辑框中修改后的内容保存回本地对应文件中
        """
        self.logger.info("save2local")
        output=open(self.file_path ,"w")
        output.write(data["newData"])
        output.close()

        return True

    def save2gitLab(self, data, suffix=''):
        """
        编辑框中修改后的内容保存到gitlab对应文件中
        self.file_path
        data["newData"]
        """
        pass

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("UcCodemirrorXBlock",
             """<vertical_demo>
                <uc_codemirror/>
                <uc_codemirror/>
                <uc_codemirror/>
                </vertical_demo>
             """),
        ]
