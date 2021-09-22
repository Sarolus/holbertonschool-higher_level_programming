$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const languageCode = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + languageCode, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').on('keypress', function (key) {
    if (key.which === 13) {
      const languageCode = $('INPUT#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + languageCode, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
