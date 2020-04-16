$('h1').click((event) => {
    event.target.textContent = "You click on me babe..."
})

$('#text').keypress((event) => {
    $('h1').toggleClass('text-font-right')
})

$('#submit').on('click', (event) => {
    $('.container').slideUp(5000)
})

