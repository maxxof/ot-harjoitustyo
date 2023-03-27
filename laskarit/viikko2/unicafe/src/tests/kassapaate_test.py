import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_saldo_aluksi_oikea_ja_tilastot_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii_jos_maksu_riittävä_edullinen_lounas(self):
        tulos = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(tulos, 60)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kassapaate_toimii_oikein_jos_kateismaksu_ei_riittava_edullinen_lounas(self):
        tulos = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(tulos, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_toimii_jos_maksu_riittävä_maukas_lounas(self):
        tulos = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(tulos, 50)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kassapaate_toimii_oikein_jos_kateismaksu_ei_riittava_maukas_lounas(self):
        tulos = self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(tulos, 350)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_jos_kortilla_tarpeeksi_rahaa_edullinen_lounas(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(tulos, True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_toimiii_jos_kortilla_tarpeeksi_rahaa_maukas_lounas(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(tulos, True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kassapaate_toimii_oikein_jos_kortilla_ei_ole_riittavasti_edullinen_lounas(self):
        maksukortti = Maksukortti(200)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(tulos, False)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kassapaate_toimii_oikein_jos_kortilla_ei_ole_riittavasti_maukas_lounas(self):
        maksukortti = Maksukortti(200)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(tulos, False)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kassan_kateinen_ei_muutu_kun_kaytetaan_korttia(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_rahaa_ladattaessa_saldo_muuttuu_ja_kassan_kateinen_kasvaa_oikealla_summalla(self):
        talletus = 650
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, talletus)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 16.50 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100650)

    def test_kortille_voi_lataa_vain_positiivista_summaa(self):
        talletus = -10
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, talletus)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)



    


    


    

