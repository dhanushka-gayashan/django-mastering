const names = prompt("Enter your full name: ").split(' ')
const age = parseInt(prompt("Enter your age: "))
const height = parseFloat(prompt("Enter your height: "))
const pet = prompt("Enter your pet's name: ")

const namesCondition = names[0][0] === names[1][0]
const ageCondition = age > 20 && age < 30
const heightCondition = height >= 170
const petCondition = pet[pet.length - 1] === 'y'

if (namesCondition && ageCondition && heightCondition && petCondition) {
    console.log("Access Granted....")
}



