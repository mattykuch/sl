from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50, blank=True, default="")
	last_name = models.CharField(max_length=50, blank=True, default="")
	position = models.CharField(max_length=50, blank=True, default="")
	phone = models.CharField(max_length=20, blank=True, default="")

	ABIM = 'ABIM'
	ADJUMANI = 'ADJUMANI'
	AGAGO = 'AGAGO'
	ALEBTONG = 'ALEBTONG'
	AMOLATAR = 'AMOLATAR'
	AMUDAT = 'AMUDAT'
	AMURIA = 'AMURIA'
	AMURU = 'AMURU'
	APAC = 'APAC'
	ARUA = 'ARUA'
	BUDAKA = 'BUDAKA'
	BUDUDA = 'BUDUDA'
	BUGIRI = 'BUGIRI'
	BUHWEJU = 'BUHWEJU'
	BUIKWE = 'BUIKWE'
	BUKEDEA = 'BUKEDEA'
	BUKOMANSIMBI = 'BUKOMANSIMBI'
	BUKWO = 'BUKWO'
	BULAMBULI = 'BULAMBULI'
	BULIISA = 'BULIISA'
	BUNDIBUGYO = 'BUNDIBUGYO'
	BUSHENYI = 'BUSHENYI'
	BUSIA = 'BUSIA'
	BUTALEJA = 'BUTALEJA'
	BUTAMBALA = 'BUTAMBALA'
	BUVUMA = 'BUVUMA'
	BUYENDE = 'BUYENDE'
	DOKOLO = 'DOKOLO'
	DVSKCCAKAMPALA = 'DVSKCCAKAMPALA'
	GOMBA = 'GOMBA'
	GULU = 'GULU'
	HOIMA = 'HOIMA'
	IBANDA = 'IBANDA'
	IGANGA = "IGANGA"
	ISINGIRO = 'ISINGIRO'
	JINJA = 'JINJA'
	KAABONG = 'KAABONG'
	KABALE = 'KABALE'
	KABAROLE = 'KABAROLE'
	KABERAMAIDO = 'KABERAMAIDO'
	KALANGALA = 'KALANGALA'
	KALIRO = 'KALIRO'
	KALUNGU = 'KALUNGU'
	KAMPALA = 'KAMPALA'
	KAMULI = 'KAMULI'
	KAMWENGE = 'KAMWENGE'
	KANUNGU = 'KANUNGU'
	KAPCHORWA = 'KAPCHORWA'
	KASESE = 'KASESE'
	KATAKWI = 'KATAKWI'
	KAYUNGA = 'KAYUNGA'
	KIBAALE = 'KIBAALE'
	KIBOGA = 'KIBOGA'
	KIBUKU = 'KIBUKU'
	KIRUHURA = 'KIRUHURA'
	KIRYANDONGO = 'KIRYANDONGO'
	KISORO = 'KISORO'
	KISUBIHOSPITAL = 'KISUBIHOSPITAL'
	KITGUM = 'KITGUM'
	KOBOKO = 'KOBOKO'
	KOLE = 'KOLE'
	KOTIDO = 'KOTIDO'
	KUMI = 'KUMI'
	KWEEN = 'KWEEN'
	KYANKWANZI = 'KYANKWANZI'
	KYEGEGWA = 'KYEGEGWA'
	KYENJOJO = 'KYENJOJO'
	LAMWO = 'LAMWO'
	LIRA = 'LIRA'
	LUUKA = 'LUUKA'
	LUWEERO = 'LUWEERO'
	LWENGO = 'LWENGO'
	LYANTONDE = 'LYANTONDE'
	MANAFWA = 'MANAFWA'
	MARACHA = 'MARACHA'
	MASAKA = 'MASAKA'
	MASINDI = 'MASINDI'
	MAYUGE = 'MAYUGE'
	MBALE = 'MBALE'
	MBARARA = 'MBARARA'
	MITOOMA = 'MITOOMA'
	MITYANA = 'MITYANA'
	MOROTO = 'MOROTO'
	MOYO = 'MOYO'
	MPIGI = 'MPIGI'
	MUBENDE = 'MUBENDE'
	MUKONO = 'MUKONO'
	NAKAPIRIPIRIT = 'NAKAPIRIPIRIT'
	NAKASEKE = 'NAKASEKE'
	NAKASONGOLA = 'NAKASONGOLA'
	NAMAYINGO = 'NAMAYINGO'
	NAMUTUMBA = 'NAMUTUMBA'
	NAPAK = 'NAPAK'
	NEBBI = 'NEBBI'
	NGORA = 'NGORA'
	NTOROKO = 'NTOROKO'
	NTUNGAMO = 'NTUNGAMO'
	NWOYA = 'NWOYA'
	OTUKE = 'OTUKE'
	OYAM = 'OYAM'
	PADER = 'PADER'
	PALLISA = 'PALLISA'
	RAKAI = 'RAKAI'
	RUBIRIZI = 'RUBIRIZI'
	RUKUNGIRI = 'RUKUNGIRI'
	SEMBABULE = 'SEMBABULE'
	SERERE = 'SERERE'
	SHEEMA = 'SHEEMA'
	SIRONKO = 'SIRONKO'
	SOROTI = 'SOROTI'
	TORORO = 'TORORO'
	WAKISO = 'WAKISO'
	YUMBE = 'YUMBE'
	ZOMBO = 'ZOMBO'

	DISTRICT_CHOICES = (
		(ABIM, 'Abim'),
		(ADJUMANI, 'Adjumani'),
		(AGAGO, 'Agago'),
		(ALEBTONG, 'Alebtong'),
		(AMOLATAR, 'Amolatar'),
		(AMUDAT, 'Amudat'),
		(AMURIA, 'Amuria'),
		(AMURU, 'Amuria'),
		(APAC, 'Apac'),
		(ARUA, 'Arua'),
		(BUDAKA, 'Budaka'),
		(BUDUDA, 'Bududa'),
		(BUGIRI, 'Bugiri'),
		(BUHWEJU, 'Buhweju'),
		(BUIKWE, 'Buikwe'),
		(BUKEDEA, 'Bukedea'),
		(BUKOMANSIMBI, 'Bukomansimbi'),
		(BUKWO, 'Bukwo'),
		(BULAMBULI, 'Bulambuli'),
		(BULIISA, 'Buliisa'),
		(BUNDIBUGYO, 'Bundibugyo'),
		(BUSHENYI, 'Bushenyi'),
		(BUSIA, 'Busia'),
		(BUTALEJA, 'Butaleja'),
		(BUTAMBALA, 'Butambala'),
		(BUVUMA, 'Buvuma'),
		(BUYENDE, 'Buyende'),
		(DOKOLO, 'Dokolo'),
		(DVSKCCAKAMPALA, 'DVS KCCA Kampala'),
		(GOMBA, 'Gomba'),
		(GULU, 'Gulu'),
		(HOIMA, 'Hoima'),
		(IBANDA, 'Ibanda'),
		(IGANGA, 'Iganga'),
		(ISINGIRO, 'Isingiro'),
		(JINJA, 'Jinja'),
		(KAABONG, 'Kaabong'),
		(KABALE, 'Kabale'),
		(KABAROLE, 'Kabarole'),
		(KABERAMAIDO, 'Kaberamaido'),
		(KALANGALA, 'Kalangala'),
		(KALIRO, 'Kaliro'),
		(KALUNGU, 'Kalungu'),
		(KAMPALA, 'Kampala'),
		(KAMULI, 'Kamuli'),
		(KAMWENGE, 'Kamwenge'),
		(KANUNGU, 'Kanungu'),
		(KAPCHORWA, 'Kapchorwa'),
		(KASESE, 'Kasese'),
		(KATAKWI, 'Katakwi'),
		(KAYUNGA, 'Kayunga'),
		(KIBAALE, 'Kibaale'),
		(KIBOGA, 'Kiboga'),
		(KIBUKU, 'Kibuku'),
		(KIRUHURA, 'Kiruhura'),
		(KIRYANDONGO, 'Kiryandongo'),
		(KISORO, 'Kisoro'),
		(KISUBIHOSPITAL, 'Kisubi Hospital'),
		(KITGUM, 'Kitgum'),
		(KOBOKO, 'Koboko'),
		(KOLE, 'Kole'),
		(KOTIDO, 'Kotido'),
		(KUMI, 'Kumi'),
		(KWEEN, 'Kween'),
		(KYANKWANZI, 'Kyankwanzi'),
		(KYEGEGWA, 'Kyegegwa'),
		(KYENJOJO, 'Kyenjojo'),
		(LAMWO, 'Lamwo'),
		(LIRA, 'Lira'),
		(LUUKA, 'Luuka'),
		(LUWEERO, 'Luweero'),
		(LWENGO, 'Lwengo'),
		(LYANTONDE, 'Lyantonde'),
		(MANAFWA, 'Manafwa'),
		(MARACHA, 'Maracha'),
		(MASAKA, 'Masaka'),
		(MASINDI, 'Masindi'),
		(MAYUGE, 'Mayuge'),
		(MBALE, 'Mbale'),
		(MBARARA, 'Mbarara'),
		(MITOOMA, 'Mitooma'),
		(MITYANA, 'Mityana'),
		(MOROTO, 'Moroto'),
		(MOYO, 'Moyo'),
		(MPIGI, 'Mpigi'),
		(MUBENDE, 'Mubende'),
		(MUKONO, 'Mukono'),
		(NAKAPIRIPIRIT, 'Nakapiripirit'),
		(NAKASEKE, 'Nakaseke'),
		(NAKASONGOLA, 'Nakasongola'),
		(NAMAYINGO, 'Namayingo'),
		(NAMUTUMBA, 'Namutumba'),
		(NAPAK, 'Napak'),
		(NEBBI, 'Nebbi'),
		(NGORA, 'Ngora'),
		(NTOROKO, 'Ntoroko'),
		(NTUNGAMO, 'Ntungamo'),
		(NWOYA, 'Nwoya'),
		(OTUKE, 'Otuke'),
		(OYAM, 'Oyam'),
		(PADER, 'Pader'),
		(PALLISA, 'Pallisa'),
		(RAKAI, 'Rakai'),
		(RUBIRIZI, 'Rubirizi'),
		(RUKUNGIRI, 'Rukungiri'),
		(SEMBABULE, 'Sembabule'),
		(SERERE, 'Serere'),
		(SHEEMA, 'Sheema'),
		(SIRONKO, 'Sironko'),
		(SOROTI, 'Soroti'),
		(TORORO, 'Tororo'),
		(WAKISO, 'Wakiso'),
		(YUMBE, 'Yumbe'),
		(ZOMBO, 'Zombo'),

		)
	district_select = models.CharField(max_length=50,
									choices =DISTRICT_CHOICES,
									default =ABIM)
	facility = models.TextField(default="", blank=True)
