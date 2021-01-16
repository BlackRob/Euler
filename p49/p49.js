import { primes as _primes } from "./genPrimes.js"


// we need an array of 4 digit primes to work with
// so we generate two arrays of primes, one 3 digits and less
// the other 4 digits and less, then remove the 3 digit one
// not the best way to do this, but the easiest
const threeDig = _primes(1000)
const fourDig = _primes(10000)
const primes = fourDig.slice((threeDig.length))

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

// check if three 4-digit numbers are permutations of each other
const permCheck = (a, b, c) => {
  let perms = false
  let a_ = Array.from(String(a)).sort().toString()
  let b_ = Array.from(String(b)).sort().toString()
  let c_ = Array.from(String(c)).sort().toString()

  if (a_ === b_ && a_ === c_) {
    perms = true
  }

  return perms
}


// our main loop
let gap = 0

for (let i = 0; i < primes.length - 3; i++) {
  for (let j = i + 1; j < primes.length - 2; j++) {
    gap = primes[j] - primes[i]
    if (bsFound(primes, primes[j] + gap)) {
      // now check if the numbers are all permutations
      if (permCheck(primes[i], primes[j], primes[j] + gap)) {
        console.log(`${primes[i]}, ${primes[j]}, ${primes[j] + gap}, ${gap}`)
      }
    }
  }
}
