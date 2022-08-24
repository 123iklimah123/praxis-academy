def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
        case 401 | 403 | 404:
            return "Not allowed"

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"x={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case point(x=0, y=0):
            print("Origin")
        case point(x=0, y=y):
            print(f"Y={y}")
        case point(x=x, y=0):
            print(f"X={x}")
        case point():
            print("Somewhere else")
        case _:
            print("Not a point")

point(1, var)
point(1, y=var)
point(x=1, y=var)
point(y=var, x=1)

match points:
    case []:
        print("No points")
    case [point(0, 0)]:
        print("The origin")
    case [point(x, y)]:
        print(f"Single point {x}, {y}")
    case [point(0, y1), point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("something else")

    match point:
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print(f"Not on the diagonal")

case (Point(x1, y1), Point(x2, y2) as p2):...

from enum import enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

    color = Color(input('Enter your choice of 'red', 'blue' or 'green': "))

    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")