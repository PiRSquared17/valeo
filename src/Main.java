public class Main {

    private static Double saldo;

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public static Double getSaldo() {
        return saldo;
    }

    public static void main(String[] args) {
        int i;
        for (i = 1; i <= 5; i++ ) {
            System.out.println(getSaldo() + i);
        }
    }
}
