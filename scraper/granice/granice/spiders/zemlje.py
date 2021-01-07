import scrapy
import re
from granice.items import GraniceItem


class ZemljeSpider(scrapy.Spider):
    name = 'zemlje'
    allowed_domains = ['www.mfa.gov.rs']
    start_urls = ['http://www.mfa.gov.rs/sr/index.php/konzularni-poslovi/putovanja-u-inostranstvo/vesti-za-putovanja-u-inostranstvo?lang=lat&start=6/']

    def parse(self, response):
        # items
        granice = GraniceItem()
        
        #nadji deo sa kojim cemo da radimo
        content = response.css('table.blog table table')[1].css("td")[0]
        # print(content.get())

        #azurirano dana
        azurirano = content.re(r"ažurirano (05.01.2021.)")
        # zemlje
        zemlje = content.xpath('//strong/text()').getall()
        zemlje = zemlje[:-2]
        
        # detaljnije o ulasku u zemlju
        opis = re.findall(r"</strong>([\S\n\t\va-zA-Z\w\d\s]*?)<strong>", content.get())
        for i in range(len(opis)):
            opis_tmp = re.sub(r"<scrip([\S\n\t\v\s]*?)</script>", "", opis[i])
            opis[i] = re.sub(r"<br>", "\n", opis_tmp)
        
        # status
        status = [""]*len(opis)
        zatvoreno_reci = [
            "ne mogu",
            "nije dozvoljen",
            "zabranjen ulazak",

            ]
        otvoreno_reci = [
            "Srbije mogu",
            "Od putnika se traži da poseduju negativan PCR",
            "Putnici moraju prilikom dolaska posedovati negativan PCR test",
            " zahteva od svih putnika",
            "mogu da uđu državljani Srbije",
            "je dozvoljen",
            "Srbije mogu ući",
            "Srbije mogu ulaziti",
            "mogu da uđu",
            "potrebna viza",
            "dozvoljen je ulazak"
            ]
        for i in range(len(opis)):
            if (any(map(opis[i].__contains__, zatvoreno_reci))):
                status[i] += "❌"
            elif (any(map(opis[i].__contains__, otvoreno_reci))):
                status[i] += "✅"
                if "negativan PCR test" in opis[i]:
                    status[i] += "🧪"


        ##test podudaranja
        # print("Imamo ukupno zemalja:" + str(len(zemlje)) + " i ukupno opisa: " + str(len(opis)) )
        

        for i in range(0, len(zemlje)):
            granice['zemlja'] = zemlje[i]
            granice['opis'] = opis[i]
            granice['ulazak'] = status[i]
            granice['azurirano'] = azurirano

            yield granice