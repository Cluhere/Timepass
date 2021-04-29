#include <stdio.h>
int main()
{
    int hrs,mins,ch,nmins,nhrs, a, Nhrs;
    printf("Enter your Time in hrs: ");
    scanf("%d",&hrs);
    printf("Enter your Time in mins: ");
    scanf("%d",&mins);

    printf("Type 1 to know Japan Time \n");
    printf("Type 2 to know London Time \n");
    printf("Type 3 to know Sydney Time \n");
    printf("Type 4 to know Beijing Time \n");
    printf("Type 5 to know New York Time \n");

    scanf("%d", &a);

    switch (a) {

    case 1: 
    {
        if (hrs<=24 && hrs>=0 && mins>=0 && mins<=60)
        {
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
        else 
        {
          printf("invalid input");
        }
    break;
    }
    case 2: 
    {
        if (hrs<=24 && hrs>=0 && mins>=0 && mins<=60)
        {
            nmins=mins+30;
            if(nmins>=0)
            {
                nmins=nmins-60;
                nhrs=hrs-5;
                if(nhrs<0)
                {
                    nhrs=24+nhrs;
                    printf("IST to BST(Time yesterday): %d:%d",nhrs,nmins);
                }
                else
                {
                    printf("IST to BST: %d:%d",nhrs,nmins);
                }
            }
            else
            {
                nhrs=hrs-4;
                if(nhrs<0)
              {
                nhrs=24+nhrs;
                printf("IST to JST(Time next day): %d:%d",nhrs,nmins);
               }
                else
                 {
                 printf("IST to JST: %d:%d",nhrs,nmins);
                }
            }
        }
        else 
        {
          printf("invalid input");
        }
    break;
    }
   
    }
}
