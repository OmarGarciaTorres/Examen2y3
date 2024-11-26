def calculate_rectangle_area(width, height):
    """
    Calcula el área de un rectángulo.

    :param width: Ancho del rectángulo (debe ser positivo)
    :param height: Altura del rectángulo (debe ser positivo)
    :return: Área del rectángulo
    """
   if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
    raise TypeError("El ancho y la altura deben ser números.")
