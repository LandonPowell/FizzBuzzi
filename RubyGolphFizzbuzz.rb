for x in 1..100
    puts (x%3==0 ? "Fizz":"")+(x%5==0 ? "Buzz":(x%3!=0 ? String(x) :""))
end
