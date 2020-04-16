const tds = document.querySelectorAll('td')

tds.forEach((element) => {
    element.addEventListener('click', (event) => {
        const text = element.textContent.trim()
        if (text === '') {
            element.textContent = 'X'
        } else if (text === 'X') {
            element.textContent = 'O'
        } else {
            element.textContent = ''
        }
    })
})

document.querySelector('#restart').addEventListener('click', (event) => {
    tds.forEach((element) => element.textContent = '')
})
