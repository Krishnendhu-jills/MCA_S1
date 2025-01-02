#include<stdio.h>
int a[3],i;
void main()
{
    printf("Enter 3 numbers: ");
    for(i=0;i<3;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Array elements: ");
    for(i=0;i<3;i++)
    {
        printf("%2d",a[i]);
    }

}
