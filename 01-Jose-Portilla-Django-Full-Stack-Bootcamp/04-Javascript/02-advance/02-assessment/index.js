const sleepIn = function (weekday, vacation) {
    return !weekday || vacation
}

console.log(sleepIn(false, false))
console.log(sleepIn(true, false))
console.log(sleepIn(false, true))


const monkeyTrouble = function (aSmile, bSmile) {
    return (aSmile && bSmile) || (!aSmile && !bSmile)
}

console.log(monkeyTrouble(true, true))
console.log(monkeyTrouble(false, false))
console.log(monkeyTrouble(true, false))


const stringTimes = function (str, n) {
    result = ""
    for (i = 0; i < n; i++) {
        result = result + str
    }
    return result
}

console.log(stringTimes("Hi", 2))


const luckySum = function (a, b, c) {
    if (a === 13) {
        return 0
    } else if (b === 13) {
        return a
    } else if (c === 13) {
        return a + b
    } else {
        return a + b + c
    }
}

console.log(luckySum(1, 2, 3))
console.log(luckySum(1, 2, 13))
console.log(luckySum(1, 13, 3))


const caught_speeding = function (speed, is_birthday) {
    if (is_birthday) {
        speed -= 5
    }

    if (speed >= 81) {
        return 2
    } else if (speed >= 61) {
        return  1
    } else {
        return  0
    }
}

console.log(caught_speeding(60, false))
console.log(caught_speeding(65, false))
console.log(caught_speeding(65, true))


const makeBricks = function (small, big, goal) {
    need_small = goal % 5 >= 0
    enought_small = ((goal % 5) - small) <= 0
    enought_bricks = ((big * 5) + small) >= goal
    return need_small && enought_small && enought_bricks
}

console.log(makeBricks(3, 1, 8))
console.log(makeBricks(3, 1, 9))
console.log(makeBricks(3, 2, 10))
