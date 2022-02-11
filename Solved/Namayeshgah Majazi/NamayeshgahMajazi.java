import java.util.Scanner;

/*
Question title = namayeshgah majazi - نمایشگاه مجازی
https://quera.ir/problemset/110015/
 */

public class NamayeshgahMajazi {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int count = Integer.parseInt(sc.nextLine().trim());

        //number of booth
        int num = 1;

        int remainingBooth = count;
        for (int i = 1; i <= 4; i++) {
            System.out.println("########.......########");
            switch (count) {
                case 1: {
                    System.out.println("#ghorfe" + num + "..............#");
                    remainingBooth--;
                    break;
                }
                case 0: {
                    System.out.println("#.....................#");
                    break;
                }
                default: {
                    System.out.println("#ghorfe" + num + ".......ghorfe" + (1 + num) + "#");
                    remainingBooth -= 2;
                    num += 2;
                    break;
                }
            }
            count = remainingBooth;
        }
        System.out.println("#######################");
    }
}