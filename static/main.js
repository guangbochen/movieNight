(function() {

    // assign movie title and youtbe trailer on modal open
    $('.card-link').click(function() {
        var movie_title = $(this).attr('data-name');
        var movie_trailer_link = $(this).attr('data-link');
        $('.modal-title').text(movie_title);
        $('#modal-movie-trailer').attr('src', movie_trailer_link);
        $('#movie-trailer-modal').modal();
    });

    // remove the yotube video link on close
    $('#movie-trailer-modal').on('hidden.bs.modal', function (e) {
        $('#modal-movie-trailer').attr('src', '');
    })
})();
