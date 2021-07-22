$(document).ready(function () {
    //Input boxes wrapper ID
    var inputs_Wrapper_id = $("#InputsWrapper");
    //Add, removed, submit button ID
    var add_button_id = $("#AddMoreSection");
    var removed_button_id = $("#removeButton");
    var submit_button_id = $("#submit");

    //-----need to define variables: count, url, form_id-----------

    //Add a section when added button click
    $(add_button_id).click(function () {

        count++;
        var subtitle_id = 'blog_subtitle_' + count;
        var content_id = 'blog_content_' + count;
        //add section
        $(inputs_Wrapper_id).append(
            '<div> \
                <hr>\
                <div class="mb-3">\
                    <label for="'+ subtitle_id + '" class="form-label">Subtitle#' + count + ' (required)</label>\
                    <input type="text" id="'+ subtitle_id + '" name="blog_subtitles" placeholder="Post Subtitle" class="form-control"\
                        required>\
                </div>\
                <div class="mb-3">\
                    <label for="'+ content_id + '" class="form-label">Content#' + count + '</label>\
                    <textarea name="blog_contents" id="'+ content_id + '" placeholder="Post content" class="form-control"\
                        rows="10"></textarea>\
                </div>\
            </div>');
    });

    //Remove the last section when removed button click
    $(removed_button_id).on('click', function () {
        if (count > 1) {
            //remove the last section
            $(this).closest('form').children('div').children('div')[count].remove();
            count--;
        }
        return false;
    })
    $(submit_button_id).click(function () {
        $.ajax({
            url: url,
            method: "POST",
            data: $(form_id).serialize(),
            success: function (data) {
                $(form_id)[0].reset();
            }
        });
    });
});