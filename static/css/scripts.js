function toggle(item) {
    let url = item.data('url'),
        heart = item.find('.bi');
    $.get(
        `${location.origin}/${url}`
    ).done(function (data) {
        let count = heart.text();
        if (data.favorite === true) {
            heart.addClass('bi-heart-fill').removeClass('bi-heart');
            heart.text(++count);
        } else {
            heart.addClass('bi-heart').removeClass('bi-heart-fill');
            heart.text(--count);
        }
    }).fail(function (error) {
        console.log(error)
    })
}