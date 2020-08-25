program sin 
implicit none 
real :: x, sum_1 
integer(kind = 16) :: n, i , n_1, n_factorial

n=16
read (*,*) x 
n_factorial = 1 
sum_1=0 

DO i = 1, n 
n_factorial = (2*i)-1
    DO n_1=n_factorial-1, 1, -1
        if (n_1 == 1) then
            exit
        end if
        n_factorial=n_factorial*n_1
    END DO
    sum_1 = sum_1 + ( ((-1)**(i-1)) * (x**((2*i) - 1)) )/(n_factorial)
END DO 
write (*,*) sum_1 

end program sin
