class Circle:
        def CalculateArea(self):
                print("enter radius")
                self.s=float(input())
                area=3.14*self.s*self.s
                print("Area of circle is=%f"%(area))
        def CalculatePerimeter(self):
                perimeter=2*3.14*self.s
                print("perimeter of circle is=%f"%(perimeter))
c=Circle()
c.CalculateArea()
c.CalculatePerimeter()
