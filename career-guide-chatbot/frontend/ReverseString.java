class ReverseString{
    public static void main(String[] args){
        String s = "Geeks";
        StringBuilder res = new StringBuilder();
        res.append(s);
        res.reverse();
        System.out.println(res);
    }
}