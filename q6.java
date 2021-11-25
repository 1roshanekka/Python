import java.util.Scanner;

class q6
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int x = (a<b)? 1 : 0;;
        int y = (a>=b)? 1 : 0;;
        System.out.println((x*(a))+((y)*(a%b)));

    }
}
