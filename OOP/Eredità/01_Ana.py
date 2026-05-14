class Prodotto:
    def_init_(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
        
    def info(self):
        return f"{self.marca} - {self.tipo}"
        
    def prodotto_finito(self):
        return f"Il prodotto è finito"


    class prodottodettaglio(prodotto)
        def_init_(self, marca, tipo, prezzo)
        super()._init_(marca, tipo)
        self.prezzo = prezzo

    il_mio_prodotto=prodottodettaglio("Elseve", "Shampoo", 5)


prodotto_base = Prodotto("Elseve", "Shampoo")
print(f"Prodotto: {il_mio_prodotto.info()}, Prezzo: {il_mio_prodotto.prezzo}")
print(il_mio_prodotto.prodotto_finito())
