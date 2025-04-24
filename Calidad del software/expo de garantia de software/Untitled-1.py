class JuegoMemo:
    def __init__(self):
        self.memo = {}

    def jugada(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            return n
        self.memo[n] = self.jugada(n - 1) + self.jugada(n - 2)
        return self.memo[n]

juego = JuegoMemo()
nivel = int(input("Ingresa el nivel de jugada: "))
print("Resultado:", juego.jugada(nivel))