const employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31,
    nameLength() {
        console.log(this.name.length)
    },
    report() {
        console.log("Name is " + this.name + ", Job is " + this.job + ", Age is " + this.age)
    },
    lastName() {
        console.log(this.name.split(' ')[1])
    }
}

employee.nameLength()

employee.report()

employee.lastName()
