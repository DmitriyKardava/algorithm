import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class simpleNumbers {
    public static void main(String[] args){
        Date startDate = new Date();
        findSimpleNumbers(100000);
        Date endDate = new Date();
        System.out.println(endDate.getTime() - startDate.getTime());
        startDate = new Date();
        findSimpleNumbers2(100000);
        endDate = new Date();
        System.out.println(endDate.getTime() - startDate.getTime());
    }
    public static List<Integer> findSimpleNumbers(int lastNumber) {
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= lastNumber; i++) {
            boolean simple = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    simple = false;
                    break;
                }
            }
            if (simple) {
                result.add(i);
            }
        }
        return result;
    }
    public static List<Integer> findSimpleNumbers2(int lastNumber) {
        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(2);
        for (int i = 3; i <= lastNumber; i+=2) {
            boolean simple = true;
            for (int j = 3; j < result.size(); j++) {
                if (j * j > i) {break;}
                if (i % j == 0) {
                    simple = false;
                    break;
                }
            }
            if (simple) {
                result.add(i);
            }
        }
        return result;
    }
}

