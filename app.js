function showBooksByTags () {
    var tags = $(this).val().split(',');
    var cards = $('.card');
    if (tags.length > 0 && tags[0].length > 1) {
        cards.hide();
        tags.forEach(function (item) {
            $('.card.' + item).show();
        });
    }
    else {
        cards.show();
    }
    var totalVisible = $('.card:visible').length;
    $('#displaying').html(totalVisible);
}

$('#filters').change(showBooksByTags);