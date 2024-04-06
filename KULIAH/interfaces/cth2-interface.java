package interfaces;

//first interface
interface Arbath1{
    public void display1();
}
//second interface
interface Arbath2 {
    public void display2();
}
//This interface is extending both the above interfaces
interface Arbath3 extends Arbath1,Arbath2{
}
class Arbath4 implements Arbath3{
    public void display1(){
        System.out.println("Arbath interface display2 method");
    }
    public void display2(){
        System.out.println("display3 method");
    }
}
class Demo{
    public static void main(String args[]){
        Arbath4 obj=new Arbath4();
        obj.display1();
    }
}
