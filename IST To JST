#include <stdio.h>
int main()
{
    int hrs,mins,ch,nmins,nhrs;
    printf("Enter your Time in hrs: ");
    scanf("%d",&hrs);
    printf("Enter your Time in mins: ");
    scanf("%d",&mins);

    nmins=mins+30;
    if(nmins>=60)
    {
        nmins=nmins-60;
        nhrs=hrs+4;
        if(nhrs>=24)
        {
            nhrs=nhrs-24;
            printf("IST to JST(Time next day): %d:%d",nhrs,nmins);
        }
        else
        {
            printf("IST to JST: %d:%d",nhrs,nmins);
        }
    }
    else
    {
        nhrs=hrs+3;
        if(nhrs>=24)
        {
            nhrs=nhrs-24;
            printf("IST to JST(Time next day): %d:%d",nhrs,nmins);
        }
        else
        {
            printf("IST to JST: %d:%d",nhrs,nmins);
        }
    }
}
