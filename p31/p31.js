const coins = {
  _1: 1,
  _2: 2,
  _5: 5,
  _10: 10,
  _20: 20,
  _50: 50,
  _100: 100,
  _200: 200
}

let answer = 0
let combo = ""

const makeChange = (total, str, start) => {
  switch (true) {
    case (total === 0):
      answer += 1
      // next line will print every combo :(
      // console.log(`${answer} ${str}`)
      break
    case (total >= coins._200 && start >= coins._200):
      makeChange(total - coins._200, str + "_200", coins._200)
    case (total >= coins._100 && start >= coins._100):
      makeChange(total - coins._100, str + "_100", coins._100)
    case (total >= coins._50 && start >= coins._50):
      makeChange(total - coins._50, str + "_50", coins._50)
    case (total >= coins._20 && start >= coins._20):
      makeChange(total - coins._20, str + "_20", coins._20)
    case (total >= coins._10 && start >= coins._10):
      makeChange(total - coins._10, str + "_10", coins._10)
    case (total >= coins._5 && start >= coins._5):
      makeChange(total - coins._5, str + "_5", coins._5)
    case (total >= coins._2 && start >= coins._2):
      makeChange(total - coins._2, str + "_2", coins._2)
    case (total >= coins._1 && start >= coins._1):
      makeChange(total - coins._1, str + "_1", coins._1)
  }
}

makeChange(200, combo, 200)

console.log(answer)
