x = [1,2,3,4,5,6];
print(x[1]);
print(x[:]);
print(x[:2]);
print(x[2:]);
print(x[2:4]);
x[2]=100;
print(x);
y=[7,8,9];
print(x+y);
del(x[2]);
print(x);
z = x[:];
x[2]=300;
print(z);
z[1]=9;
print(x);
