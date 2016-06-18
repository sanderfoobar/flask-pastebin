var paste_public = true;

function toggle_private(){
    if(paste_public) {
        $('#exposure').html('Private.');
        $('#exposure_text').html('Share the private access URL responsibly.');
        paste_public = false;
    } else {
        $('#exposure').html('Public.');
        $('#exposure_text').html('Anyone will be able to find and view this paste.');
        paste_public = true;
    }
}