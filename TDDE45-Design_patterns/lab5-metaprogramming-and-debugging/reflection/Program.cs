using System;
using System.Linq;
using System.Reflection;
using pizzainterfaces;

namespace testreflection
{
    class MexicanaPizza : pizzainterfaces.IPizza
    {
        string IPizza.Description()
        {
            return "Spicy pizza";
        }
    }
    class MexicanaPizzaMaker : pizzainterfaces.IPizzaMaker
    {
        IPizza IPizzaMaker.CreatePizza()
        {
            return new MexicanaPizza();
        }
    }
    class RandomPizzaMaker : pizzainterfaces.IPizzaMaker
    {
        static Random rnd = new Random();

        IPizza IPizzaMaker.CreatePizza()
        {
            // TODO: Your code goes here

            // Look through all loaded "assemblies" (the loaded .exe and .dll files)
            // for all classes that implement IPizza (and are concrete classes)

            // Choose one of classes implementing IPizza
            Assembly asm = Assembly.LoadFrom("ThirdPartyPlugin.dll");
            IPizza pizza;
            Random random = new Random();
            int rand = random.Next(0, 3);
            var curNamespaceTypes = Assembly.GetExecutingAssembly().GetTypes().ToList();
            var namespaceTypes = asm.GetTypes().ToList().Concat(curNamespaceTypes).ToList();
            pizza = (IPizza) Activator.CreateInstance(namespaceTypes[rand]);


            // Call the constructor of this class

            return pizza;

            //throw new NotImplementedException();
        }
    }
    class MainClass
    {
        public static void Main(string[] args)
        {
            // You may change this to an absolute path if you are not running it from the same location as the README suggests.
            // You can also comment out loading the dll (for example for testing the code first), but make sure to load the dll when
            // handing in the final result.
            Assembly a = Assembly.LoadFrom("ThirdPartyPlugin.dll");
            IPizzaMaker pm = new RandomPizzaMaker();
            foreach (int i in Enumerable.Range(1, 20)) {
                IPizza pizza = pm.CreatePizza();
                Console.WriteLine("{0} - {1}", pizza, pizza.Description());
            }
        }
    }
}
