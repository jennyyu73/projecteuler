#Euler 25: 1000th digit fibonacci number
var fib2 = _.memoize(function(n) {
  return n < 2 ? n : fib2(n - 1) + fib2(n - 2);
});

print(function(12))
