/**
 * Created with PyCharm.
 * User: zhangyanni
 * Date: 15-5-24
 * Time: 下午3:53
 * To change this template use File | Settings | File Templates.
 */
function UcDockerXBlock(runtime, element) {
    var save2localHandlerUrl = runtime.handlerUrl(element, 'save2local');
    var save2gitLabHandlerUrl = runtime.handlerUrl(element, 'save2gitLab');

    function saveFileCallback(response) {
        alert("save successful!");
    }



    $('#saveFile_btn', element).click(function(eventObject) {
        params = {
            "newData": $("#code", element).val()
        };
        $.ajax({
            type: "POST",
            url:save2localHandlerUrl,
            data: JSON.stringify(params),
            success: saveFileCallback
        });

        $.ajax({
            type: "POST",
            url:save2gitLabHandlerUrl,
            data: JSON.stringify(params)

        });
    });
    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}