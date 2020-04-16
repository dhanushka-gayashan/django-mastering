const carInfo = {
    make: "Toyota",
    year: 2019,
    model: "Camry",
    getModel () {
        return this.model
    }
}

console.log(carInfo)
console.log(carInfo.make)
console.log(carInfo.year)
console.log(carInfo.model)

carInfo.year = 2020
console.log(carInfo.make)

console.log(carInfo.getModel())

for (let key in carInfo) {
    console.log(key + " - " + carInfo[key])
}
