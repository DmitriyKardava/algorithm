import java.util.Arrays;
import java.util.Date;

public class heapSort {
    public static void main(String[] args) {
        int[] array = new int[10000000];
        for (int j = 0; j < array.length; j++) {
            array[j] = (int) (Math.random() * 10000);
        }
        Date startDate = new Date();
        heapSort.sort(array);
        Date endDate = new Date();
        System.out.println(endDate.getTime() - startDate.getTime());
    }

    public static void sort(int[] array) {
        int i;
        int temp;
        int size = array.length;
        for(i=size/2-1; i >= 0; i--) heapify(array, i, size-1);
        for(i=size-1; i > 0; i--) {
            temp=array[i]; array[i]=array[0]; array[0]=temp;
            heapify(array, 0, i-1);
        }
    }

    private static void heapify(int[] array, int k, int n) {
        int newEl;
        int child;
        newEl = array[k];
        while (k <= n/2) {
            child = 2*k;
            if( child < n && array[child] < array[child+1] )
                child++;
            if( newEl >= array[child] ) break;
            array[k] = array[child];
            k = child;
        }
        array[k] = newEl;
    }
}
