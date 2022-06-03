#include<stdio.h>
int check(int n)
{
	if(n == 1 || n == 2)
		return 1;
	int a = 1, b = 1,kq ,i;
	for(i =3;i<=n;i++)
	{
		kq = a+b;
		a = b;
		b =kq;
	}
	return kq;
}
int Fibonacci(int n)
{
    if (n == 1 || n == 2)
        return 1;
    return Fibonacci(n - 1) + Fibonacci(n - 2);
}
int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i<=n;i++)
		printf("%d ", Fibonacci(i));
}
