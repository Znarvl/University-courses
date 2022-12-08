#3.1.1

#Fråga 1
N1 <- rnorm(100, mean = 10, sd = 4)
hist(N1, probability = TRUE)
xfit <- seq(0, 20, 1)   
yfit <- dnorm(xfit, mean=10 , sd = 4) 
lines(xfit, yfit, col="blue", lwd=2) 

N2 <- rnorm(n = 10000, mean = 10, sd = 4)
hist(N2, probability = TRUE)
xfit <- seq(-5, 25, 1)   
yfit <- dnorm(xfit, mean= 10, sd = 4) 
lines(xfit, yfit, col="blue", lwd=2) 

#Fråga 2
#Skillanden är då att den ena har en sample på 100 dragningar medans den andra har på 10000
#Detta gör då den med 10 har slumpen mer roll jämfört med 10000 dragningar där 
# Normalfördellingen följer bättre "bellcurve"



#3.1.2 

## Bernoulli
X.1 <- rbinom(n = 10000, size = 1, prob= 0.2)
hist(X.1, probability = TRUE)
xfit <- seq(0, 1, 1)   
yfit <- dbinom(xfit, size= 1, prob= 0.2) 
lines(xfit, yfit, col="blue", lwd=2) 


## Binomial X2

X.2 <- rbinom(n = 10000, size = 20 , prob = 0.1)
hist(X.2, probability = TRUE) 
xfit <- seq(0, 10, 1)   
yfit <- dbinom(xfit, size = 20, prob = 0.1) 
lines(xfit, yfit, col="blue", lwd=2) 



## Binomial X3

X.3 <- rbinom(n = 10000, size = 20 , prob = 0.5)
hist(X.3, probability = TRUE) 
xfit <- seq(0, 18, 1)   
yfit <- dbinom(xfit, size = 20, prob = 0.5) 
lines(xfit, yfit, col="blue", lwd=2) 

## Geometrisk 
X.4 <- rgeom(n = 10000, prob = 0.1)
hist(X.4 , probability = TRUE) 
xfit <- seq(0, 60, 1)   
yfit <- dgeom(xfit, prob = 0.1) 
lines(xfit, yfit, col="blue", lwd=2) 

## Poisson

X.5 <- rpois(n = 100000, lambda = 10)
hist(X.5 , probability = TRUE)
xfit <- seq(0, 24,1)
yfit <- dpois(xfit, lambda = 10)
lines(xfit, yfit, col="blue", lwd=2) 

## Likformingt = Uniform
Y.1 <- runif(n = 10000, min = 0, max = 1)
hist(Y.1, probability = TRUE)
xfit <- seq(0, 1, 1)
yfit <- dunif(xfit, min = 0, max = 1)
lines(xfit, yfit, col="blue", lwd=2) 


## EXP
Y.2 <- rexp(n = 10000, rate = 3)
hist(Y.2, probability = TRUE)
xfit <- seq(0,2,1)
yfit <- dexp(xfit, rate = 3)
lines(xfit, yfit, col="blue", lwd=2) 

## Gamma
Y.3 = rgamma(n = 10000, shape = 2, scale = 1)
hist(Y.3, probability = TRUE)
xfit <- seq(0,13,1)
yfit <- dgamma(xfit, shape = 2, scale= 1)
lines(xfit, yfit, col="blue", lwd=2) 

##Student-t
Y.4 = rt(n = 10000, df = 3, ncp = 0)
hist(Y.4, probability = TRUE)
xfit <- seq(-10,10,1)
yfit <- dt(xfit, df = 3, ncp = 0)
lines(xfit, yfit, col="blue", lwd=2)

## BETA Y5 KONSTIG
Y.5 <- rbeta(n = 10000, shape1 = 0.1, shape2 = 0.1, ncp = 0)
hist(Y.5, probability = TRUE)
xfit <- seq(0,1,1)
yfit <- dbeta(xfit, shape1 = 0.1, shape2 = 0.1, ncp = 0)
lines(xfit, yfit, col="blue", lwd=2)

## BETA Y6
Y.6 <- rbeta(n = 10000, shape1 = 1, shape2 = 1, ncp = 0)
hist(Y.6, probability = TRUE)
xfit <- seq(0,1,1)
yfit <- dbeta(xfit, shape1 = 1, shape2 = 1, ncp = 0)
lines(xfit, yfit, col="blue", lwd=2)

## BETA Y7 KONSTIG
Y.7 <- rbeta(n = 10000, shape1 = 10, shape2 = 5, ncp = 0)
hist(Y.7, probability = TRUE)
xfit <- seq(0,1,1)
yfit <- dbeta(xfit, shape1 = 10, shape2 = 5, ncp = 0)
lines(xfit, yfit, col="blue", lwd=2)


##3.1.3

# 1

## Bionomal 
X <- rbinom(n = 10000, size = 1000, p = 0.001)
hist(X, probability = TRUE)
xfit <- seq(0,6,1)
yfit <- dbinom(xfit, size = 1000, p = 0.001)
lines(xfit, yfit, col="blue", lwd=2)

#2
#Biominal konvergerar mot poission 
#3
Y <- rpois(10000, 1)
hist(Y)


##Student t
Y <- rt(n = 10000, df = 1000, ncp = 0)
hist(Y, probability = TRUE)
xfit <- seq(-4,4,1)
yfit <- dt(xfit, df = 1000, ncp = 0)
lines(xfit, yfit, col="blue", lwd=2)

#2
## Konvergerar mot normal dist
#3

N <- rnorm(n=1000, mean = 0)
hist(N)

#3.1.4

X <- function(){
  return (rnorm(n = 10000, mean = 0, sd = 1))
}

Y <-function()
{
  return (rbinom(n=10000, size = 10, prob = 0.1))
}

#P(Y=y) med tathetfunktion
densityProb <- function(N){
  return (dbinom(x=N, size = 10, prob = 0.1))
}

#P(Y=N) random probabilitet
dist2 <- function(N){
  x=Y()
  return (sum(x/10000))
}
densityProb(0)
dist2(0)


#2 och 3

#P(X < 0)

pnorm(q= 0, mean = 0, sd = 1, lower.tail = TRUE , log.p = FALSE)

X <- X()
sum(X < 0) / 10000


#P( -1 < X < 1)
pnorm(q= 1 , mean = 0, sd = 1, lower.tail = TRUE , log.p = FALSE) - 
pnorm(q= -1, mean = 0, sd = 1, lower.tail = TRUE , log.p = FALSE)

X <- X()
sum((X > -1) & (X < 1)) / 10000


#P(1.96 < X)
pnorm(q = 1.96, mean = 0, sd = 1, lower.tail = FALSE, log.p = FALSE)

X <- X()
sum(X > 1.96) / 10000

#P(0<Y<10)

pbinom(0, size = 10,p= 0.1, lower.tail = FALSE) - pbinom(9, size = 10, p = 0.1, lower.tail = FALSE) 

Y <- Y()
sum((Y > 0) & (Y < 10)) / 10000


#P(Y = 0)
pbinom(0, size = 10, p=0.1, lower.tail = TRUE)
Y <- Y()

sum(Y==0) / 10000

#p(0=<Y<=10)
pbinom(10, size = 10,p= 0.1, lower.tail = TRUE) - pbinom(-1, size = 10, p = 0.1, lower.tail = TRUE) 

Y<-Y()
sum((Y >= 0) & (Y <= 10)) / 10000


#3.1.5

#1
#gamla systemet
sum(rbinom(n= 10000, size = 337, p = 0.1)) / 10000

#nya systemet
P <-sum(runif(n = 10000, min = 0.02, max = 0.16))
sum(rbinom(n = 10000, size = 337, p = P)) / 10000

# Uppgift 3.2.1
# Del 1

X <- function(S){
  return (mean(rbinom(n=10, size=S, prob=0.2)))
}

Y <- function(S){
  return (mean(rgamma(n=S, shape=0.2, scale=0.2)))
}


X(10000) # = 2001.7, stämmer ganska väl överens med E(X) = size*prob = 10000*0.2
Y(10000) # = 0.0395, stämmer ganska väl överens med E(Y) = α*β = 0.2*0.2


# Del 2
vector.list <- c(10, 20, 30 ,40, 50,60,70,80,90,100,200,300,400,500,600,700,800,900
          ,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000)


vectorizedMeanX <- Vectorize(X)
vectorizedMeanY <- Vectorize(Y)
vectorMeanX <- vectorizedMeanX(vector.list)
vectorMeanY <- vectorizedMeanY(vector.list)
plot(vectorMeanX, type='l')
plot(vectorMeanY, type='l')


#3.3.1
#question 1
E[X] = 1 / rate = 1 / 10 = 0.1
Var[X] = 1 /rate^2 = 1 / 100 = 0.01
E[Y] = Var[Y] = lambda = 3 

#Question 2

X <- rexp(n= 10000, rate = 10)
mean(X)
var(X)

Y= rpois(n=10000, lambda = 3)
mean(Y)
var(Y)


# Question 3
E(3) = 3
E(3*X+2) = 3E(X) + 2 = 3*0.1+2 = 0.3 + 2 = 2.3
E(X + Y) = E(X) + E(Y) = 3 + 0.1 = 3.1
E(X*Y) = E(X) * E(Y) = 0.1 * 3 = 0.3
E(3*X+2*Y-3) = 3E(X) + 2E(Y) - 3 = 3*0.3 + 2*3 -3 = 3.3
Var(2*X-5) = 2^2Var(X) = 4*0.01 = 0.04
Var(X+Y) = Var(X) + Var(Y) = 0.01 + 3 = 3.01

#Question 4
X <- rexp(n = 10000, rate = 10)
Y <- rpois(n= 10000, lambda = 3)
mean(3)
mean(3*X+2)
mean(X+Y)
mean(3 * X + 2 * Y - 3)
var(2*X-5)
var(X+Y)


#3.4.1
#Question 1
X<-rpois(n= 1000, lambda = 5)
Y<- rexp(n= 1000, rate = 1)
Z<-rbinom(n= 1000, size = 10, p=0.01)

hist(X)
hist(Y)
hist(Z)
#Question 2
AverageX<- vector()
AverageY <-vector()
X<-rpois(n= 1000, lambda = 5)
for (i in 1:1000){
  median <- sum(rpois(n= 10, lambda = 5))/ 10
  AverageX <- append(AverageX, median)
}
hist(AverageX)

for (i in 1:1000){
  median <- sum(rexp(n= 10, rate = 5))/ 10
  AverageX <- append(AverageY, median)
}
hist(AverageY)

#Question 3
###
#X 
###
AverageX30 <- vector()
for (i in 1:1000){
  median <- sum(rpois(n= 30, lambda = 5))/ 30
  AverageX30 <- append(AverageX30, median)
}
hist(AverageX30)

AverageX100 <- vector()
for (i in 1:1000){
  median <- sum(rpois(n= 100, lambda = 5))/ 100
  AverageX100 <- append(AverageX100, median)
}
hist(AverageX100)

AverageX1000 <- vector()
for (i in 1:1000){
  median <- sum(rpois(n= 1000, lambda = 5))/ 1000
  AverageX1000 <- append(AverageX1000, median)
}
hist(AverageX1000)
####
#Y##
####
AverageY30 <- vector()
for (i in 1:1000){
  median <- sum(rexp(n= 30, rate = 5))/ 30
  AverageY30 <- append(AverageY30, median)
}
hist(AverageY30)

AverageY100 <- vector()
for (i in 1:1000){
  median <- sum(rexp(n= 100, rate = 5))/ 100
  AverageY100 <- append(AverageY100, median)
}
hist(AverageY100)

AverageY1000 <- vector()
for (i in 1:1000){
  median <- sum(rexp(n= 1000, rate = 5))/ 1000
  AverageY1000 <- append(AverageY1000, median)
}
hist(AverageY1000)

####
#Z##
####
AverageZ30 <- vector()
for (i in 1:1000){
  median <- sum(rbinom(n= 30, size = 10, prob = 0.01))/ 30
  AverageZ30 <- append(AverageZ30, median)
}
hist(AverageZ30)

AverageZ100 <- vector()
for (i in 1:1000){
  median <- sum(rbinom(n= 100, size = 10, prob = 0.01))/ 100
  AverageZ100 <- append(AverageZ100, median)
}
hist(AverageZ100)

AverageZ1000 <- vector()
for (i in 1:1000){
  median <- sum(rbinom(n= 1000, size = 10, prob = 0.01))/ 1000
  AverageZ1000 <- append(AverageZ1000, median)
}
hist(AverageZ1000)

# Vi på historiegramen för X,Y och Z att de konvergerar mot normalfördelning 
#
# Utifrån vad vi ser på graferna så ser det ut som att Z går snabbast mot 
# normalförderlningen.


