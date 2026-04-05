def euler(x,dx,y,deriv,params):
    dy=deriv(x,y,params)
    return y+dx*dy
#Requires a deriv(t,y,params) function 
#to be defined beforehand according to the problem 