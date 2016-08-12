for x = 1 to 100 do
    if x mod 15 = 0 then 
        print_endline "FizzBuzz"
    else if x mod 3 = 0 then 
        print_endline "Fizz"
    else if x mod 5 = 0 then
        print_endline "Buzz"
    else
        print_endline (string_of_int x)
done;;
