#include<stdio.h>
#include<string.h>
typedef struct
{
	char ten[30];
	int maSV;
	float diemT,diemTR,diemLTC;
	
}sv;
float dtb(sv x)
{
	return (x.diemT + x.diemTR + x.diemLTC)/3;
}
int main()
{
	int i,n,dem = 0;
	scanf("%d", &n);
	sv a[n];
	for(i=0;i<n;i++)
	{
		scanf("%s",a[i].ten);
		scanf("%d",&a[i].maSV);
		scanf("%f",&a[i].diemT);
		scanf("%f",&a[i].diemTR);
		scanf("%f",&a[i].diemLTC);
	}
	printf("Danh sach sinh vien dat hoc bong\n");
	for(i=0;i<n;i++)
		if(a[i].diemT>=5.5 && a[i].diemTR>=5.5 && a[i].diemLTC>=5.5 && dtb(a[i])>=7.0)
		{
			printf("%s ",a[i].ten);
			printf("%d ", a[i].maSV);
			printf("%.2f ", a[i].diemT);
			printf("%.2f ", a[i].diemTR);
			printf("%.2f ", a[i].diemLTC);
			printf("%.2f", dtb(a[i]));
			printf("\n");
			dem++;
		}
			
		
	printf("So sinh vien dat hoc bong: %d",dem);
}
	


