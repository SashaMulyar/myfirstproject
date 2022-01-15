import abc
class Vehicle(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def transport(self):
        pass

    def start_engine(self):
        print('starting')
    
    def move(self):
        print('moving')
    
    def stop(self):
        print('stopping')

class Wheel_vehicle(Vehicle):
    def __init__(self, name, year, axis_count, wheel_count):
        self.__name = name
        self.__year = year
        self.__axis_count = axis_count
        self.__wheel_count = wheel_count
        
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    property = (get_name, set_name)

    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    property = (get_year, set_year)
    
    def get_axis_count(self):
        return self.__axis_count
    def set_axis_count(self, axis_count):
        self.__axis_count = axis_count  
    property = (get_axis_count, set_axis_count)  

    def get_wheel_count(self):
        return self.__wheel_count
    def set_wheel_count(self, wheel_count):
        self.__wheel_count = wheel_count  
    property = (get_wheel_count, set_wheel_count)

    def transport(self):
        print(f'{self.__name} with {self.__axis_count} axises and {self.__wheel_count} wheels was made in {self.__year}')
    
    
    
class Non_engine_ground_vehicle(Vehicle):
    def __init__(self, axis_count, wheel_count):
        self.__axis_count = axis_count
        self.__wheel_count = wheel_count
    
    def get_axis_count(self):
        return self.__axis_count
    def set_axis_count(self, axis_count):
        self.__axis_count = axis_count  
    property = (get_axis_count, set_axis_count)  

    def get_wheel_count(self):
        return self.__wheel_count
    def set_wheel_count(self, wheel_count):
        self.__wheel_count = wheel_count  
    property = (get_wheel_count, set_wheel_count)

    def transport(self):
        print(f'transport with {self.__axis_count} axises and {self.__wheel_count} wheels ')
    
    
class Water_vehicle(Vehicle):
    def __init__(self, name, year, displacement, engine_count):
        self.__name = name
        self.__year = year
        self.__displacement = displacement
        self.__engine_count = engine_count
        
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    property = (get_name, set_name)

    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    property = (get_year, set_year)
    
    def get_displacement(self):
        return self.__displacement
    def set_displacement(self, displacement):
        self.__displacement = displacement  
    property = (get_displacement, set_displacement)  

    def get_engine_count(self):
        return self.__engine_count
    def set_engine_count(self, engine_count):
        self.__engine_count = engine_count 
    property = (get_engine_count, set_engine_count)

    def transport(self):
        print(f'{self.__name} with {self.__displacement} displacement and {self.__engine_count} engine was made in {self.__year}')
    
    
class Rail_vehicle(Vehicle):
    def __init__(self, name, year, rails_width):
        self.__name = name
        self.__year = year
        self.__rails_width = rails_width
        
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    property = (get_name, set_name)

    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    property = (get_year, set_year)
    
    def get_rails_width(self):
        return self.__rails_width
    def set_rails_widtht(self, rails_width):
        self.__rails_width = rails_width  
    property = (get_rails_width, set_rails_widtht)  

    def transport(self):
        print(f'{self.__name} with {self.__rails_width}m rails width was made in {self.__year}')


class Air_vehicle(Vehicle):
    def __init__(self, name, year, altitude): 
        self.__name = name
        self.__year = year
        self.__altitude = altitude

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    property = (get_name, set_name)

    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    property = (get_year, set_year)
    
    def get_altitude(self):
        return self.__altitude
    def set_altitude(self, altitude):
        self.__altitude = altitude  
    property = (get_altitude, set_altitude)  

    def transport(self):
        print(f'{self.__name} with max altitude {self.__altitude}m was made in {self.__year}')

class Car(Wheel_vehicle):
    def __init__(self, model, door_count, body_type, colour): 
        self.__model = model
        self.__door_count = door_count
        self.__body_type = body_type
        self.__colour = colour

    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model
    property = (get_model, set_model)

    def get_door_count(self):
        return self.__door_count
    def set_door_count(self, door_count):
        self.__door_count = door_count
    property = (get_door_count, set_door_count)

    def get_body_type(self):
        return self.__body_type
    def set_body_type(self, body_type):
        self.__body_type = body_type  
    property = (get_body_type, set_body_type)
    
    def get_colour(self):
        return self.__colour
    def set_colour(self, colour):
        self.__colour = colour  
    property = (get_colour, set_colour)  

    def transport(self):
        print(f'{self.__colour} {self.__model} with {self.__door_count} doors {self.__body_type}')
    
    def start_engine(self):
        Wheel_vehicle.start_engine(self)
    def move(self):
        Wheel_vehicle.move(self)
    def stop(self):
        Wheel_vehicle.stop(self)

class Air_plane(Air_vehicle, Wheel_vehicle):
    def __init__(self, model, passengers_count): 
        self.__model = model
        self.__passengers_count = passengers_count
    
    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model
    property = (get_model, set_model)

    def get_passengers_count(self):
        return self.__passengers_count
    def set_passengers_count(self, passengers_count):
        self.__passengers_count = passengers_count
    property = (get_passengers_count, set_passengers_count)

    def transport(self):
        print(f'{self.__model} can transport {self.__passengers_count} passengers')

    def start_engine(self):
        Wheel_vehicle.start_engine(self)
    def move(self):
        Wheel_vehicle.move(self)
    def stop(self):
        Wheel_vehicle.stop(self)

class Jetski(Water_vehicle):
    def __init__(self, colour, model):
        self.__model = model
        self.__colour = colour
    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model
    property = (get_model, set_model)

    def get_colour(self):
        return self.__colour
    def set_colour(self, colour):
        self.__colour = colour
    property = (get_colour, set_colour)

    def transport(self):
        print(f'{self.__colour} Jetski {self.__model} ')
    
    def start_engine(self):
        Water_vehicle.start_engine(self)
    def move(self):
        Water_vehicle.move(self)
    def stop(self):
        Water_vehicle.stop(self)

class Cargo_train(Rail_vehicle):
    def __init__(self, model, locomotiveCount, cartsCount):
        self.__model = model
        self.__locomotiveCount = locomotiveCount
        self.__cartsCount = cartsCount

    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model
    property = (get_model, set_model)
    
    def get_locomotiveCount(self):
        return self.__locomotiveCount
    def set_locomotiveCount(self, locomotiveCount):
        self.__locomotiveCount = locomotiveCount
    property = (get_locomotiveCount, set_locomotiveCount)

    def get_cartsCount(self):
        return self.__cartsCount
    def set_cartsCount(self, cartsCount):
        self.__cartsCount = cartsCount
    property = (get_cartsCount, set_cartsCount)

    def transport(self):
        print(f'{self.__model} with {self.__locomotiveCount} locomotives and {self.__cartsCount} carts')
    
    def start_engine(self):
        Rail_vehicle.start_engine(self)
    def move(self):
        Rail_vehicle.move(self)
    def stop(self):
        Rail_vehicle.stop(self)

class Helicopter(Air_vehicle):
    def __init__(self, model, engine_count, pilots):
        self.__model = model
        self.__engine_count = engine_count
        self.__pilots = pilots
    
    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model
    property = (get_model, set_model)
    
    def get_engine_count(self):
        return self.__engine_count
    def set_engine_count(self, engine_count):
        self.__engine_count = engine_count
    property = (get_engine_count, set_engine_count)

    def get_pilots(self):
        return self.__pilots
    def set_pilots(self, pilots):
        self.__pilots = pilots
    property = (get_pilots, set_pilots)
    
    def transport(self):
        print(f'{self.__model} with {self.__engine_count} engines and {self.__pilots} pilots')
    
    def start_engine(self):
        Air_vehicle.start_engine(self)
    def move(self):
        Air_vehicle.move(self)
    def stop(self):
        Air_vehicle.stop(self)

class Railcar(Non_engine_ground_vehicle):
    def __init__(self, driver_count):
        self.__driver_count = driver_count
    
    def get_driver_count(self):
        return self.__driver_count
    def set_driver_count(self, driver_count):
        self.__driver_count = driver_count
    property = (get_driver_count, set_driver_count)

    def transport(self):
        print(f'railcar needs {self.__driver_count} drivers')
    def move(self):
        Non_engine_ground_vehicle.move(self)
    def stop(self):
        Non_engine_ground_vehicle.stop(self)

class Bicycle(Wheel_vehicle, Non_engine_ground_vehicle):
    def __init__(self, model, colour, type):
        self.__model = model
        self.__colour = colour
        self.__type = type

    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model
    property = (get_model, set_model)

    def get_colour(self):
        return self.__colour
    def set_colour(self, colour):
        self.__colour = colour
    property = (get_colour, set_colour)

    def get_type(self):
        return self.__type
    def set_type(self, type):
        self.__type = type 
    property = (get_type, set_type)

    def transport(self):
        print(f'{self.__colour} {self.__model} {self.__type} bicyle')
    def move(self):
        Non_engine_ground_vehicle.move(self)
    def stop(self):
        Non_engine_ground_vehicle.stop(self)

if __name__ == "__main__":
    wv=Wheel_vehicle('automobile',1986,2,4)
    wv.transport()
    c=Car('toyota',4,'sedan','red')
    c.transport()
    c.start_engine()
    c.move()
    c.stop()

    n=Non_engine_ground_vehicle(2,4)
    n.transport()
    r=Railcar(2)
    r.transport()
    r.move()
    r.stop()
    b=Bicycle('Aist','yellow','mountain')
    b.transport()
    b.move()
    b.stop()

    w=Water_vehicle('boat',1977,500,1)
    w.transport()
    j=Jetski('orange','yamaha')
    j.transport()
    j.start_engine()
    j.move()
    j.stop()

    rv=Rail_vehicle('train',1992,1.5)
    rv.transport()
    ct=Cargo_train('чс4т',3,50)
    ct.transport()
    ct.start_engine()
    ct.move()
    ct.stop()

    av=Air_vehicle('plane',2010,1100)
    av.transport()
    ap=Air_plane('boeing737',170)
    ap.transport()
    ap.start_engine()
    ap.move()
    ap.stop()
    h=Helicopter('ми24',2,2)
    h.transport()
    h.start_engine()
    h.move()
    h.stop()
















    







    



    



