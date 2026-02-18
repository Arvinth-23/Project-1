class Parameter{
    public void add(){
        int a= 10;
        int b= 45;
        int c=97;
        System.out.println("Addition:"+(a+b+c));
    }
    public static void main(String[]args){
        int a= 10;
        int b= 45;
        int c=97;
        
        System.out.println("Multipication:"+(a*b*c));
        if ( a>b&& a>c){
            System.out.println("A is Greater than B and C");
        }
        else {
            System.out.println("B and C Are Greater than A");
        
        }
        Parameter obj = new Parameter() ;
        obj.add();
    }
}