def piramide (piedras, col1, col2, col3):
    movimientos = []
    
    def mover(piedras, col1, col2, col3):
        if piedras == 1:
            movimientos.append()
        else:
            mover(piedras - 1, col1, col3, col2)
            movimientos.append((col1, col2))
            mover(piedras - 1, col3, col2, col1)
        
    mover(piedras, col1, col2, col3)