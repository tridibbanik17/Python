def is_palindrome(s: str) -> bool:
  l, r = 0, len(s) - 1
  while l < r:
      while l < r and not is_alpha_numeric(s[l]):
          l += 1
      while l < r and not is_alpha_numeric(s[r]):
          r -= 1
      if s[l].lower() != s[r].lower():
          return False
      l += 1
      r -= 1
  return True

def is_alpha_numeric(c: str) -> bool:
    return (ord('A') <= ord(c) <= ord('Z') or 
    ord('a') <= ord(c) <= ord('z') or
    ord('0') <= ord(c) <= ord('9'))

print(is_palindrome("A man, a plan, a canal: Panama"))