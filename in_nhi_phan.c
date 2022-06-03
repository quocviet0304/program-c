#include <stdio.h>
void doi_nhi_phan(int number)
{
	int i,dem=0;
	int a[100];
	do{
		a[dem++] = number%2;
		number /= 2;
	}while(number);
	
	for(i = dem-1 ; i>=0; i--)
		printf("%d ", a[i]);	
}
void in (int a,int b)
{
	for(int i = a; i <=b; i++)
	{
		printf("%d: ", i);
		doi_nhi_phan(i);
		printf("\n");
	}
	
}
int main()
{
	int a,b;
	scanf("%d %d", &a,&b);
	if(a<b)
		in(a,b);
	else
		in(b,a);
	
	return 0;
}
