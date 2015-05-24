/* Javascript for UcCodemirrorXBlock. */
function UcCodemirrorXBlock(runtime, element) {
    var getJsonDataHandlerUrl = runtime.handlerUrl(element, 'get_jsonData');
    var readFileHandlerUrl = runtime.handlerUrl(element, 'readFile');
    var file_path=""
    function gen_jstree(result) {
        $('#jstree', element).jstree({
            'core' : {
                'data' :result.jsonData
            },
            "themes" : {
                "theme" : "classic",
                "dots" : true,
                "icons" : true
            },
            "types":{
                "leaf" : {
                    "icon" : "jstree-file"
                }
            },
            "plugins" : [
                "themes","json_data", "ui","types","dnd"
            ]
        })
            .on('changed.jstree', function (e, data) {
                file_path=result.lab_path +data.instance.get_path(data.selected[0],"/",0);
                document.getElementById('choosenfilename').value=data.instance.get_node(data.selected[0]).text;
            });
    }

    function gen_codemirror(result){
        editor.setValue(result.fileData);
    }


    $('#selectLab', element).click(function(eventObject) {
        var input = document.getElementById("selectLab");
        var lab = input.options[input.selectedIndex].innerHTML;
        var lab_path="/edx/var/edxapp/staticfiles/ucore/0f28b5d49b3020afeecd95b4009adf4c/ucore_lab/labcodes/"+lab
        params={"lab_path":lab_path};
        $.ajax({
            type: "POST",
            url: getJsonDataHandlerUrl,
            data: JSON.stringify(params),
            success: gen_jstree
        });
    });

    $('#readfile_btn', element).click(function(eventObject) {
        params = {
            "file_path":file_path
        };
        $.ajax({
            type: "POST",
            url: readFileHandlerUrl,
            data: JSON.stringify(params),
            success: gen_codemirror
        });

    });



    $(function ($) {
        /* Here's where you'd do things on page load. */
        var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
            lineNumbers: true,
            styleActiveLine: true,
            matchBrackets: true,
            mode: "text/x-c++src",
            extraKeys: {"Ctrl-Space": "autocomplete",
                "F11": function(cm) {
                    cm.setOption("fullScreen", !cm.getOption("fullScreen"));
                },
                "Esc": function(cm) {
                    if (cm.getOption("fullScreen")) cm.setOption("fullScreen", false);
                }
            }
         });
    });
}


$('#selectTheme', element).click(function(eventObject) {
    var input = document.getElementById("selectTheme");
    var theme = input.options[input.selectedIndex].innerHTML;
    editor.setOption("theme", theme);
    var choice = document.location.search &&
    decodeURIComponent(document.location.search.slice(1));
    if (choice) {
         input.value = choice;
         editor.setOption("theme", choice);
    }
});


$('#OpenLocalFile_btn', element).click(function(eventObject) {
    var File_Name = document.getElementById("filename").files[0];
    if (File_Name) {
        var reader = new FileReader();

        reader.readAsText(File_Name,'UTF-8');
        reader.onload = function (e) {
            editor.setValue(e.target.result);


        };
    }
});