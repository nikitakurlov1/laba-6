from shapes import Triangle, Rectangle, Trapeze, Parallelogram, Circle

def create_shape(shape_type, params):
    try:
        if shape_type == "Triangle":
            return Triangle(*params)
        elif shape_type == "Rectangle":
            return Rectangle(*params)
        elif shape_type == "Trapeze":
            return Trapeze(*params)
        elif shape_type == "Parallelogram":
            return Parallelogram(*params)
        elif shape_type == "Circle":
            return Circle(*params)
    except (ValueError, TypeError) as e:
        print(f"Ошибка при создании фигуры {shape_type}: {e}")
    return None

def process_file(filename):
    shapes = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            shape_type = parts[0]
            params = [float(x) for x in parts[1:]]
            shape = create_shape(shape_type, params)
            if shape:
                shapes.append(shape)
    return shapes

def find_max_shapes(shapes):
    if not shapes:
        raise ValueError("Список фигур пуст")
    max_area_shape = max(shapes, key=lambda x: x.area())
    max_perimeter_shape = max(shapes, key=lambda x: x.perimeter())
    return max_area_shape, max_perimeter_shape

def main():
    files = ['input01 (1).txt', 'input02 (1).txt', 'input03 (1).txt']
    all_shapes = []
    
    for file in files:
        try:
            shapes = process_file(file)
            all_shapes.extend(shapes)
        except FileNotFoundError:
            print(f"Файл {file} не найден")
        except Exception as e:
            print(f"Ошибка при обработке файла {file}: {e}")
    
    if not all_shapes:
        print("Не удалось создать ни одной фигуры")
        return
        
    try:
        max_area_shape, max_perimeter_shape = find_max_shapes(all_shapes)
        
        print(f"Фигура с максимальной площадью: {type(max_area_shape).__name__}")
        print(f"Площадь: {max_area_shape.area():.2f}")
        print(f"Периметр: {max_area_shape.perimeter():.2f}")
        print()
        print(f"Фигура с максимальным периметром: {type(max_perimeter_shape).__name__}")
        print(f"Площадь: {max_perimeter_shape.area():.2f}")
        print(f"Периметр: {max_perimeter_shape.perimeter():.2f}")
    except Exception as e:
        print(f"Ошибка при поиске максимальных фигур: {e}")

if __name__ == "__main__":
    main() 