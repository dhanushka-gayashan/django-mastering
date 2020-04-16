const myHeader = document.querySelector("h1")

const getRandomColor = () => {
    const letters = "0123456789ABCDEF"
    let color = "#"
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)]
    }
    return color
}

const changeHeaderColor = () => myHeader.style.color = getRandomColor()

setInterval("changeHeaderColor()", 500)
