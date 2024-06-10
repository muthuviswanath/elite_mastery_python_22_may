import java.util.ArrayList;
public class LstComp{

    public static void main(String[] args){
        ArrayList<Integer> al = new ArrayList<>();
        for(int i=1; i<=10;i++){
            al.add(i*i);
        }

        System.out.println(al);
    }
}