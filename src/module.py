def calculate_rectangle_area(width, height):
    """
    Calcula el área de un rectángulo.

    :param width: Ancho del rectángulo (debe ser positivo)
    :param height: Altura del rectángulo (debe ser positivo)
    :return: Área del rectángulo
    """
    if width <= 0 or height <= 0:
        raise ValueError("El ancho y la altura deben ser positivos.")
    return width * height
