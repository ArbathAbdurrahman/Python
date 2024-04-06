package abstraction;

class Arbath1{
    public void display1(){
       System.out.println("display1 method");
    }
 }
 abstract class Arbath2{
    public void display2(){
       System.out.println("display2 method");
    }
 }
 abstract class Arbath3 extends Arbath1{
    abstract void display3();
 }
 class Arbath4 extends Arbath3{
    public void display3(){
       System.out.println("Arbath abstract display3 method");
    }
 }
 class Demo{
    public static void main(String args[]){
        Arbath4 obj=new Arbath4();
        obj.display3();
    }
 }