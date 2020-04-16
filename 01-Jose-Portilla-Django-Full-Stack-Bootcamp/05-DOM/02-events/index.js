const header = document.querySelector("h1")

header.addEventListener('click', () => {
    alert("You click on header....")
})

header.addEventListener('mouseover', () => {
    header.style.color = 'red'
})

header.addEventListener('mouseleave', () => {
    header.style.color = 'black'
})
