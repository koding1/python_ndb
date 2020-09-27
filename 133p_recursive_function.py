def factorial_recursive_function(i):
  # 종료조건 -> i 가 1 일 때
  if i == 1:
    return 1

  # n! = n * (n-1) 을 코드로 표현
  return i * factorial_recursive_function(i-1)

# 5! 계산
print(factorial_recursive_function(5))
