window.onload = function () {
    $('INPUT#btn_translate').on('click', function () {
        const languageCode = $('INPUT#language_code').val();
        $.get('https://fourtonfish.com/hellosalut/?lang=' + languageCode, function (data) {
            $('DIV#hello').text(data.hello);
        });
    });
};
