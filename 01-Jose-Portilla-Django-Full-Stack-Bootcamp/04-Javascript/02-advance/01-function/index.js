const hello = function () {
    console.log("Hello World")
}
hello()


const greet = function (name) {
    console.log("Hello " + name)
}
greet("Dhanushka")


const addNum = function(num1, num2) {
    console.log(num1 + num2)
}
addNum(10, 20)


const helloSomeone = function (name="Jill") {
    console.log("Hello " + name)
}
helloSomeone("Dhanushka")
helloSomeone()


const formal = function (name="Sam", title="Sir") {
    return title + " " + name
}
console.log(formal("Dhanushka", "Gayashan"))



