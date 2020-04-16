const header = $('h1')
const headerCSS = {
    background: "green",
    color: "white",
    border: "20px solid red"
}
header.css(headerCSS)


const listItems = $('li')
const item1CSS = {
    color: "red"
}
const itemLastCSS = {
    color: "blue"
}
listItems.eq(0).css(item1CSS)
listItems.eq(-1).css(itemLastCSS)


const pStatus = $('#status')
pStatus.text("This is awesome")


const pTest = $('#test')
pTest.html('<em>This is crazy baby..</em>')


const submit = $('#submit')
submit.attr('type', 'reset')
submit.val('Reset')


const text = $('#text')
text.val('this is text box')
text.addClass('textFontRight')
text.removeClass('textFontLeft')




