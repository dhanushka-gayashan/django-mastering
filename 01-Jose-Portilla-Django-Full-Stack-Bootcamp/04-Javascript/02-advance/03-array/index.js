const countries = ["USA", "SL", "NZ"]
console.log(countries[0])
console.log(countries[1])
console.log(countries[2])

countries[0] = "AUS"
countries[1] = "FRN"
countries[2] = "SWD"
console.log(countries[0])
console.log(countries[1])
console.log(countries[2])


const mix = ["Dhanu", 33, 5.9]
console.log(mix)
console.log(mix.length)


const multi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
console.log(multi)


const numbers = ["one", "two", "three"]
console.log(numbers)
console.log(numbers.length)

numbers.push("four")
numbers.push("five")

console.log(numbers)
console.log(numbers.length)

numbers.pop()

console.log(numbers)
console.log(numbers.length)


const letter = ['a', 'b', 'c', 'd', 'e']

for (let s in letter) {
    console.log(s)
}

for (let l of letter) {
    console.log(l)
}

letter.forEach((i) => console.log(i))
