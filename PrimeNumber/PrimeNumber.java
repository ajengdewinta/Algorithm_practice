import java.util.*;
import static java.lang.Math.sqrt;

public class PrimeNumber {

    /**
     * @param args the command line arguments
     */
    static boolean CheckPrime(int i, int num, int sqrtnum){
        
        if (num == 2)
            return true;
        
        else if(i<=sqrtnum){
            if(num %i ==0){
                return false;
            }
            else{
                i++;
                return CheckPrime(i, num, sqrtnum);
            }   
        }
        
        else
            return true;
    }
    
    static void PrimeNumber(int num){
        boolean flag=true;
        int x=2;
        for(int i=2; i<=num; i++ ){
            flag = CheckPrime(2,i,(int)sqrt(i));
            
            if(flag == true){
                System.out.print(i+ " ");
            }                 
        }
        System.out.println("");
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter any positive number: ");
        int num = sc.nextInt();
        PrimeNumber(num);
    }
    
}