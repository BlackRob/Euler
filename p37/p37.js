const gen = require("./genPrimes")

const primes = gen.primes(1000000)

// we don't want the single-digit primes
const mt = primes.slice(4)

const leftTrunc = (numb) => {
  let lt = true;
  let numbStr = '' + numb
  while (numbStr.length >= 1) {
    if (!primes.includes(+numbStr)) {
      lt = false
      break
    }
    numbStr = numbStr.slice(1)
  }
  return lt
}

const rightTrunc = (numb) => {
  let rt = true;
  let numbStr = '' + numb
  while (numbStr.length >= 1) {
    if (!primes.includes(+numbStr)) {
      rt = false
      break
    }
    numbStr = numbStr.slice(0,-1)
  }
  return rt
}

let bitruncatable = []

mt.forEach( (numb) => {
  if (leftTrunc(numb) && rightTrunc(numb)) {
    console.log(numb)
    bitruncatable.push(numb)
  }
})

console.log(`bitruncatables found ${bitruncatable.length}`)

console.log(`sum ${bitruncatable.reduce( (sum, curr) => sum + curr) }`)