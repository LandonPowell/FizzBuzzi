program FizzBuzz

integer x
do x = 1, 100, 1
   if      ( modulo(x, 15) == 0 ) then
       print *, "FizzBuzz"
   else if ( modulo(x,  3) == 0 ) then
       print *, "Fizz"
   else if ( modulo(x,  5) == 0 ) then
       print *, "Buzz"
   else
       print *, x
   end if
end do

end program FizzBuzz 
