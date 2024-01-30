using System;
namespace pizzainterfaces
{
    public interface IPizza
    {
        string Description();
    }
    public interface IPizzaMaker
    {
        IPizza CreatePizza();
    }
}
