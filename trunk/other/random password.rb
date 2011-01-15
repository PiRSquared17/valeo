def random_password(length=8)
  chars = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ23456789'
  Array.new(length) { chars[rand(chars.length)].chr }.join
end
print random_password()