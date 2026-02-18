class CompoundInterest{
    public static void main(String args[])
    {
        double principal = 10000, rate = 5, time = 2;
        double A = principal *
                    (Math.pow((1 + rate / 100), time));
          double CI = A - principal;
        
        System.out.println("Compound Interest is "+ CI);
    }
}
