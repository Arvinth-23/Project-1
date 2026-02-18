public class TemperatureConverter {
    public void temperature (){
       double celsius = 36;
       double fahrenheit = (celsius * 9/5)+ 32;
       double  kelvin = celsius + 273.15;
       System.out.println("Celsius: " + celsius);
       System.out.println("Fahrenheit: " + fahrenheit);
         System.out.println("Kelvin: " + kelvin);
            
    }
    public static void main(String[] args) {
        TemperatureConverter  temp = new TemperatureConverter ();
        temp.temperature();
      
    }
}
