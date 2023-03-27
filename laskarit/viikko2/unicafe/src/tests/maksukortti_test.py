import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(250)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.50 euroa")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(350)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.50 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_palauttaa_true_jos_rahat_riittivät_ja_muuten_false(self):
        tulos = self.maksukortti.ota_rahaa(800)

        self.assertEqual(tulos, True)

        tulos = self.maksukortti.ota_rahaa(300)
        
        self.assertEqual(tulos, False)