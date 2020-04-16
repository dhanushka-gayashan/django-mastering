const students = []

let run = prompt("Would you like to start the roster web application? y/n")

while (run === 'y') {
    const operation = prompt("Please select and action: add, remove, display, or quit")

    if (operation === "add") {
        students.push(prompt("What name would you like to add?"))
    } else if (operation === "remove") {
        const index = students.indexOf(prompt("What name would you like to remove?"))
        if (index !== -1) {
            students.splice(index, 1)
        }
    } else if (operation === "display") {
        console.log(students)
    } else if (operation === "quit") {
        run = "n"
    } else {
        console.log("Requested option is invalid..")
    }
}

alert("Thanks for using Web App! Please refresh the page to start over")
