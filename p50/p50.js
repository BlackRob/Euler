import { primes as _primes } from "./genPrimes.js"

// wrote this so you must include the max number as an argument
let maxPrime = process.argv[2]
if (process.argv[2] == null) {
  console.log("You forgot the argument, using 100")
  maxPrime = 100
}

// we need an array of primes to work with
const primes = _primes(maxPrime)

// binary search of sorted array; 
// just returns true or false if item is found
const bsFound = (aSortedArray, aNumber) => {
  let foundIt = false
  let min = 0
  let max = aSortedArray.length - 1
  let midPoint = Math.floor(aSortedArray.length / 2)

  do {
    if (aSortedArray[midPoint] < aNumber) {
      min = midPoint
      midPoint = midPoint + Math.floor((max - midPoint) / 2)
    } else if (aSortedArray[midPoint] > aNumber) {
      max = midPoint
      midPoint = midPoint - Math.floor((midPoint - min) / 2)
    } else {
      foundIt = true
    }
  } while (foundIt === false && midPoint !== min && midPoint !== max)

  return foundIt
}

console.log(primes)

const mp = primes[primes.length - 1]
let longestSequence = 0
let longestSequenceNum = 0
let tempSum = primes[0]

for (let i = 0; i <= primes[primes.length - 1]; i++) {
  tempSum = primes[i]
  for (let j = i + 1; tempSum <= primes[primes.length - 1]; j++) {
    tempSum = tempSum + primes[j]
    if (bsFound(primes, tempSum) && (j - i + 1) >= longestSequence) {
      longestSequenceNum = tempSum
      longestSequence = j - i + 1
      console.log(`i = ${i}, j = ${j}, ${tempSum}, ${longestSequence}`)
    }
  }
}
