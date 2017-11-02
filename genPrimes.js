/* generates an array of prime numbers up to
  ( <= to ) the argument, then returns that array */
exports.primes = (upTo) => {
  let found = [2,3]
  for (let i = 5; i <= upTo; i += 2 ) {
    let r = Math.ceil(Math.sqrt(i))
    for (let j = 1; j < found.length; j++ ) {
      if (i % found[j] === 0) {
        break
      } else if (found[j] >= r) {
        found.push(i)
        break
      }
    }
  }
  return found
}