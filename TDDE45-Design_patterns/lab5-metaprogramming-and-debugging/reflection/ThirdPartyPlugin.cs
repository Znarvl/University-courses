using System;
using pizzainterfaces;

namespace thirdparty
{
    public class HawaiiPizza : pizzainterfaces.IPizza
    {
        string IPizza.Description()
        {
            return "A ham and pineapple pizza";
        }
    }
    public class HamPizza : pizzainterfaces.IPizza
    {
        string IPizza.Description()
        {
            return "A ham pizza";
        }
    }
}
