import java.util.ArrayList;
import java.util.Scanner;

public class mypet {
    static String petName;
    static int happiness = 50;
    static int hunger = 50;
    static boolean isRunning = true;
    static ArrayList<String> actionHistory = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("✨ Welcome to MyPet!");
        System.out.print("Name your pet: ");
        petName = scanner.nextLine();
        System.out.println(petName + " is ready! (^_^)");

        while (isRunning) {
            showStatus();
            printMenu();

            String choice = scanner.nextLine();
            System.out.println("----------------------");

            switch (choice) {
                case "1":
                    feedPet();
                    break;
                case "2":
                    playWithPet();
                    actionHistory.add("[Played] with " + petName);
                    break;
                case "3":
                    endGame();
                    break;
                default:
                    System.out.println("Invalid choice!");
            }

            checkStatus();
        }

        scanner.close();
    }

    public static void feedPet() {
        if (hunger >= 30) {
            hunger -= 30;
        } else {
            hunger = 0;
        }

        for (int i = 0; i < 3; i++) {
            happiness += 3;
            if (happiness > 100) {
                happiness = 100;
                break;
            }
        }

        System.out.println(petName + " ate happily!");
        actionHistory.add("[Fed] " + petName);
    }

    public static void playWithPet() {
        happiness = Math.min(100, happiness + 25);
        hunger = Math.min(100, hunger + 20);
        System.out.println(petName + " had fun!");
    }

    static void endGame() {
        System.out.println("\n=== Game Over ===");
        System.out.println("Your action history:");

        for (int i = 0; i < actionHistory.size(); i++) {
            System.out.println((i + 1) + ". " + actionHistory.get(i));
        }

        System.out.println("\nFinal status:");
        showStatus();
        isRunning = false;
    }

    static void printMenu() {
        System.out.println("\n1. Feed 🍎");
        System.out.println("2. Play 🎾");
        System.out.println("3. Exit");
        System.out.print("Choose (1-3): ");
    }

    static void showStatus() {
        System.out.println("\n* " + petName + "'s Status *");
        System.out.println("Happiness: " + "🟩".repeat(happiness / 10) + " " + happiness + "%");
        System.out.println("Hunger:    " + "🍗".repeat(hunger / 10) + " " + hunger + "%");
    }

    static void checkStatus() {
        if (happiness <= 20) {
            System.out.println("\n⚠️ " + petName + " needs attention!");
        }
        if (hunger >= 80) {
            System.out.println("\n⚠️ " + petName + " is starving!");
        }
        if (happiness <= 0) {
            System.out.println("\n😢 " + petName + " left...");
            endGame();
        }
    }
}
